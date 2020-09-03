# coding: UTF-8
import sys

keys = ["ハッシュタグを入力してください(eg. #きのこ)", "データ取得開始日を入力してください(eg. 2020-08-28)", "データ取得終了日を入力してください(eg. 2020-08-30)", "取得ツイート件数を入力してください(eg. 100)" ]
params = []
for key in keys:
    print(key)
    data = sys.stdin.readline()
    params.append(data)

print(str(params).decode('string-escape'))

