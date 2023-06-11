import requests
from bs4 import BeautifulSoup  
url="https://www.codewithharry.com"

r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

#Tags
#NavigableString
#BeautifulSoup
#Comment

title=soup.title
print(title)

paras=soup.find_all('p')
anchors=soup.find_all('a')

# print(soup.find('p'))
# print(soup.find('p')['class'])
print(soup.find('p').get_text())

all_links=set()
for links in anchors:
    if (links !='#'):
        LinkText="https://codewithharry.com"+ links.get('href')
        all_links.add(links)
        print(LinkText)
