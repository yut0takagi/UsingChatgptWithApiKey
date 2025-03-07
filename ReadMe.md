# ChatGPTをAPIキーを使って利用する際のGUI
## 1.クローンする
```zsh
!git clone https://github.com/yut0takagi/UsingChatgptWithApiKey.git
```
## 2.pipenv環境に入り、必要なライブラリをインストールする
```zsh
pipenv shell
pipenv install -r requirements.txt
```
## 3. 環境変数として定義
以下のサイトを参照して設定してください。
[URL](https://www.javadrive.jp/command/command/index4.html#section4)

## 4. wsgiを用いてrun
```zsh
Python3 wsgi.py
```


