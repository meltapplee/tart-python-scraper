# tart-python-scraper

### 기능
- [프랩 칼럼 페이지](https://prap.kr/?cat=5) 에 존재하는 모든 칼럼을 스크래핑하여 DB에 저장합니다.
- identifier를 기반으로 데이터를 체크하여, 기존 데이터가 존재할 경우 최신 스크래핑 정보로 즉시 동기화합니다.

### 기술스택
- 언어: Python 3.9
- 프레임워크: Django 4.2.28
- 라이브러리:
  - BeautifulSoup4: HTML 파싱 및 데이터 추출
  - httpx: HTTP 클라이언트 (Timeout 및 연결 관리)
- 데이터베이스: PostgreSQL

### 실행 방법
1. **코드 받기 & 프로젝트 폴더로 이동**
```
git clone https://github.com/meltapplee/tart-python-scraper.git
cd tart-python-scraper
```
2. **가상환경 생성**(이미 가상환경을 사용 중이거나 시스템 전역에 패키지를 설치해도 무관한 경우 건너뛰어도 됩니다.)

   - Windows
      ```
      python -m venv venv
      .\venv\Scripts\activate
      ```
   - Mac / Linux
      ```
      python3 -m venv venv
      source venv/bin/activate
      ```
4. **필요한 라이브러리 설치**
```
pip install -r requirements.txt
```
5. **환경변수 설정**
- .env.example 파일을 복사하여 .env 파일을 생성하고, 본인의 DB 정보를 입력합니다.
- Django Secret Key 설정: 아래 명령어를 터미널에서 실행하여 생성된 키를 .env의 SECRET_KEY 항목에 붙여넣습니다.
```
python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
6. **데이터베이스 테이블 생성 및 실행**
```
# 데이터베이스 테이블 생성
python manage.py migrate

# 크롤러 실행 
python manage.py prap
```

### 관련 프로젝트
[tart-backend-api](https://github.com/meltapplee/tart-backend-api): 본 스크래퍼가 수집한 데이터를 DB에서 읽어와 페이징 및 정렬된 형태로 제공하는 Kotlin/Spring 기반 API 서버입니다.
