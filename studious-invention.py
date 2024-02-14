from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bsoup

def main():
    with open("links.txt", "r") as file:
        lines = file.readlines()
        print("Scraping " + str(len(lines)) + " items from links.txt:\n")
        for link in lines:
            check(link)
  
def check(link):
    request = Request(link, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'})
    webpage = urlopen(request).read().decode('utf-8')
    html = bsoup(webpage, "html.parser")

    title = str(html.find("span", class_ = "a-size-large product-title-word-break"))
    endIndex1 = title.find("       </span")
    title = title[78:endIndex1]
    print(title)

    price = str(html.find("span", class_ = "a-offscreen"))
    endIndex2 = price.find("</span>")
    price = price[26:endIndex2]    
    print("Current price: " + price + "\n")
