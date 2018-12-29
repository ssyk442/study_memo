import os

# テキストファイルを開き、ファイルに書き込む(上書き)
test_file = open(os.path.abspath('test.txt'), 'w')
test_file.write("hello python!\n")
test_file.close()

# テキストファイルを開き、ファイルに書き込む(追記)
test_file = open(os.path.abspath('test.txt'), 'a')
test_file.write("i'm back, because i'm now in winter vacation!\n")
test_file.write("i'm really glad to see you again :)\n")
test_file.close()

# テキストファイルを読み込む
test_file = open(os.path.abspath('test.txt'))
test_content = test_file.read()
print(test_content)
test_file.close()

# 1行ずつの文字列のリストとしてファイルを読み込む
test_file = open(os.path.abspath('test.txt'))
test_content = test_file.readlines()
print(test_content)
test_file.close()
