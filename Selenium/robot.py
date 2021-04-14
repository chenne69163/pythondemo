# -*- coding: utf-8 -*-

import os,sys
import time
import requests
import json
import tkinter

def send_to_lark(cluster):
    with open(check_cluster_txt, 'r') as f:
        a = f.readlines()
        q = "".join(a)
    data = {
        'title' : cluster,
        'text': q
    }

    headers = {'Content-Type': 'application/json'}
    url = 'https://open.feishu.cn/open-apis/bot/hook/996f08f1-da5f-4b24-8b52-10ccdcf04cba'
    response = requests.post(url=url, headers=headers, data=json.dumps(data))
    # print(response.text)

def main():
    url = 'https://open.feishu.cn/open-apis/bot/hook/996f08f1-da5f-4b24-8b52-10ccdcf04cba'
    top1 = tkinter.Tk()
    top1.title('功能选择')
    top1.geometry('400x200')
    top1.wm_attributes('-topmost', 1)

    panel1 = tkinter.Frame(top1)
    button1 = tkinter.Button(panel1, text='接口测试', command=api_test)
    button1.pack(side='left',fill='x', expand=True)
    button2 = tkinter.Button(panel1, text='退出', command=quit)
    button2.pack(side='right',fill='x', expand=True)
    button3 = tkinter.Button(panel1, text='作者', command=show_about)
    button3.pack(side='right',fill='x', expand=True)
    button4 = tkinter.Button(panel1, text='数据库', command=mysql_client)
    button4.pack(side='left',fill='x', expand=True)
    panel1.pack(side='bottom',fill='x', expand=True)

    top1.mainloop()

if __name__ == '__main__':
	main()
