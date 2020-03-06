import os
def sc():
    path = os.getcwd()
    str1 = "rmdir /s/q "+str(path)+'\\temp'
    os.system(str1)
    # os.mkdir(path+'\\temp')
    str1 = "rmdir /s/q "+str(path)+'\\workspace'
    os.system(str1)
    # os.mkdir(path+'\\workspace')