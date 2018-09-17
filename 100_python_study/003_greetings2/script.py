from german_greetings import GermanGreetings
from norwegian_greetings import NorwegianGreetings
from icelandic_greetings import IcelandicGreetings
from spanish_greetings import SpanishGreetings
from basque_greetings import BasqueGreetings

# --------------------------------------
# グローバル変数っぽくしたい(他クラスからも同じ定数呼びたい)
GERMAN = '0'
NORWEGIAN = '1'
ICELANDIC = '2'
SPANISH = '3'
BASQUE = '4'

GENDER_MALE = "0"
GENDER_FEMALE = "1"
# --------------------------------------
# 選択言語コードチェック
def check_language_id(id):
    return{
        GERMAN:True    # German
        ,NORWEGIAN:True   # Norwegian
        ,ICELANDIC:True   # Icelandic
        ,SPANISH:True   # Spanish
        ,BASQUE:True    # Basque
    }.get(id,False) # other ids aren't valid
# --------------------------------------
# 選択性別コードチェック
def check_gender_id(id):
    return{
        GENDER_MALE:True    # male
        ,GENDER_FEMALE:True   # female
    }.get(id,False) # other ids aren't valid
# --------------------------------------

# 名前の入力
name = ''
while not name:
    name = input("Please enter your name.: ")

# 自己紹介したい言語の選択
print(name + ", in which language do you want to introduce yourself?")

language_id = ''
while not language_id:
    language_id = input("Please select the number. \n- 0.German 1.Norwegian 2.Icelandic 3.Spanish 4.Basque: ")
    # 想定値以外を入力した場合は再度入力を促す
    if not check_language_id(language_id):
        language_id = ''

# 自己紹介する人の性別(スペイン語)
my_gender_id = ''
langs_using_my_gender = [SPANISH]

if language_id in langs_using_my_gender:
    while not my_gender_id:
        my_gender_id = input("Please select your gender. \n- 0.male 1.female: ")
        # 想定値以外を入力した場合は再度入力を促す
        if not check_gender_id(my_gender_id):
            my_gender_id = ''

# 自己紹介したい相手の性別(アイスランド語)
others_gender_id = ''
langs_using_others_gender = [ICELANDIC]

if language_id in langs_using_others_gender:
    while not others_gender_id:
        others_gender_id = input("Please select the gender who you want to introduce yourself. \n- 0.male 1.female: ")
        # 想定値以外を入力した場合は再度入力を促す
        if not check_gender_id(others_gender_id):
            others_gender_id = ''

print("------------------------")

# インスタンス化
if language_id == GERMAN:
    greetings = GermanGreetings(name)
elif language_id == NORWEGIAN:
    greetings = NorwegianGreetings(name)
elif language_id == ICELANDIC:
    greetings = IcelandicGreetings(name, others_gender_id)
elif language_id == SPANISH:
    greetings = SpanishGreetings(name, my_gender_id)
elif language_id == BASQUE:
    greetings = BasqueGreetings(name)
# elseは通り得ないが、言語追加の度else=>elifに直すのが嫌なので
# ダミーelseを作っておく
else:
    greetings = Greetings(name)

# 出力結果
print(greetings.self_introducing())
print("------------------------")
