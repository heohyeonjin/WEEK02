# ------------------------------------
# 파이썬 함수
# ------------------------------------

# 함수 생성 방법 (1) -------------------
# 기  능 : 두개의 정수 더하기
# 함수명 : add
# 재  료 : num1, num2
# 반환값 : 더한 결과
# -------------------------------------
def add(num1,num2):
    result = num1+num2
    return result

# 함수 사용 => 함수 호출 함수명(재료)
value = add(10,20)
print(f"10+20 = {value}")

# 함수 생성 방법 (2) -------------------
# 기  능 : 0개~여러개 정수를 입력받아 더한 후 결과 반환
# 함수명 : getSum
# 재  료 : 0~ 여러개 정수 => 가변인자
# 반환값 : 더한 결과
# -------------------------------------
def getSum(*data):
    result = 0
    for num in data:
        result +=num
    return result
#인자 갯수 상관 없음
print(f"getSum(1,3,5,7,9) : {getSum(1,3,5,7,9)}")
print(f"getSum(1,3) : {getSum(1,3)}")
print(f"getSum() : {getSum()}")

data = list(range(1,101))  # 1~100가지 데이터 저장 리스트
print(f"data=> {data}")
print(f"getSum(): {getSum(*data)}")

def getMaxMin(*data):
    _max = max(data)
    _min = min(data)
    return _max,_min
#함수 여러개 반환 시 튜플로 반환
_max, _min = getMaxMin(1,2,3,4,5,6)  # 언패킹하여 받기
print(f"max : {_max}, min :{_min}")
maxmin = getMaxMin(1,2,3,4,5,6)      # 패킹하여 받기
print(f"maxmin : {maxmin}")

# 함수 생성 방법 (3) -------------------
# 기  능 : 키와 값의 형태로 가변데이터 처리
# 함수명 : setIdPw
# 재  료 : 키와 값 형태의 => 가변인자
# 반환값 : 없음
# -------------------------------------
def setIdPw(**idpw):
    print(idpw,type(idpw))
#딕셔너리 형태로 반환
setIdPw(id = "123", id2 = "aaa")   #키, 값형태

#람다 : 이름없는 한줄 함수, 익명함수

