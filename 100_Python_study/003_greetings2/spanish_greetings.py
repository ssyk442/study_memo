from greetings import Greetings

class SpanishGreetings(Greetings):
    def __init__(self, name, my_gender_id):
        super().__init__(name)
        self.my_gender_id = my_gender_id

    def self_introducing(self):
        common_expression = \
            '¡Hola!\n' + \
            'Me llamo ' + self.name + '.\n'

        # 自分の性別によって表現が異なる
        if self.my_gender_id == super().GENDER_MALE:
            return common_expression + '¡Encantado!'
        else:
            return common_expression + '¡Encantada!'
