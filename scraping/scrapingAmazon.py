from bs4 import BeautifulSoup
from lxml import html
import requests
from .models import Product
from decimal import Decimal
from .utils import *
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

def getUrl(searchKey):
    url = "https://www.amazon.in/"
    searchKey = searchKey.replace(" ", "+")
    url = url + "/s?k=" + searchKey + "&ref=nb_sb_noss"
    return url

def scraping(searchKey):
    html_text = requests.get(getUrl(searchKey=searchKey), headers=header).text
    soup = BeautifulSoup(html_text, "lxml")

    # Product Name
    name = soup.find("span", class_="a-size-medium a-color-base a-text-normal").text
    print(name)

    # Product Price
    price = soup.find("span", class_="a-price-whole").text.strip()
    print(price)

    # Product Image
    img_div = soup.find("div", class_="a-section aok-relative s-image-fixed-height")
    img_src = img_div.img["src"]
    print(img_src)

    # Customer reviews
    rating_star = soup.find("span", class_="a-icon-alt").text
    rating_star = rating_star.split()[0]
    print(rating_star)
    # global_rating = soup.find("span", class_="a-size-base").text
    # print(f"Global ratings: {global_rating}")

    # Page Link
    page_url = getUrl(searchKey=searchKey)
    print(f"Page url: {page_url}")

    return Product(
        name = name,
        url = page_url,
        image_url = img_src,
        website_name = WEBSITE_AMAZON,
        price = price,
        rating = rating_star
    )
