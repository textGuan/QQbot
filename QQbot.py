import os
import time
import threading
import csv
import cv2
import win32gui
import win32con
import win32clipboard as wc

import baidu_ocr

msg = "[自动发送，无需回复]不好意思打扰了，记得明天打卡健康每日报/cy"
qq = []
hwnd_title = []
temp_hwnd = []
people_list1 = []
people_list = []
class_list = []

def get_people():#compare and find the peoples
    global people_list1
    global qq
    str_return = ''
    file_path = 'workspace/'
    filename = os.listdir(file_path)
    for i in filename:
        path = file_path+i
        img1 = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
        temp_list = baidu_ocr.run(img1)
        if temp_list[0] == "ERROR":
            return "ERROR"
        people_list1 = people_list1 + temp_list
    for i in people_list1:
        if i not in people_list:
            people_list.append(i)
    for i in people_list:
        for ii in range(len(class_list)):
            if i in class_list[ii][0]:
                qq.append(class_list[ii][1])
                str_return = str_return + class_list[ii][1]+'\n'
    return str_return
    pass

def search_people():#find the people's qq nums
    global qq
    uname = ''
    str_return = get_people()
    if str_return == "ERROR":
        return "ERROR"
    # qq = []
    # for i in class_list:
    #     qq.append(i[1])
    # qq = ['1157411076']
    for i in qq:
        send_to(i)
    return str_return
    pass

def send_to(qqnum):#send msg to specific people reco by qq num
    global hwnd_title
    hwnd_title = []
    uname = ''
    hwnd = win32gui.FindWindow('TXGuiFoundation','QQ')
    send_msg(qqnum)
    win32gui.SendMessage(hwnd,258,22,2080193)
    win32gui.SendMessage(hwnd,770,0,0)
    time.sleep(1)
    win32gui.SendMessage(hwnd,win32con.WM_KEYDOWN,win32con.VK_RETURN,0)
    win32gui.SendMessage(hwnd,win32con.WM_KEYUP,win32con.VK_RETURN,0)
    time.sleep(1)
    win32gui.EnumWindows(get_all_hwnd,0)
    for i in hwnd_title:
        if i is not "" and i not in temp_hwnd:
            uname = str(i)
    send_and_close(uname)
    pass

def send_msg(to_send):#send msg to some people
    wc.OpenClipboard()
    wc.EmptyClipboard()
    wc.SetClipboardData(win32con.CF_UNICODETEXT,to_send)
    wc.CloseClipboard()
    pass

def send_and_close(uname):
    hwnd = win32gui.FindWindow('TXGuiFoundation',uname)
    send_msg(msg)
    win32gui.SendMessage(hwnd,258,22,2080193)
    win32gui.SendMessage(hwnd,770,0,0)
    time.sleep(1)
    win32gui.SendMessage(hwnd,win32con.WM_KEYDOWN,win32con.VK_RETURN,0)
    win32gui.SendMessage(hwnd,win32con.WM_KEYUP,win32con.VK_RETURN,0)
    win32gui.SendMessage(hwnd,win32con.WM_CLOSE,0,0)

def get_all_hwnd(hwnd,mouse):#get all the windows
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.append(win32gui.GetWindowText(hwnd))

def find_qq():#detect if qq's launched correctly
    global hwnd_title
    win32gui.EnumWindows(get_all_hwnd,0)
    if "QQ" not in hwnd_title:
        # print("QQ_ERROR")
        return "QQ_ERROR"
    else:
        for i in hwnd_title:
            temp_hwnd.append(i)
        hwnd_title = []
        str_return = search_people()
        return str_return

def read_qq():
    global class_list
    csv_file = open(u'1.csv',encoding='utf-8-sig')
    csv_reader_line = csv.reader(csv_file)
    for i in csv_reader_line:
        class_list.append(i)
        
def run(message_input):
    global msg
    msg = str(message_input)
    read_qq()
    return find_qq()
    # print(qq)