import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('http://www.scotturb.com/carreiras/horarios/').read()
soup = bs.BeautifulSoup(sauce,'lxml')

print(soup.title)

