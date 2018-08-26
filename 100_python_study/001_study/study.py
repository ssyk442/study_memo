# Sigur Rósの人数当てクイズ
input_count = input("Sigur Rósのメンバーは何人？：")
count = int(input_count)

if count == 3:
    print('あたり！')

elif count == 4:
    print('そんな時代もありました')

else:
    print('はずれー')
