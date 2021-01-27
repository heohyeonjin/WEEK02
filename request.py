# 이미지 파일 다운로드 하기
import urllib.request
import os.path

#URL, 파일 경로 선언
url = "http://uta.pw/shodou/img/28/214.png"
DIR = "../Image/"
SAVENAME = "test.png"

# 저장 폴더 체크 후 생성
#if not os.path.exits(DIR) : os.mkdir(DIR)

# 파일 형태로 다운로드
filename, header = urllib.request.urlretrieve(url, SAVENAME)
print(f"filename : {filename}\n header : {header}")
print("저장되었습니다...!")

#-------------------------파이썬으로 파일 저장

url = "http://uta.pw/shodou/img/28/214.png"
SAVENAME = "test1.png"

men = urllib.request.urlopen(url)
header = men.getheaders()
data = men.read()
#print(data)

#바이너리 모드로 파일 저장 / 그림으로 저장
with open(SAVENAME, mode='wb' ) as f:
    f.write(data)
    print("저장되었습니다...!")

 # 바이트 데이터 읽기
print('type(data) = ', type(data))
print(data)

text = data.decode("utf-8")
print(text)

##########
google_url = "https://www.google.co.kr/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
savename = "google.png"
res = urllib.request.urlopen(google_url)
data = res.read()
with open(savename, mode='wb' ) as f:
    f.write(data)
    print("저장되었습니다...!")