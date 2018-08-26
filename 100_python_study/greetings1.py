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
