from greetings import Greetings

# 印欧語族だらけのヨーロッパにポツンとある系統不明な言語です！
# 能格と絶対格の表現を組めれば面白いかも。
class BasqueGreetings(Greetings):
    def __init__(self,name):
        super().__init__(name)

    def self_introducing(self):
        return \
            'Kaixo!\n' + \
            'Nire izena ' + self.name + ' da.\n' + \
            'Urte askotarako!'
