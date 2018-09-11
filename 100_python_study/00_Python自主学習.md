## Pythonのバージョン確認
| Python2     | Python3             |
| ----------- | ------------------- |
| $ python -V | $ python3 --version |

=> 20180827追記  
pyenvにバージョンの設定をすれば、バージョンの切り替えができるようになる。特に2系と3系の切り替えが楽になる。  

$ python --version

## pyenv
pyenvをインストールすると、複数のバージョンが管理できる。  

pyenvのインストール、使い方、pythonのバージョン切り替えできない時の対処法(@koooooo)
https://qiita.com/koooooo/items/b21d87ffe2b56d0c589b

以降、Python3を想定

## .pyファイル実行
- $ cd [.pyファイルがあるディレクトリ]
- $ python3 [実行したいファイル.py]

##    文字列出力
[ファイル名].py
```
print('hello python')
print("hello python")
# either double-quoted or quoted strings is okay in python
# Ruby => puts "hello ruby"
# Java => System.out.println("hello java");
```

## 型変換str
```
member_count = 3
print("Sigur Rós has " + str(member_count) + " members now.")

=> Sigur Rós has 3 members now.
```

## 型変換inc
```
count = '3'
price = 100
total_price = price * int(count)
print(total_price)

=> 300
```

## 条件式
- <b>インデント超大事！</b>

```
score = 100
if score == 100:
    print('Good job!')
    print('You're GENIOUS!!')

# 100の場合
    => Good job!
    => You're GENIOUS!!

# 100以外の場合
    => null
```
```
if score == 100:
    print('Good job!')
print('You're GENIOUS!!Oops!')

# 100の場合
    => Good job!
    => You're GENIOUS!!Oops!

# 100以外の場合
    => You're GENIOUS!!Oops!
```
```
member_count = 3
if not member_count == 4:
    print('Kjartan is already left Sigur Rós.')

=> Kjartan is already left Sigur Rós.
```
Comparing 3 languages
```
# in Python
if score == 100:
    print('Good job!')
    print('You're GENIOUS!!')

elif score >= 65:
    print('Pretty good.')

else:
    print(':<')

# you don't need "end" in python
```
```
# in Ruby
score = 100
if score == 100
    puts "Good job!"
    puts "You're GENIOUS!!"

elsif score >= 65
    puts "Pretty good."

else
    puts ":<"

end
```
```
// in Java
int score = 70;
if ( score == 100 ) {
    System.out.println("Good job!");
    System.out.println("You're GENIOUS!!");

} else if ( score >= 65 ) {
    System.out.println("Pretty good.");

} else {
    System.out.println(":<");
}    
```

## コンソールから入力値を受け取る
```
input_count = input('Please input the number of apples you want to purchase:')
print('I will buy ' + input_count + 'apples.')
```
```
numbers = input().rstrip().split(' ')
result = int(numbers[0]) + int(numbers[1])
print(  result)

# input
2 3
# output
5
```

## for文
```
countries = ['Iceland','Greenland','Singapore','Taiwan']
for country in countries:
    print('I traveled ' + country + '!')
```
result
```
I traveled Iceland!
I traveled Greenland!
I traveled Singapore!
I traveled Taiwan!
```

## 辞書

```
countries = {'Iceland':'氷島','Singapore':'新嘉坡'}
countries['Singapore'] = '星港'
countries['Malaysia'] = '馬来西亜'
print(countries)
for country in countries:
    print(country + ' is written ' + countries[country] + ' in Kanji.' )
```
result
```
{'Iceland': '氷島', 'Singapore': '星港', 'Malaysia': '馬来西亜'}
Iceland is written 氷島 in Kanji.
Singapore is written 星港 in Kanji.
Malaysia is written 馬来西亜 in Kanji.
```

