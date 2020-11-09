from flask import Flask, render_template, request, redirect
from Scrapper_so import get_jobs
import socket

# ip체크를 위한 함수
def ipcheck():
    return socket.gethostbyname(socket.getfqdn())

app = Flask("SuperScrapper")

# /는 웹사이트 root를 의미한다. -> /로 접속 요청을 하면 파이썬 함수를 실행할 것
@app.route("/")
def home():
    return render_template("potato.html")

# potato.html에서 넘어오는 report 데이터를 처리
@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        jobs = get_jobs(word)
        print(jobs)
    else:
        redirect("/")

    return render_template("report.html", searchingBy=word)

# @는 데코레이터 -> 바로 아래에 있는 함수를 찾는데, 그 함수를 decorate(꾸밈)을 해준다.
# <>꺽쇠 부분은 placeHolder이라 하며, 이 경우 인자를 사용해야 한다.
#@app.route("/<username>")
#def potato(username):
#    return f"Hello, your name is {username} how are you doing?"

# 
app.run(host=ipcheck())

