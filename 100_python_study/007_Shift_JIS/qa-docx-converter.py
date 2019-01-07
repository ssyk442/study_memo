# Python3
# coding: shift_jis
import configparser
import csv
import docx
import os
from datetime import datetime

# ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
# 注：shift_jis環境で使用する場合は、
# 1.coding: shift_jisとすること！！
# 2.バックスラッシュ(使用不可)を\に置換すること！！
# 3.config.iniをencoding = shift_jisとすること！！
# ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
# パラメータ設定(config.iniより取得)
config = configparser.ConfigParser()

try:
    # configのファイルを開く
    config.read('./config/config.ini')
    # セクションを取得
    encoding_section = config['ENCODING']
    file_section = config['FILE_NAME']
    index_section = config['COLUMN_INDEX']

    # パラメータの読み込み
    # エンコード
    ENCODING = encoding_section.get('encoding')

    # 各ファイル名
    CSV_FILE_NAME = file_section.get('csv_file')
    DOCX_FILE_NAME = file_section.get('docx_file')

    # CSVから取り出したい文字列の列インデックス(0～)
    TITLE_COLUMN_INDEX = int(index_section.get('title_column'))
    QUESTION_COLUMN_INDEX = int(index_section.get('question_column'))
    FIRST_ANSWER_COLUMN_INDEX = int(index_section.get('first_answer_column'))
    LAST_ANSWER_COLUMN_INDEX = int(index_section.get('last_answer_column'))

# iniファイルオープン、セクション取得に失敗した場合
# ※パラメータ読み込みチェックは実装していません。
except:
    print("config.iniが存在しないか、config.ini内のパラメータが不正です。")
    exit()

# --------------------------------------------------------
# Wordに転記する「最終回答」を対象行より取得するメソッド
def get_last_answer(row):
    # 回答列を1列のみパラメータ指定している場合、その回答を「最終回答」とする
    if FIRST_ANSWER_COLUMN_INDEX == LAST_ANSWER_COLUMN_INDEX:
        return row[FIRST_ANSWER_COLUMN_INDEX]

    # 回答を後ろから初回回答へ検索し、最初にヒットした回答を「最終回答」とする
    for i in range(LAST_ANSWER_COLUMN_INDEX, FIRST_ANSWER_COLUMN_INDEX - 1, -1):
        if row[i] != "":
            return row[i]

    # 仮に全ての回答が空白だった場合、空白を返す
    return ""

# --------------------------------------------------------
# csvフォルダにあるCSVファイルオープン
csv_path = "./csv/" + CSV_FILE_NAME
if not os.path.isfile(csv_path):
    print("csvフォルダに"+CSV_FILE_NAME+"が存在しません。")
    exit()

csv_file = \
    open(csv_path, "r", encoding=ENCODING, errors="", newline="" )

# Wordファイル新規作成
doc = docx.Document()

# CSVファイル読み込み
csv_rows = \
    csv.reader(csv_file, delimiter=",", doublequote=True, \
    lineterminator="\r\n", quotechar='"', skipinitialspace=True)

# 2行目以降をWordファイルに転記
for row in csv_rows:
    # 1行目のヘッダは読み飛ばし
    if csv_rows.line_num == 1:
        continue
    # 見出し
    doc.add_heading(row[TITLE_COLUMN_INDEX], 0)
    # 質問
    doc.add_heading("質問", 1)
    doc.add_paragraph(row[QUESTION_COLUMN_INDEX])
    doc.add_paragraph('\n')
    # 回答(最終回答のみをセットする)
    doc.add_heading("回答", 1)
    doc.add_paragraph(get_last_answer(row))
    # 改ページ
    doc.add_page_break()

# Wordファイルの新規作成or上書き
docx_path = "./docx/"+DOCX_FILE_NAME
if os.path.isfile(docx_path):
    choice = input("同名ファイルが既に存在します。リネームして退避しますか？\
        \nはい → y(=n以外) いいえ → n：")
    # 同名ファイルをリネームして退避
    if choice != "n":
        current_date = datetime.now().strftime('%y%m%d%H%M%S')
        os.rename(docx_path, str.rstrip(docx_path, ".docx") + current_date + ".docx")

# Wordファイルをdocxフォルダに保存
doc.save(docx_path)
print(DOCX_FILE_NAME+"を作成しました。")