## 関数
002_greetings1/greetings.py
```
import random

def hello(name):
    print('Hello world! My name is ' + name + ' :)')

def greeting_german(name, message='Freut mich!'):
    print('Guten Tag! Mein Name ist ' + name + '.')
    print(message)

def greeting_english(name, message='Nice to meet you!'):
    random_number = random.randint(1,99)
    print('Hello! My name is ' + name + '.')
    print(message)
    print('By the way, my lucky number today is ' + str(random_number) + '!')

```
script1.py
```
import greetings

greetings.greeting_german('Schneider','Ich komme aus Schweiz.')
greetings.greeting_german('Leonardo')
```
$ python3 script1.py
```
Guten Tag! Mein Name ist Schneider.
Ich komme aus Schweiz.
Guten Tag! Mein Name ist Leonardo.
Freut mich!
```
script2.py
```
import greetings

greetings.greeting_english('Doraemon','Please give me dorayaki.')
```
$ python3 script2.py
```
Hello! My name is Doraemon.
Please give me dorayaki.
By the way, my lucky number today is 66!
```

## class
003_greetings2/greetings.py
```
class IcelandicGreetings:
    pass

class GermanGreetings:
    # __init__メソッドはインスタンス化直後に必ず呼ばれる
    def __init__(self,name):
        self.name = name

    def morning_greeting(self):
        print('Guten Morgen!')

    def self_introducing(self):
        print('Hallo!')
        print('Mein Name ist ' + self.name + '.')
        print('Freut mich!')

class NorwegianGreetings:
    def __init__(self,name):
        self.name = name

    def morning_greeting(self):
        print('God morgen!')

    def self_introducing(self):
        print('Hei!')
        print('Jeg heter ' + self.name + '.')
        print('Hyggelig å se deg!')
```
script.py
```
from greetings import GermanGreetings, NorwegianGreetings

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
```
$ python3 script3.py  
ex1.result(名前:Masamune 言語:German)
```
What's your name?: Masamune
------------------------
In which language do you want to introduce yourself?
Please choose the number. - 0.German 1.Norwegian: 0
------------------------
Hallo!
Mein Name ist Masamune.
Freut mich!
```
ex2.result(名前:Tsunenaga 言語:Norwegian)
```
What's your name?: Tsunenaga
------------------------
In which language do you want to introduce yourself?
Please choose the number. - 0.German 1.Norwegian: 1
------------------------
Hei!
Jeg heter Tsunenaga.
Hyggelig å se deg!
```
#### Javaとの違い
- クラスをインスタンス化した後、そのインスタンス変数に対して、元となったクラスで定義されていない変数を自由に定義できてしまう。(「Pythonはこれもできてしまう」のところ)
- 引数なしの場合でも必ず"self"を定義しなければならない。引数ありの場合は、selfの後ろに定義していく。尚、渡す引数はself以降の引数のみを順に入れていく。
- Javaのコンストラクタは、Pythonでは`__init__`メソッドで定義するっぽい。

#### Pythonはこれもできてしまう
```
class GermanGreetings:
def self_introducing(self):
    print('Guten Tag!')
    print('Mein Name ist ' + self.name + '.')
    print('Freut mich!')

german_greeting = GermanGreetings()
# クラス側に未定義の変数↓
german_greeting.name = 'Oliver'
print(german_greeting.name)
```
## 端数処理
- 四捨五入 round(数値)

## 継承
```
# 子クラス(親クラス)
class GermanGreetings(Greetings):
    pass
```
- 「親クラス(上位)を継承する」と「サブルーチン(下位)を呼ぶ」は、共通処理を呼ぶという意味では共通だが、呼び先が上位なのか下位なのかが異なる。
- 子クラスは親クラスのメソッドをそのまま使える。子クラス側で独自にメソッドを定義してもok。
- オーバーライドはJavaと同じ発想。子クラスに同名メソッドがある場合、子クラスのメソッドが呼ばれる。


## インタフェース
PythonでC#やJavaのinterfaceみたいなものを実現する(@baikichiz)
https://qiita.com/baikichiz/items/7c3fdb721bb72644f638

29.7. abc — 抽象基底クラス  
https://docs.python.jp/3/library/abc.html

Pythonは多重継承を許す。

## 正規表現
##### 参考：「退屈なことはPythonにやらせようーノンプログラマーにもできる自動化処理プログラミング」(Al Sweigart著 相川 愛三訳 オライリー・ジャパン)
- import re(正規表現モジュール)
- re.compile()で検索したい正規表現(Regexオブジェクト)を返す。
- Regexオブジェクトのsearch()内に上記正規表現のパターンがないか検索する。ある場合は、Matchオブジェクトに合致した部分を返す。
- Matchオブジェクトのgroup()メソッドでマッチしたテキストを返す。
