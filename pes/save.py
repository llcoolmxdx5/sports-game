import csv
import requests
from random import shuffle
from os import mkdir
import os

read_filename = r'D:\chengxv - 副本\后端\python\crawl\游侠\yxcontent.csv'
write_filename = r'D:\chengxv - 副本\后端\python\crawl\游侠\pes' + '\\'

def code_transfer(string):
    replaces = ['"', '：', ' ', ' ', ':', '/', '<', '>', '?', '“', '”', '|', '*']
    for i in replaces:
        string = ''.join(string.split(i))
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

with open(read_filename, 'r', encoding='gb18030') as csvfile:
    reader = csv.reader(csvfile)
    while True:
        try:
            for row in reader:
                title = code_transfer(row[0])
                path = write_filename + title
                if os.path.exists(path):
                    continue
                mkdir(path)
                content = []
                l = row[1][1:-1].split(',')
                for p in l:
                    content.append(p[2:-4])
                shuffle(content)
                content = '\n\n'.join(content)
                with open(path + '\\' + title + '.txt', 'w') as f1:
                    f1.write(content)

                url = row[3]

                pic_L = row[2]
                if len(pic_L) > 2:
                    pic_s = pic_L[1:-1]
                    pic_L = pic_s.split(',')
                    i = 1
                    for pic_url in pic_L:
                        if i > 1:
                            content = html_download(pic_url[2:-1])
                        else:
                            content = html_download(pic_url[1:-1])
                        if not content:
                            continue
                        with open(path + '\\'+pic_url[-10:-1], 'wb') as f:
                            f.write(content)
                        i += 1

        except Exception as e:
            print(e)
        except:
            pass

