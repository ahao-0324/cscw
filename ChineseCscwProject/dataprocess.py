import os

data_dir = r'C:\Users\ljh\Desktop\-\cscw数据竞赛\SCHOLAT Interactive User Recommendation\user_attribute'

data_document_name = os.listdir(data_dir)
res = []
for name in data_document_name[:5]:
    datapath = data_dir + '\\' + name

    with open(datapath, 'r', encoding="utf_8") as f:
        data = f.readline()
        data.rstrip('')
        li = data.split(' ')
        print(li)
