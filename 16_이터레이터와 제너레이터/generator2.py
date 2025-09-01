# generator2.py

import time

def longtime_job():
    print("job start")
    time.sleep(1)
    return "done"
# list_job = [longtime_job() for i in range(5)] # 리스트 
list_job = (longtime_job() for i in range(100)) #제너레이터 표현식
print(next(list_job))