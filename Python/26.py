import requests
from bs4 import BeautifulSoup

url = input("url: ")
class_n= input("class_name: ")
class_img= input("class_img: ")

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("div", class_="cover_image")

for book in books:
    title = book.find("div", class_=class_n)
    
    img_tag = book.find("img")
    img_src = img_tag.get("src", "")
    
    img_link = "https://www.gutenberg.org" + img_src if img_src.startswith("/") else img_src
    
    print("Title:", title)
    print("Image:", img_link)
    print("-" * 40)


