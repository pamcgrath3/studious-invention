from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bsoup
import smtplib

def main():
    with open("links.txt", "r") as file:
        lines = file.readlines()
        print("Scraping " + str(len(lines)) + " items from links.txt:\n")
        for link in lines:
            check(link)
        email = input("\nRecipient email: ")
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login("studiousinvention@gmail.com", "viesujixdvqczoja")
        with open("draft.txt", "r", encoding = "utf-8") as draft:
            body = draft.read()
            subject = "Report for " + str(len(lines)) + " links"
            full = f"Subject: {subject}\n\n{body}"
            s.sendmail("studiousinvention@gmail.com", email, full.encode("utf-8"))
            print("Email has been sent.")
            s.quit()
  
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

    with open("draft.txt", "a", encoding="utf-8") as draft:
            draft.write(link)
            draft.write(title + "\n")
            draft.write("Current price: " + price + "\n\n")
