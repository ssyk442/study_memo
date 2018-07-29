## リモートリポジトリからローカルリポジトリへ同期する
$ cd ローカルリポジトリ  
$ git pull origin master

## ローカルリポジトリの変更ステータスを確認する
$ git status

## ローカルリポジトリの変更箇所の差分を確認する
$ git diff

## ローカルリポジトリ内ファイルの変更をコミット可能な状態にする
1. ファイル名指定の場合  
$ git add "FILENAME"

2. 全ファイル  
$ git add .

## ローカルリポジトリの中身をコミットする
$ git commit -m "message"

## GitHubのリモートリポジトリ情報を追加する(初回のみ)
$ git remote add origin <リモートリポジトリ情報(GitHubの"Clone or download"のところ)>

## ローカルリポジトリをリモートリポジトリに反映する
$ git push origin master
