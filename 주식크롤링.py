# server.py
from flask_cors import CORS
from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

# app = Flask(__name__)은 Flask 애플리케이션을 생성하는 코드입니다. 이 코드는 Flask 프레임워크에서 제공하는 Flask 클래스를 사용하여 웹 애플리케이션을 초기화합니다.
app = Flask(__name__)
CORS(app)

@app.route('/api/stock/price')
def get_stock_price():
    url = "https://finance.naver.com/item/main.naver?code=005930"
    # 지정된 URL로 HTTP GET 요청을 보내고 응답을 res 변수에 저장
    res = requests.get(url)
    # BeautifulSoup 객체 (bs_obj)를 생성하여 응답의 HTML 내용을 파싱합니다. "html.parser"는 BeautifulSoup이 제공하는 HTML 파서
    bs_obj = BeautifulSoup(res.text, "html.parser")
    # HTML에서 클래스가 "today"인 <div> 요소를 찾음
    div_today = bs_obj.find("div", {"class": "today"})
    em = div_today.find("em")
    price = em.find("span", {"class": "blind"}).text

    return jsonify({'price': price})

@app.route('/api/stock/oilInfo')
def get_stock_info():
    url = "https://finance.naver.com/"
    res = requests.get(url)
    bs_obj = BeautifulSoup(res.text, "html.parser")
    div_group = bs_obj.find("div", {"class" : "group1"})

if __name__ == '__main__':
    app.run(debug=True)
