import os

print(os.path.abspath('.'))
print(os.path.abspath('Scripts'))

# 引数が絶対パスなら True、相対パスなら False
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))
