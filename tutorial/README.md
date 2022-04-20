[강의노트 바로가기](https://www.notion.so/fastapi/dddb1dba1d154834bd7968a8daf89995?v=c35c3464fa3d43b3b65d5cfd75cd84a5)

## FastAPI 기초

Chapter1-1 및 Chapter1-2 강의노트에 수록된 코드 조각입니다.

## Chapter1-1
각 파일은 `python <filenmae>.py` 와 같이 바로 실행 할 수 있습니다.

### 사전 설치

```bash
$ pip install fastapi uvicorn
```

## Chapter1-2

각 파일은 단독 실행이 불가능합니다.. vs code에서는 프로젝트의 소스 디렉토리 설정이 어려운 이유와 더불어,

- database.py
- models.py
- schemas.py

를 Chapter1-2에서 공통으로 사용할 예정이기 때문도 있습니다. 이 디렉토리의 소스를 tutorial_app/main.py 에 복사/붙여넣기 하여 사용하세요.

### 사전 설치

먼저, tutorial_app/init-db.sh를 실행하세요. 도커로 MySQL을 실행합니다.

```shell
$ cd tutorial_app
$ ./init-db.sh
```

다음은 필수 라이브러리를 설치해야 합니다.

```bash
$ cd tutorial_app
$ pip install requirements.txt
```

### 실행

tutorial/chapter_1-2/ 하위에 있는 파일을 tutorial_app/main.py에 복사/붙여넣기 하세요. 그리고

```bash
$ uvicorn tutorial_app.main:app --host 0.0.0.0 --reload 
```
을 실행합니다.

### 강의노트와의 차이점

강의노트는 설명을 편하게/쉽게 보기 위해 uvicorn 임포트 구문이 없습니다. 추가로 강의노트는 보다 더 집중할 수 있도록 앤드포인트가 하나였지만, 본 코드들에는 소주제 별로 묶여서 하나의 파일로 각각 존재합니다. 때문에 앤드포인트가 다르거나 함수명이 다를수 있지만 놀라지 마세요. 내용은 전부 같습니다! 😎
