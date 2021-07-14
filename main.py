import requests
import bs4

header = {
    ' User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/91.0.4472.124 Safari/537.36 '
}

url = 'https://store.steampowered.com/'

r = requests.get(url, header)

soup = bs4.BeautifulSoup(r.text, "html.parser")
steam = soup.findAll('div', attrs={'class':'tab_item_content'})
for steams in steam:
  print( steams.find('div',attrs={'class':'tab_item_name'}).text)
