### リモートリポジトリからローカルリポジトリへ同期する
$ cd ローカルリポジトリ  
$ git pull origin master

### ディレクトリ名の大文字・小文字の差分を認識させる
#### 注：ローカル側では大文字小文字を差分扱いしないが、リモート側では差分扱いすることがある(＝同名ファイルがリモート上2ファイルできる)為、ローカル側で大文字・小文字の変換をしないこと！
$ git config core.ignorecase false

### ローカルリポジトリの変更ステータスを確認する
$ git status

### ローカルリポジトリの変更箇所の差分を確認する
$ git diff

### ローカルリポジトリ内ファイルの変更をコミット可能な状態にする
1. ファイル名指定の場合  
$ git add "FILENAME"

2. 全ファイル  
$ git add .

### ローカルリポジトリの中身をコミットする
$ git commit -m "message"

### GitHubのリモートリポジトリ情報を追加する(初回のみ)
$ git remote add origin <リモートリポジトリ情報(GitHubの"Clone or download"のところ)>

### ローカルリポジトリをリモートリポジトリに反映する
$ git push origin master

### GitHubにpushできない場合の対処方法(publickey関連)
$ eval "$(ssh-agent -s)"  
$ ssh-add ~/.ssh/id_rsa # github用のssh-keyへのパス
