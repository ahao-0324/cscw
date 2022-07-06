import os
from pandas.core.frame import DataFrame


data_dir = r'.\user_attribute'


def dataProcess(data):
    return '0'


data_document_name = os.listdir(data_dir)
res = []
for name in data_document_name:
    datapath = data_dir + '\\' + name

    with open(datapath, 'r', encoding="utf_8") as f:
        data = f.readline()
        data = data.rstrip(' ')
        # data = dataProcess(data)
        li = data.split(' ')
        res.append(li)
d = DataFrame(res)
d.to_csv('data.csv')