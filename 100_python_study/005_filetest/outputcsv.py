import csv

# CSVファイルオープン
csv_file = open("./csvtest.csv", "r", encoding="utf_8", errors="", newline="" )

# CSVファイル読み込み
# 参考：https://qiita.com/motoki1990/items/0274d8bcf1a97fe4a869
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
header = next(f)
for row in f:
    #rowはList
    print(row[0]+"\n"+row[1]+"\n"+row[2])
