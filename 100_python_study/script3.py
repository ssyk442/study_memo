from greetings2 import GermanGreetings, NorwegianGreetings

# 名前の入力
name = input("What's your name?: ")
print("------------------------")

# 自己紹介したい言語の選択
print("In which language do you want to introduce yourself?")
selected_language = int(input("Please choose the number. - 0.German 1.Norwegian: "))

# エラーチェック本当は必要

print("------------------------")

# Pythonでの親クラスの定義の仕方を知りたい
german_greeting = GermanGreetings(name)
norwegian_greeting = NorwegianGreetings(name)

# 0.German 1.Norwegian
greetings = [german_greeting,norwegian_greeting]

# 出力結果
greetings[selected_language].self_introducing()
