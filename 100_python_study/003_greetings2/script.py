from german_greetings import GermanGreetings
from norwegian_greetings import NorwegianGreetings

# --------------------------------------
# 選択言語コードチェック
def check_language_id(id):
    return{
        '0':True    # German
        ,'1':True   # Norwegian
    }.get(id,False) # other ids aren't valid
# --------------------------------------

# 名前の入力
name = ''
while not name:
    name = input("What's your name?: ")
print("------------------------")

# 自己紹介したい言語の選択
print(name + ", in which language do you want to introduce yourself?")

language_id = ''
while not language_id:
    language_id = input("Please choose the number. - 0.German 1.Norwegian: ")
    # 想定値以外を入力した場合は再度入力を促す
    if not check_language_id(language_id):
        language_id = ''

print("------------------------")

# 0.German 1.Norwegian
greetings = [
    GermanGreetings(name)
    ,NorwegianGreetings(name)
    ]

# 出力結果
language_index = int(language_id)
print(greetings[language_index].self_introducing())
