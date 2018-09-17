from greetings import Greetings

class NorwegianGreetings(Greetings):
    def __init__(self,name):
        super().__init__(name)

    def morning_greeting(self):
        return 'God morgen!'

    def self_introducing(self):
        return \
            'Hei!\n' + \
            'Jeg heter ' + self.name + '.\n' + \
            'Hyggelig å se deg!'
