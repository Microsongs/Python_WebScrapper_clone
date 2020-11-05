# 파이썬에 요청을 모아둔 것 -> request
# 패키지에서 정보를 뺴오기 좋은 것 -> beautifulsoappi
import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={LIMIT}"

def get_last_pages():
    # url을 get해옴
    result = requests.get(URL)
    # 링크의 text를 html로 파싱
    soup = BeautifulSoup(result.text, 
    'html.parser')
    # div에 클래스명이 pagination인 것을 찾는다
    pagination = soup.find("div",{"class":"pagination"})

    # a태그를 전부 찾는다.
    links = pagination.find_all('a')
    # a태그 내의 span을 전부 출력
    pages = []
    for link in links[:-1]:
        pages.append(link.find("span").string)
    # spans의 맨 마지막꺼를 뺴준다.
    max_page = pages[-1]

    return max_page

# 각 요소의 제목과 회사명을 찾고 반환
def extract_job(html):
    title = html.find("h2",{"class":"title"}).find("a")["title"]
    # company중에 link가 없는 것도 있다. -> if else 사용
    company = html.find("span",{"class":"company"})
    company_anchor = company.find("a")
    if company:
        if company_anchor is not None:
            company = str(company_anchor.string)
        else:
            company = str(company.string)
        # strip으로 빈칸 제거
        company = company.strip()
    else:
        company = None
    #location : 회사의 장소
    #location = html.find("span",{"class":"location"}).string
    location = html.find("div",{"class":"recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]   
    return {
        'title':title, 
        'company':company, 
        'location':location, 
        'link': f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit=50&vjk={job_id}"
    }

# 최대 페이지를 받아 받은만큼 reqeust하는 함수
def extract_get_jobs(last_page):
    jobs = []
    for page in range(int(last_page)):
        print(f"Scrapping Indeed page: Page: {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text,"html.parser")
        results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
            # job을 jobs 안에 삽입
    return jobs

def get_jobs():
    last_page = get_last_pages()
    jobs = extract_get_jobs(last_page)
    return jobs