import csv
import os
from os import mkdir
from random import shuffle
import sys

import requests

def code_transfer(string):
    replaces = ['\\','/','*','?','>','?',':','"','|','<']
    for i in replaces:
        if i == '?':
            string = string.replace(i, '？')
        elif i == '<':
            string = string.replace(i, '《')
        elif i == '>':
            string = string.replace(i, '》')
        elif i == ':':
            string = string.replace(i, '：')
        elif i == '"':
            string = string.replace(i, '“')
        else:
            string = string.replace(i, '')
    return string


def gbk_cannot(string):
    replaces = ['\xa0', '游侠网', '游侠']
    for i in replaces:
        string = string.replace(i, '')
    return string


def html_download(picurl):
    headers = {'User-Agent': "User-Agent:Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"}
    # request = Request(url, headers=headers)
    try:
        res = requests.get(picurl, headers=headers)
    except:
        pass
    else:
        return res.content


def main(year):
    file_content = f'{sys.path[0]}\\fifa{year}content.csv'
    write_path = f'{sys.path[0]}\\fifa{year}'
    if not os.path.exists(write_path):
        mkdir(write_path)
    with open(file_content, 'r', encoding='gb18030') as csvfile:
        reader = csv.reader(csvfile)
        while True:
            try:
                for row in reader:
                    title = code_transfer(row[0])
                    title_path = f'{write_path}\\{title}.txt'
                    if not os.path.exists(write_path):
                        continue
                    content = []
                    l = row[1][1:-1].split(',')
                    num = 0
                    for p in l:
                        if len(p) < 5:
                            continue
                        num += 1
                        if '支持键盘“← →”键翻页' in p or '责任编辑' in p:
                            continue
                        if num < 2:
                            content.append(gbk_cannot(p[1:-1]))
                        else:
                            content.append(gbk_cannot(p[2:-1]))
                    content = '\n\n'.join(content)
                    with open(title_path, 'w', encoding='utf-8') as f1:
                        f1.write(content)
                break
            except Exception as e:
                print(e)
