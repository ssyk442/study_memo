class Greetings:
    # 性別
    GENDER_MALE = "0"
    GENDER_FEMALE = "1"

    # __init__メソッドはインスタンス化直後に必ず呼ばれる
    def __init__(self,name):
        self.name = name

    def self_introducing(self):
        return "★★ Sorry! I'm not ready to answer your request. ★★"
