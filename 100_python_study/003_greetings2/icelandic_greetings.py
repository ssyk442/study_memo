from greetings import Greetings

class IcelandicGreetings(Greetings):
    def __init__(self, name, others_gender_id):
        super().__init__(name)
        self.others_gender_id = others_gender_id

    def self_introducing(self):
        common_expression = \
            'Hæ!\n' + \
            'Ég heiti ' + self.name + '.\n'

        # 話す相手の性別によって表現が異なる
        if self.others_gender_id == super().GENDER_MALE:
            return common_expression + 'Komdu sæll!'
        else:
            return common_expression + 'Komdu sæl!'
