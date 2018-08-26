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
