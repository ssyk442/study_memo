import re

class SearchMobileNumber:
    def __init__(self,text):
        self.text = text

    def is_mobile_number(self):
        if not self.text:
            return 'nothing to search'

        # re.compile()に正規表現を渡し、Regexオブジェクトを生成
        mobile_number_regex = \
         re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')

        # Regexオブジェクト内に上記正規表現のパターンがないか検索する。
        # ある場合は、Matchオブジェクトに合致した部分を返す。
        match_object = \
         mobile_number_regex.search(self.text)

        if match_object:
            # Matchオブジェクトのgroup()メソッドでマッチしたテキストを返す。
            # 但し、この場合、一つ目の番号しかヒットしない。
            return 'mobile number: ' + match_object.group()
        else:
            return 'no mobile number included'
