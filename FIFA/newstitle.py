import requests
import csv
from pyquery import PyQuery as pq
import sys


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

def save_to_csv(file_name, items):
    with open(file_name, "a", newline='', encoding='gb18030') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(items)

def parse_news(year, html):
    doc = pq(html)
    if 2014 <= year <= 2019:
        aes = doc('#frameContent ul li span.first a').items() # 2014-2019
    elif 2011 <= year <= 2013:
        aes = doc('#newbiao_la ul li a').items() # 2013-211
    for a in aes:
        title = code_transfer(a.text())
        url = a.attr('href')
        # print(title, url)
        yield title, url

def main(url, year):
    file_name = f'{sys.path[0]}\\fifa{year}title.csv'
    print(file_name)
    html = html_download(url)
    items = parse_news(year, html)
    for item in items:
        print(f'正在写 {item[0]} title')
        save_to_csv(file_name, item)

if __name__ == "__main__":
    url = 'http://www.ali213.net/zt/fifa11/news/'
    year = 2011
    main(url, year)
'''
'#frameContent > ul:nth-child(1) > li:nth-child(1) > span.first > a' 游侠游戏资讯title pes2014-2019
#newbiao_la > ul > li:nth-child(1) > a 游侠游戏资讯title pes2013-2011
http://www.ali213.net/zt/pes2018/news/ pes2018资讯页
#newbiao_la > ul > li:nth-child(76) > a
'''
