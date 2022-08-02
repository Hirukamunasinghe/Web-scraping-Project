#Importing modules
import requests
from bs4 import BeautifulSoup
from smtplib import SMTP

#URL and headers
URL = "https://www.alibaba.com/product-detail/Bt-Speaker-5-0-Flame-Light_1600456546739.html?spm=a2700.galleryofferlist.topad_creative.d_title.2774253079PbGS"

headers={
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
}
MY_EMAIL ="munasinghehiruka@gmail.com"
PASSWORD ="Google Company"

response = requests.get(URL,headers=headers)
website_html = response.text

#Creating soup
soup = BeautifulSoup(website_html,"lxml")
# print(soup.prettify())

#Getting the Price of the product
heading = soup.find(name='span',class_="pre-inquiry-price").getText()
product_price = float(heading.split("$")[0])
print(product_price)

#Sending the email
if product_price<50:
    with SMTP('smtp.gmail.com',port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL,PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="BT Speaker is now available in Alibaba at below $50. BUY NOW!"
        )

#End of Program