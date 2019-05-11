from newstitle import main as titlemain
from newsconttent import main as contentmain
from save import main as savemain

url = 'http://www.ali213.net/zt/fifa19/news/'
year = 2019

if __name__ == "__main__":
    titlemain(url,year)
    contentmain(year)
    savemain(year)