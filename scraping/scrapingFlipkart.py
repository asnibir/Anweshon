from bs4 import BeautifulSoup
import requests
from .models import Product
from .utils import *

def getUrl(searchKey):
    url = "https://www.flipkart.com/"
    searchKey = searchKey.replace(" ", "+")
    url = url + "search?q=" + searchKey
    return url


def scrapingFlip(searchKey):
    html_text = requests.get(
        getUrl(searchKey=searchKey
        ),
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
        },
    ).text
    soup = BeautifulSoup(html_text, "lxml")
    # product name
    name = soup.find("div", class_="_4rR01T").text
    print(name)

    # product price
    price = soup.find("div", class_ = "_30jeq3").text
    print(price)
    #  _16Jk6d
    # rating
    ratings = soup.find("div", class_="_3LWZlK").text
    print(ratings)

    # image url
    divi = soup.find("div", class_="CXW8mj")
    img_src = divi.img["src"]
    print(img_src)

    # Page Link
    page_url = getUrl(searchKey=searchKey)
    print(f"Page url: {page_url}")

    return Product(
        name = name,
        url = page_url,
        image_url = img_src,
        website_name = WEBSITE_FLIPKART,
        price = price,
        rating = ratings
    )
