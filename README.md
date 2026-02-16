<div align="center">

# 🎯 Scout AI

### AI-Powered Personalized Scout Message Generator

**Claude API (Sonnet 4.5)を活用した、候補者へのスカウトメッセージ自動生成ツール**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.31+-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Claude API](https://img.shields.io/badge/Claude-Sonnet%204.5-8B5CF6?style=flat)](https://www.anthropic.com/)

[主な機能](#-主な機能) • [使用例](#-使用例) • [セットアップ](#-セットアップ) • [使い方](#-使い方)

</div>

---

## ✨ 主な機能

<table>
<tr>
<td width="50%">

### 🤖 AI自動生成
Claude Sonnet 4.5による高品質でパーソナライズされたスカウトメッセージを数秒で生成

</td>
<td width="50%">

### 📝 シンプルなUI
候補者情報と募集ポジションを入力するだけの直感的なインターフェース

</td>
</tr>
<tr>
<td width="50%">

### 🎯 カスタマイズ可能
プロンプト編集により、メッセージのトーンやスタイルを柔軟に調整可能

</td>
<td width="50%">

### 📋 ワンクリックコピー
生成されたメッセージを即座にコピーして使用可能

</td>
</tr>
</table>

---

## 🎬 使用例

**候補者情報を入力**
```
名前: 山田太郎様
現職: 株式会社テックカンパニー / シニアソフトウェアエンジニア
スキル: Python, React, AWS, Docker, スクラム開発
経験: 5年
```

**募集ポジション**
```
企業: 株式会社〇〇
ポジション: プロダクトエンジニア（バックエンド）
```

**生成されるメッセージ（例）**
> 山田太郎様
>
> 突然のご連絡失礼いたします。〇〇と申します。
>
> 山田様のPythonとReactを活用したフルスタック開発のご経験、特にAWSとDockerを用いたモダンなインフラ構築のスキルに大変注目しております...

---

## 🚀 セットアップ

### 前提条件

- **Python 3.8以上**
- **Anthropic API Key** - [こちら](https://console.anthropic.com/settings/keys)から取得

### インストール

```bash
# 1. リポジトリをクローン
git clone <repository-url>
cd scout-ai

# 2. 仮想環境を作成
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. 依存パッケージをインストール
pip install -r requirements.txt

# 4. 環境変数を設定
cp .env.example .env
# .envファイルを編集してAPIキーを設定
```

### 環境変数の設定

`.env`ファイルに以下を記述:

```bash
ANTHROPIC_API_KEY=your_api_key_here
```

---

## 💡 使い方

### 1. アプリケーションを起動

```bash
streamlit run app.py
```

ブラウザで自動的に `http://localhost:8501` が開きます。

### 2. 情報を入力

左カラム（候補者情報）:
- 候補者名
- 現在の勤務先
- 現在の役職
- 主なスキル
- 経験年数
- 追加情報（任意）

右カラム（募集ポジション情報）:
- 募集企業名
- 募集ポジション

### 3. メッセージを生成

「✨ スカウトメッセージを生成」ボタンをクリック

### 4. コピーして使用

生成されたメッセージをコピーして、候補者へ送信

---

## 🛠️ 技術スタック

| カテゴリ | 技術 |
|---------|------|
| **言語** | Python 3.8+ |
| **フレームワーク** | Streamlit |
| **AI API** | Anthropic Claude (Sonnet 4.5) |
| **依存管理** | python-dotenv, anthropic SDK |

---

## 📂 プロジェクト構成

```
scout-ai/
├── app.py              # メインアプリケーション
├── requirements.txt    # 依存パッケージ
├── .env.example        # 環境変数サンプル
├── .env               # 環境変数（Git管理外）
├── .gitignore         # Git除外設定
└── README.md          # このファイル
```

---

## 🎨 カスタマイズ

### プロンプトの調整

`app.py`の`generate_scout_message`関数内のプロンプトを編集することで、メッセージのトーンやフォーマットを変更できます。

```python
# app.py L34-54
prompt = f"""あなたは採用支援の優秀なリクルーターです。
以下の候補者情報をもとに、魅力的でパーソナライズされた
スカウトメッセージを作成してください。
...
"""
```

### モデルの変更

コストや速度を最適化したい場合:

```python
# app.py L58
model="claude-haiku-4-5-20251001"  # より高速・低コスト
# または
model="claude-opus-4-6"  # より高品質
```

---

## 💰 コスト目安

| モデル | 入力 | 出力 | 1メッセージあたり |
|-------|------|------|-----------------|
| **Sonnet 4.5** | $3/MTok | $15/MTok | ~$0.01-0.02 |
| Haiku 4.5 | $1/MTok | $5/MTok | ~$0.003-0.01 |
| Opus 4.6 | $15/MTok | $75/MTok | ~$0.05-0.10 |

詳細: [Anthropic Pricing](https://www.anthropic.com/pricing)

---

## 🔒 セキュリティ

- ✅ `.env`ファイルは`.gitignore`で保護
- ✅ APIキーは環境変数で管理
- ✅ 認証情報はコードに直接記述しない
- ⚠️ 本番環境では適切なアクセス制御を実装

---

## 🚧 今後の拡張予定

- [ ] LinkedIn プロフィールからの自動情報抽出
- [ ] 複数バリエーション同時生成
- [ ] CSV一括アップロード対応
- [ ] 生成履歴の保存・管理機能
- [ ] A/Bテスト用の複数トーン生成
- [ ] Notion / Airtable 連携

---

## 📄 ライセンス

このプロジェクトは個人ポートフォリオ用です。

---

<div align="center">

**Powered by [Claude API](https://www.anthropic.com/) (Sonnet 4.5)**

</div>
