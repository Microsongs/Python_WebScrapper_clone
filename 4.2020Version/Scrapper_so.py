import requests
from bs4 import BeautifulSoup

# 마지막 페이지를 가져오는 함수
def get_last_page(url):
    result = requests.get(url)
    # soup -> html을 가져오는 라이브러리
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div",{"class":"s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)

# 페이지의 job들의 상세 정보를 가져오는 함수
def extract_job(html):
    # div->title에서 변경됨
    title = html.find("h2",{"class":"fc-black-800"}).find("a")["title"]
    # 다음과 같이 사용하면 첫번째 span요소 -> company, 2번째 span 요소 -> locatino에 들어감
    # recursive=False는 더 깊게 들어가지 않게 해줌
    company, location = html.find("h3",{
        "class":"fc-black-700"
        }).find_all("span", recursive=False)
    company = company.get_text(strip=True).strip("\n")
    location = location.get_text(strip=True).strip("-").strip("\r").strip("\n")
    job_id = html['data-jobid']

    return {
        'title' : title,
        'company' : company,
        'location' : location,
        "apply_link" : f"https://stackoverflow.com/jobs/{job_id}"
        }

# 페이지의 job들을 가져오는 함수
def extract_jobs(last_page, url):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping StackOverflow: Page {page}")
        result = requests.get(f"{url}&pg={page+1}")
        soup = BeautifulSoup(result.text,"html.parser")
        results = soup.find_all("div",{"class":"-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

# jobs를 가져오는 함수
def get_jobs(word):
    url = f"https://stackoverflow.com/jobs?q={word}"
    last_page = get_last_page(url)
    jobs = extract_jobs(last_page, url)
    return jobs