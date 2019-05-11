import csv
import multiprocessing
import sys
import threading
from functools import partial

import chardet
import requests
from pyquery import PyQuery as pq


def html_download(url):
    headers = {'User-Agent': "User-Agent:Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"}
    # request = Request(url, headers=headers)
    try:
        html = requests.get(url, headers=headers)
        # encoding = chardet.detect(html)['encoding']
        encoding = 'utf-8'
        # if '2010' or '2011' or '2012' or '2013' in url:
        # encoding = 'gb2312'
        html.encoding = encoding
    except:
        pass
    return html.text


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


def save_to_csv(file_content, items):
    with open(file_content, "a", newline='', encoding='gb18030') as csvfile:
        writer = csv.writer(csvfile)
        print(f'正在写 {items[0]} content')
        writer.writerow(items)


def parse_news(html, url):
    doc = pq(html)
    title = doc('h1').text()
    content_p = [] #用来保存文章段落
    # 2018-2013
    ps = doc('#Content p').items()
    for p in ps:
        content_p.append(p.text())
    # img_urls = [] # 用来保存图片链接
    # imgs = doc('#Content p img').items()
    # for img in imgs:
    #     img_urls.append(img.attr('src'))
    # return title, content_p, img_urls, url
    return title, content_p, url


def start(url, file_content):
    html = html_download(url)
    items = parse_news(html, url)
    save_to_csv(file_content, items)


def main(year):
    file_title = f'{sys.path[0]}\\fifa{year}title.csv'
    file_content = f'{sys.path[0]}\\fifa{year}content.csv'
    with open(file_title, 'r', encoding='gb18030') as csvfile:
        reder = csv.reader(csvfile)
        urls = []
        for row in reder:
            urls.append(row[1])
    pool = multiprocessing.Pool()
    # 多进程
    thread = threading.Thread(target=pool.map, args = (partial(start, file_content=file_content), urls))
    thread.start()
    thread.join()

if __name__ == "__main__":
    main(2011)


'''
total_page = doc('#Content  div.page_fenye  span:last a').text() 2011-2013
gb2312
'''
