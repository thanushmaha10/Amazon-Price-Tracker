import requests
from bs4 import BeautifulSoup
import smtplib
MY_EMAIL = "testmailpyth01@gmail.com"
PASSWORD = "qwpjlcmnjyxuaaxz"

headers = {
    "User-Agent": "https://www.amazon.com/dp/B075CYMYK6?"
                  "ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1",
    "Accept-Language": "text/html,application/xhtml+xml,application/xml;"
                       "q=0.9,image/avif,image/webp,image/apng,*/*;"
                       "q=0.8,application/signed-exchange;v=b3;q=0.7"
}

response = requests.get(url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1",
                        headers=headers)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
price_class = soup.find(name="span", class_="a-price-whole").get_text()
price = int(price_class.split(".")[0])
product_selector = soup.select("div h1 span")[0]
product = product_selector.get_text()
# print(price)
# print(product)

if price < 100:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="thanushmaha10@gmail.com",
                            msg=f"Subject: PRICE DROP FROM AMAZON\n\n "
                                f"{product}\n\n price dropped under $ 100\n\n New price is ${price}".encode('utf-8')
                            )
