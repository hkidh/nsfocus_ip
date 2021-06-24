
# read_file
data = []                       # 開一個空清單
with open('tp.txt', 'r') as f:  # 開啟檔案,讀進檔案 tp.txt
    for line in f:              # 在檔案中每一行一行
        data.append(line.strip()) # 把每行去除換行符號,一行行加入data清單中
print('Policy 共有' + str(len(data)) + '行資料' + '\n') # 計算data有多少行的資料,將 int 改為 str
print('-' * 90)
#print('Policy 名稱如下: ')

# write_file
with open('tp_t.csv', 'w') as f: # 開啟檔案,寫入檔案tp.csv 
    for line in data:
        if line == '!':         # 有!的行,跳過
            continue
        if len(line) != 0:      # 在行有字元
            if '-group_ip' in line: # 有'protect zone'字的行
                    f.write(line + '\n') # 寫進f檔

# sort_and_policy_name_list
# csv = []
# one = []
# with open('tp_t.csv', 'r') as f:
#     for line in f:
#         csv.append(line.split(' '))
# #    print('csv: ', csv[0])
#     for line in csv:
#         one.append(line[2])
# #    print('-' * 100)
# #    print('one:', one[0])
#     x = sorted(set(one)) #去除重複值+排序
#     for line in x:
#         print(line)


# filter_Policy_and_list
x = []
while True:
    with open('tp_t.csv', 'r') as f:
        print('-' * 90)
        print('--輸入  ''q''  退出--')
        print('')
        gn = input('請輸入 IP: ')
        if gn == 'q':
            break
        if gn == '':
            break
        for line in f:
            if gn in line:
                x = line.split(' ')
                print('')
  #              print(gn)
                print('所在的 group_name 為 :', x[2])
  #             print('')