# Python 3.8.0 Alpine 이미지를 가져옵니다. 이 이미지는 Python 개발 환경을 제공하며, Alpine 리눅스를 기반으로 합니다
FROM python:3.8.0-alpine

# 작업 디렉토리 설정
WORKDIR /usr/src/app

#Python 환경 변수를 설정
# .pyc 파일을 생성하지 않도록 설정
#파이썬 출력을 버퍼링하지 않도록 설정
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#해당 줄들은 Alpine 리눅스 패키지 매니저인 apk를 사용하여 필요한 종속성을 설치하는 명령
# apk update는 패키지 목록을 업데이트
# apk add는 PostgreSQL 개발 라이브러리와 기타 필요한 패키지들을 설치
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev #--(5.2)
RUN apk add libffi-dev #cffi설치 에러



#현재 디렉토리의 모든 파일을 컨테이너 내의 /usr/src/app/ 디렉토리로 복사
COPY . /usr/src/app/
# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#static 파일이 404되는 오류를 해결위함
CMD ["bash", "-c", "python manage.py collectstatic --settings=BACKEND.settings.deploy --no-input"]
