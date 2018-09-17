from german_greetings import GermanGreetings
from norwegian_greetings import NorwegianGreetings
from icelandic_greetings import IcelandicGreetings

# --------------------------------------
GERMAN = '0'
NORWEGIAN = '1'
ICELANDIC = '2'
# ここ一本化したい
GENDER_MALE = "0"
GENDER_FEMALE = "1"
# --------------------------------------
# 選択言語コードチェック
def check_language_id(id):
    return{
        GERMAN:True    # German
        ,NORWEGIAN:True   # Norwegian
        ,ICELANDIC:True   # Icelandic
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
    language_id = input("Please choose the number. - 0.German 1.Norwegian 2.Icelandic: ")
    # 想定値以外を入力した場合は再度入力を促す
    if not check_language_id(language_id):
        language_id = ''

# 自己紹介する人の性別
# my_gender_id = ''
# while not my_gender_id:
#     my_gender_id = input("Please choose your gender. - 0.male 1.female: ")
#     # 想定値以外を入力した場合は再度入力を促す
#     if not check_gender_id(my_gender_id):
#         my_gender_id = ''

if language_id == ICELANDIC:
    # 自己紹介したい相手の性別(アイスランド語の場合必要)
    others_gender_id = ''
    while not others_gender_id:
        others_gender_id = input("Please choose the gender who you want to introduce yourself. - 0.male 1.female: ")
        # 想定値以外を入力した場合は再度入力を促す
        if not check_gender_id(others_gender_id):
            others_gender_id = ''

print("------------------------")

# 0.German 1.Norwegian 2.Icelandic
if language_id == GERMAN:
    greetings = GermanGreetings(name)
elif language_id == NORWEGIAN:
    greetings = NorwegianGreetings(name)
else:
    greetings = IcelandicGreetings(name, others_gender_id)

# 出力結果
print(greetings.self_introducing())
