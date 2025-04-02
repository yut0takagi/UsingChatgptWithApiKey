# 🧠 ChatGPT Webチャットアプリ（Flask製・ファイル対応）

このプロジェクトは、OpenAIのChatGPT APIを利用した **ファイルアップロード・モデル選択対応のチャットWebアプリケーション** です。  
完全にFlaskのみで構築されており、HTML/CSSにはTailwind CSSを使用しています。

---

## 📦 機能概要 / Features

- ✅ ChatGPTとの会話（gpt-3.5-turbo / gpt-4）
- ✅ PDF / テキストファイルのアップロード対応
- ✅ アップロードされたファイルを自動で読み取って質問できる
- ✅ ダークモードでシックなUI（Tailwind CSS）
- ✅ 完全ローカルで動作（APIキーさえあれば即使える）

---
## 🚀 セットアップ方法 / Setup(Webアプリから利用する場合)
1. [リンク](https://usingchatgptwithapikey.onrender.com/)から、アクセス   
    <img src="https://github.com/yut0takagi/UsingChatgptWithApiKey/blob/main/img/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202025-04-02%2017.59.42.png" alt="実行画面">
2. ChatGPT API KEYとモデルを選択,入力しチャット開始

## 🚀 セットアップ方法 / Setup(ローカルで利用する場合)

### 1. リポジトリのクローン

```bash
git clone https://github.com/yut0takagi/UsingChatgptWithApiKey.git
cd UsingChatgptWithApiKey
```

### 2. 仮想環境に入る

```bash
pipenv shell
```

### 3. ライブラリのインストール

```bash
pip install -r requirements.txt
```

### 4. OpenAI APIキーの設定

プロジェクトルートに `.env` ファイルを作成し、以下のように記述します：

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## ▶️ アプリの起動

```bash
python app.py
```

ブラウザで以下のURLを開きます：

```
http://127.0.0.1:5000
```

---

## 📁 ディレクトリ構成

```
chatgpt-flask-app/
├── app.py                 # Flaskアプリ本体
├── templates/
│   └── index.html         # チャット画面（Tailwind対応）
├── uploads/               # アップロードファイル保存用
├── .env                   # OpenAI APIキー
└── requirements.txt       # 必要ライブラリ一覧
```

---

## 📝 使用ライブラリ

- Flask
- python-dotenv
- openai
- PyPDF2①
- Tailwind CSS②

①: PDFのテキスト抽出用  
②: CDN経由で利用

---

## 📋 使用例

- テキストやPDFの資料を読み込ませて、ChatGPTに要約や質問を依頼
- 選んだモデルで違いを比較
- APIキーさえあれば誰でも使える、展開不要な軽量チャット環境

---

## 🔐 注意事項

- OpenAIの利用には **APIキーと当量費用制** が必要です
- アップロードされたファイルは `uploads/` に保存されます
- 必要に応じて、自動削除処理などを追加してください

---

## 🌐 English Summary

A minimal Flask web app for chatting with ChatGPT (gpt-3.5-turbo or gpt-4) with:

- File upload support (PDF, .txt)
- Tailwind CSS UI
- No database, just plug and play
- Requires an OpenAI API key

---

## 🤝 ライセンス / License

MIT License

---

## 💠 作者 / Author

- [yut0takagi](https://github.com/yut0takagi)

