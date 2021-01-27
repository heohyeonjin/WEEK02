# ---------------------------------
# 파이썬 모듈 사용하기
# ---------------------------------
# 모듈 로딩하기 ---------------------
import math as m
# 모듈 사용 ==> 모듈명.xxx, 모듈명.함수()
print(f"math.pi      => {m.pi}")
print(f"math.pow()   => {m.pow(2,3)}")

from math import factorial,pow
#모듈에서 특정함수, 변수, 클래스만 가지고 온 경우
print(f"factorial(3) => {factorial(3)}")
print(f"pow(2,3) = > {pow(2,3)}")

import ex_01
import basic.ex_func
import ex_03 as eex
# from 패키지명.모듈명 import 변수명
import urllib.request as req
from urllib.request import urlretrieve
