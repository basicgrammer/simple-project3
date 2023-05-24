## Simple Project 3 ##

----

### 개발 시 필수 사항 

- PEP8
- Python 3.8
- Django 2.2.24
- requirements.txt or pyproject.toml
- README.md 실행 방법 명시
- API를 실행할 수 있는 Postman Export 결과 or API 테스트를 수행하는 테스트코드 작성

### 개발 시 참고사항
- SECRET_KEY 같은 비밀키 값은 프로젝트 내 포함할 것


### 그외 추가 사항
- 테스트 코드 작성
    - pytest를 활용한 테스트 코드 작성
    - 테스트 실행 방법을 README.md에 작성
    - 커버리지 측정은 codecov를 권장

- CI를 활용한 테스트 자동화 및 커버리지 결과 전송 (Github Action 권장)

- Docker
    - 하나의 컨테이너에 웹 서버 및 WSGI 애플리케이션이 실행되도록 Dockerfile 작성 또는 docker-compose.yml 작성



### 개발 내용 정리

- codecov 도입
- Action CI 도입

### Swagger

```shell

    API Documentation 접속 ==> {URL}/doc/ # ex) 192.168.0.10/doc/
    Swagger 접속 ==> {URL}/swagge/  # ex) 192.168.0.10/swagger/

```


### Action CI 설정 참고 사항

```shell
    # Repository의 GitHub Action CI  설정 파일 위치
    # FileName = .github/workflows/action.yml
    DJANGO_SETTING_MODULE = project.core.pytest_settings  # 세팅에 변경이 필요한 경우 해당 파일을 변경해주세요.
    python_files = test_*.py  # 테스트를 위해 test_로 시작하는 파일은 모두 테스트를 수행합니다.
```

### Codecov 관련 정보

```shell
    # Codecov에 코드 커버리지 측정 결과 업로드 시, Public으로 설정된 GitHub의 Repository와 연결이 설정된 경우 Token값이 필요하지 않음
    # 즉 Codecov에서 Public 레포와 연결되면서 코드 커버리지 업데이트시 Token 정보가 필요하지 않음
```

- Github Action과 연결된 Codecov 결과
<img width="1042" alt="image" src="https://github.com/basicgrammer/simple-project3/assets/55322993/5cbb69dd-4e54-4588-b11d-79fff26ba1f7">

## 해야할 것

- API 테스트 코드 마무리 처리  
- PEP8 스타일 가이드 맞춤


## Docker 명령어

```shell
    # 해당 프로젝트에서는 docker-compose를 기반으로 개발했습니다.
    # 컨테이너 구동 환경이 개발된 환경과 다를 수 있으므로 쉘 스크립트 기반이 아닌 구동 명령어를 아래 명시합니다.

    # 컨테이너 기동 상태 확인
    $ docker-compose ps -a

    # 컨테이너 기동 종료
    $ docker-compose down 

    # 컨테이너 빌드 및 백그라운드 기동
    $ docker-compose up --build -d

    # 컨테이너 로그 확인 
    $ docker logs --tail 10000 -f {container_name}
```
