import requests
import csv
from pyquery import PyQuery as pq

file_name = r'D:\chengxv - 副本\后端\python\crawl\游侠\yxtitle.csv'

def html_download(url):
    headers = {'User-Agent': "User-Agent:Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"}
    # request = Request(url, headers=headers)
    try:
        html = requests.get(url, headers=headers)
        html.encoding = 'utf-8'
    except:
        pass
    return html.text

def code_transfer(string):
    replaces = ['"', '：', ' ', ' ', ':', '/', '<', '>', '?', '“', '”', '|', '*']
    for i in replaces:
        string = ''.join(string.split(i))
    return string

def save_to_csv(items):
    with open(file_name, "a", newline='', encoding='gb18030') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(items)

def parse_news(html):
    doc = pq(html)
    # aes = doc('#frameContent ul li span.first a').items() 2014-2019
    aes = doc('#newbiao_la ul li a').items() # 2013-211
    for a in aes:
        title = code_transfer(a.text())
        url = a.attr('href')
        print(title, url)
        yield title, url

def main():
    url = 'http://www.ali213.net/zt/pes2011/news/'
    html = html_download(url)
    items = parse_news(html)
    for item in items:
        save_to_csv(item)

if __name__ == "__main__":
    main()
'''
'#frameContent > ul:nth-child(1) > li:nth-child(1) > span.first > a' 游侠游戏资讯title pes2014-2019
#newbiao_la > ul > li:nth-child(1) > a 游侠游戏资讯title pes2013-2011
http://www.ali213.net/zt/pes2018/news/ pes2018资讯页
'''
