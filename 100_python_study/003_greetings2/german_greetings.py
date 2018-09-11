from greetings import Greetings

class GermanGreetings(Greetings):
    def __init__(self,name):
        super().__init__(name)

    def morning_greeting(self):
        return 'Guten Morgen!'

    def evening_greeting(self):
        return 'Guten Abent!'

    def appreciate_someone(self):
        return 'Danke schön!'

    def self_introducing(self):
        return \
            'Hallo!\n' + \
            'Mein Name ist ' + self.name + '.\n' + \
            'Freut mich!'
