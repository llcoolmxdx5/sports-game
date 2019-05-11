import csv
import multiprocessing
import threading

import requests
from pyquery import PyQuery as pq

file_write = r'D:\chengxv - 副本\后端\python\crawl\游侠\yxcontent.csv'
file_read = r'D:\chengxv - 副本\后端\python\crawl\游侠\yxtitle.1.csv'

def html_download(url):
    headers = {'User-Agent': "User-Agent:Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"}
    # request = Request(url, headers=headers)
    try:
        html = requests.get(url, headers=headers)
        html.encoding = 'gb2312'
    except:
        pass
    return html.text

def code_transfer(string):
    replaces = ['"', '：', ' ', ' ', ':', '/', '<', '>', '?', '“', '”', '|', '*']
    for i in replaces:
        string = ''.join(string.split(i))
    return string

def save_to_csv(items):
    with open(file_write, "a", newline='', encoding='gb18030') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(items)
    
def parse_news(html, url):
    doc = pq(html)
    title = doc('title').text()[:-15]
    content_p = [] #用来保存文章段落
    # 2018-2013
    ps = doc('#Content p').items()
    for p in ps:
        content_p.append(p.text())
    img_urls = [] # 用来保存图片链接
    imgs = doc('#Content p img').items()
    for img in imgs:
        img_urls.append(img.attr('src'))
    return title, content_p, img_urls, url

def main(url):
    html = html_download(url)
    items = parse_news(html, url)
    save_to_csv(items)

if __name__ == "__main__":
    with open(file_read, 'r', encoding='gb18030') as csvfile:
        reder = csv.reader(csvfile)
        L = []
        for row in reder:
            L.append(row[1])
    pool = multiprocessing.Pool()
    # 多进程
    thread = threading.Thread(target=pool.map, args = (main,[x for x in L]))
    thread.start()
    thread.join()
        
'''
total_page = doc('#Content  div.page_fenye  span:last a').text() 2011-2013
gb2312
'''
