#-*- coding:utf-8 -*-
import csv

def save_to_file(jobs):
    # open -> 파일을 열어주며, 없을 경우 파일을 생성
    # mode는 write/read 등을 설정
    file = open("jobs.csv", mode="wt", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        # 딕셔너리는 값만 불러올 수 있다 -> values
        writer.writerow(job.values())
    return