import random

#读取文件列表
def readlist():
    f = open('NameList/namelist.conf', 'r', encoding='utf-8')
    read = f.readlines()
    s = {}
    for i in read:
        s[i.split("=")[0]] = i.split("=")[1].strip()
    return s

#抽取下一个学生
def nextname():
    namelist=readlist()
    randoms = random.randint(1,len(namelist))
    return str(randoms)+"号 "+str(namelist[str(randoms)])+"同学"
