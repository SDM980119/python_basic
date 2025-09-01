# decorator2.py

import time

def elapesd(func): # 경과시간
    def wrapper():
        start=time.time()
        result = func()
        end = time.time()
        print(f"함수 수행시간: {end-start}초")
        return result
    return wrapper

@elapesd
def myfunc():
    print('함수가 실행됩니다.')
myfunc()