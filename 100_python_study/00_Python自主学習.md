## Pythonのバージョン確認
| Python2     | Python3             |
| ----------- | ------------------- |
| $ python -V | $ python3 --version |

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
greetings.py
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
