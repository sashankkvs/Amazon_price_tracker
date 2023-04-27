import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.in/Inalsa-Air-Fryer-Nutri-Fry/dp/B09KLJ7HMV/ref=sr_1_14?crid=BU5UCVQ81JKH&th=1"
response = requests.get(url=url,headers={
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
    "Accept-Language" : "en-US,en;q=0.5"
})
response_html = response.text
soup = BeautifulSoup(response_html,"lxml")
price = soup.find(name="span", class_="a-offscreen")
price_amazon = int(price.get_text().split("₹")[1].split(".00")[0].replace(',',''))
# print(int(price_amazon.split(".00")[0].replace(',','')))
print(price_amazon)
if price_amazon < 4000:
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login("ksashank129@gmail.com", password="eomccuyhkjlqrtvk")
        connection.sendmail(from_addr="ksashank129@gmail.com",to_addrs="ksashank129@yahoo.com",msg="Subject:Price change\n\nThe product price reduced to 4000")
