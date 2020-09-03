# シェルスクリプトの作り方
参考記事:https://qiita.com/saki-engineering/items/57956af61c191b0e3282
## 1. シェルコマンドを書く
必ず #!/bin/bashを書くこと。
ファイル名(拡張子なし)がそのままコマンドになる
ex):twitterというファイルを作る場合

```
touch twitter
```
```
// twitterファイルの中身
#!/bin/sh
cd ~/Desktop/get_old_tweet/python3_docker
docker-compose up -d
docker exec python3 python opt/got3.py
cp opt/tweet_hokuto.csv ~/Desktop
docker-compose down
open ~/Desktop/tweet_hokuto.csv
```

## 2. スクリプトファイルを任意の場所に置き、シンボリックリンクを貼る
例えば、~/commandディレクトリにtwitterコマンドをおき、
/usr/local/binにシンボリックリンクを貼る場合
```
ln -si ~/command/twitter /usr/local/bin
```
echoでパスを確認できる
```
echo $PATH
/Users/md-mashimo/.nodebrew/current/bin:/usr/local/bin:/usr/local/sbin:/usr/bin:/bin:/usr/sbin:/sbin
```

## 3. コマンドに実行権限を付与する

```
chmod 777 ~/command/twitter
```
