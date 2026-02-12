# 🎯 HRdev スカウトメッセージ生成AI

株式会社HRdevの採用業務を効率化するための、Claude API を活用したスカウトメッセージ自動生成ツールです。

## 📋 概要

候補者のプロフィール情報と募集ポジション情報を入力するだけで、Claude（Sonnet 4.5）がパーソナライズされた魅力的なスカウトメッセージを自動生成します。

### 主な機能

- 📝 候補者情報の入力フォーム（名前、現職、スキル、経験年数等）
- 🎯 募集ポジション情報の入力
- 🤖 Claude APIによる高品質なスカウトメッセージ生成
- 📋 生成されたメッセージのコピー機能
- 💻 シンプルで直感的なWebインターフェース

## 🚀 セットアップ

### 1. 前提条件

- Python 3.8 以上
- Anthropic API Key（[こちら](https://console.anthropic.com/settings/keys)から取得）

### 2. インストール

```bash
# リポジトリをクローンまたはダウンロード
cd hrdev-scout-ai

# 仮想環境を作成（推奨）
python -m venv venv
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate

# 依存パッケージをインストール
pip install -r requirements.txt
```

### 3. 環境変数の設定

```bash
# .env.exampleをコピーして.envを作成
cp .env.example .env

# .envファイルを編集してAPIキーを設定
# ANTHROPIC_API_KEY=your_actual_api_key_here
```

## 💡 使い方

### アプリケーションの起動

```bash
streamlit run app.py
```

ブラウザが自動的に開き、`http://localhost:8501` でアプリケーションが表示されます。

### スカウトメッセージの生成手順

1. **候補者情報を入力**
   - 候補者名
   - 現在の勤務先
   - 現在の役職・ポジション
   - 主なスキル・技術スタック
   - 経験年数
   - 追加情報（任意）

2. **募集ポジション情報を入力**
   - 募集企業名
   - 募集ポジション

3. **「✨ スカウトメッセージを生成」ボタンをクリック**

4. **生成されたメッセージを確認・コピー**
   - 数秒で高品質なスカウトメッセージが生成されます
   - コードブロック内のメッセージをコピーして使用できます

## 📂 プロジェクト構成

```
hrdev-scout-ai/
├── app.py              # Streamlitアプリケーションのメインファイル
├── requirements.txt    # 依存パッケージ一覧
├── .env.example        # 環境変数のサンプル
├── .gitignore          # Git管理除外ファイル
└── README.md           # このファイル
```

## 🛠️ 技術スタック

- **Python 3.8+**: プログラミング言語
- **Streamlit**: WebUIフレームワーク
- **Anthropic Python SDK**: Claude API クライアント
- **Claude Sonnet 4.5**: AI モデル

## 💰 コストについて

Claude API の利用には料金がかかります（従量課金制）。

- **Sonnet 4.5**: 入力 $3/MTok、出力 $15/MTok
- 1回のスカウトメッセージ生成: 約 $0.01〜0.02 程度

詳細は [Anthropic の料金ページ](https://www.anthropic.com/pricing) をご確認ください。

## 🎨 カスタマイズ

### プロンプトの調整

[app.py](app.py#L35-L60) の `generate_scout_message` 関数内のプロンプトを編集することで、生成されるメッセージのトーンやスタイルをカスタマイズできます。

### モデルの変更

より高速な応答が必要な場合は、`claude-haiku-4-5-20251001` に変更することも可能です（コストも削減されます）。

```python
# app.py 内
model="claude-haiku-4-5-20251001"  # より高速・低コスト
```

## 🔒 セキュリティ

- `.env` ファイルは `.gitignore` に含まれており、Git管理から除外されています
- API キーは環境変数で管理し、コードに直接記述しないでください
- 本番環境では、適切なアクセス制御を実装してください

## 📝 今後の拡張案

- [ ] 複数のスカウトメッセージバリエーションを一度に生成
- [ ] 過去の成功したスカウトメッセージのテンプレート保存機能
- [ ] CSV一括アップロードによる複数候補者への一括生成
- [ ] 生成履歴の保存と管理
- [ ] A/Bテスト用の複数トーン生成（カジュアル/フォーマル等）
- [ ] Notionデータベース連携

## 📞 サポート

質問や問題が発生した場合は、社内Slackチャンネルまたは開発チームまでお問い合わせください。

---

**Powered by Claude API (Sonnet 4.5) | 株式会社HRdev**
