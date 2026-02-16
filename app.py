import streamlit as st
import anthropic
import os
from typing import Optional
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# ページ設定
st.set_page_config(
    page_title="Scout AI - スカウトメッセージ生成",
    page_icon="🎯",
    layout="wide"
)

def get_anthropic_client() -> Optional[anthropic.Anthropic]:
    """Anthropic APIクライアントを初期化"""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        st.error("⚠️ ANTHROPIC_API_KEYが設定されていません。環境変数を設定してください。")
        return None
    return anthropic.Anthropic(api_key=api_key)

def generate_scout_message(
    client: anthropic.Anthropic,
    candidate_name: str,
    current_company: str,
    current_position: str,
    skills: str,
    experience_years: int,
    target_position: str,
    target_company: str,
    additional_info: str = ""
) -> str:
    """Claude APIを使ってスカウトメッセージを生成"""

    prompt = f"""あなたは採用支援の優秀なリクルーターです。以下の候補者情報をもとに、魅力的でパーソナライズされたスカウトメッセージを作成してください。

【候補者情報】
- 名前: {candidate_name}様
- 現職: {current_company} / {current_position}
- 主なスキル: {skills}
- 経験年数: {experience_years}年
- 追加情報: {additional_info if additional_info else "なし"}

【募集ポジション】
- 企業名: {target_company}
- ポジション: {target_position}

【スカウトメッセージ作成のポイント】
1. 候補者のスキルや経験を具体的に評価し、なぜこの方をスカウトするのか明確にする
2. 募集ポジションの魅力を簡潔に伝える
3. 押し付けがましくなく、カジュアル面談への誘導を自然に行う
4. 文章は丁寧ながらも親しみやすいトーンで
5. 長すぎず（300-400文字程度）、読みやすい構成にする

上記を踏まえて、スカウトメッセージを作成してください。"""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return message.content[0].text
    except Exception as e:
        st.error(f"❌ メッセージ生成中にエラーが発生しました: {str(e)}")
        return ""

def main():
    # ヘッダー
    st.title("🎯 Scout AI - スカウトメッセージ生成")
    st.markdown("**Claude API を活用した、パーソナライズされたスカウトメッセージ自動生成ツール**")
    st.divider()

    # APIクライアント初期化
    client = get_anthropic_client()
    if not client:
        st.info("💡 `.env`ファイルに`ANTHROPIC_API_KEY=your_api_key`を設定するか、環境変数を設定してください。")
        st.stop()

    # 2カラムレイアウト
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("📋 候補者情報")

        candidate_name = st.text_input(
            "候補者名",
            placeholder="例: 山田太郎",
            help="スカウトする候補者の名前を入力してください"
        )

        current_company = st.text_input(
            "現在の勤務先",
            placeholder="例: 株式会社テックカンパニー",
            help="候補者の現在の勤務先"
        )

        current_position = st.text_input(
            "現在の役職・ポジション",
            placeholder="例: シニアソフトウェアエンジニア",
            help="候補者の現在の役職"
        )

        skills = st.text_area(
            "主なスキル・技術スタック",
            placeholder="例: Python, React, AWS, Docker, スクラム開発",
            help="候補者の保有スキルや技術スタックをカンマ区切りで入力",
            height=100
        )

        experience_years = st.number_input(
            "経験年数",
            min_value=0,
            max_value=50,
            value=5,
            help="候補者の総エンジニア経験年数"
        )

        additional_info = st.text_area(
            "追加情報（任意）",
            placeholder="例: GitHub での OSS 活動が活発、技術ブログを運営",
            help="候補者のユニークな特徴や実績があれば記入",
            height=80
        )

    with col2:
        st.subheader("🎯 募集ポジション情報")

        target_company = st.text_input(
            "募集企業名",
            placeholder="例: 株式会社〇〇",
            help="スカウト先の企業名"
        )

        target_position = st.text_input(
            "募集ポジション",
            placeholder="例: プロダクトエンジニア（バックエンド）",
            help="募集しているポジション名"
        )

        st.markdown("---")

        # 生成ボタン
        generate_button = st.button(
            "✨ スカウトメッセージを生成",
            type="primary",
            use_container_width=True
        )

    # メッセージ生成
    if generate_button:
        if not all([candidate_name, current_company, current_position, skills, target_company, target_position]):
            st.warning("⚠️ 必須項目（追加情報以外）をすべて入力してください。")
        else:
            with st.spinner("🤖 Claude がスカウトメッセージを作成しています..."):
                scout_message = generate_scout_message(
                    client=client,
                    candidate_name=candidate_name,
                    current_company=current_company,
                    current_position=current_position,
                    skills=skills,
                    experience_years=experience_years,
                    target_position=target_position,
                    target_company=target_company,
                    additional_info=additional_info
                )

                if scout_message:
                    st.divider()
                    st.subheader("📧 生成されたスカウトメッセージ")
                    st.success(scout_message)

                    # コピーボタン
                    st.code(scout_message, language=None)
                    st.caption("👆 上記のメッセージをコピーして使用してください")

    # フッター
    st.divider()
    st.caption("Powered by Claude API (Sonnet 4.5)")

if __name__ == "__main__":
    main()
