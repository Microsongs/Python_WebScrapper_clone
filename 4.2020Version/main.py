from flask import Flask, render_template, request, redirect, send_file
from Scrapper_so import get_jobs
from scrapper_indeed import get_jobs_indeed
from exporter import save_to_file
import socket

# ip체크를 위한 함수
def ipcheck():
    return socket.gethostbyname(socket.getfqdn())

app = Flask("SuperScrapper")

# db를 route 밖에 두어야 얼마나 실행되든 관계없이 상관이 없다. route 내에 있으면 report 실행 시마다 초기화됨
db = {}

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
        # db에 데이터가 있으면 다시 불러올 필요 x
        existingJobs= db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_jobs_indeed(word) + get_jobs(word)
            db[word] = jobs
    else:
        redirect("/")

    return render_template(
        "report.html",
        searchingBy=word, 
        resultsNumber=len(jobs),
        jobs = jobs
    )

# export 라우트
@app.route('/export')
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv", as_attachment=True)
    except:
        return redirect("/")
        

# @는 데코레이터 -> 바로 아래에 있는 함수를 찾는데, 그 함수를 decorate(꾸밈)을 해준다.
# <>꺽쇠 부분은 placeHolder이라 하며, 이 경우 인자를 사용해야 한다.
#@app.route("/<username>")
#def potato(username):
#    return f"Hello, your name is {username} how are you doing?"

# 
app.run(host=ipcheck())

