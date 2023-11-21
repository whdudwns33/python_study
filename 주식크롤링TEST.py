from bs4 import BeautifulSoup
import requests

url = "https://finance.naver.com/"
res = requests.get(url)
bs_obj = BeautifulSoup(res.text, "html.parser")
topItem = bs_obj.find("tbody", {"id" : "_topItems1"})
print(topItem)


