import requests
r = requests.get('https://search.jd.com/Search?keyword=%E9%85%B1%E6%B2%B9&enc=utf-8&suggest=1.rem.0.T15&wq=%E9%85%B1%E6%B2%B9&pvid=mgz20vvi.6tl9aw')
r = r.content
print  r
from bs4 import BeautifulSoup
soup = BeautifulSoup(r,'html.parser')
body = soup.body
data = body.find('div',attrs={'id':'J_container'})
mlist = data.find('div',attrs={'class':'m-list'})
clearfix = mlist.find('ul',attrs={'class':'gl-warp clearfix'})
for li in clearfix.find_all('li'):
    target = li.find('div',attrs={'class':'p-name p-name-type-2'})
    names = target.a['title']
    print names	