## Simple Project 3 ##

--------
### 개발 언어 및 환경
- OS : Ubuntu 22.04.2 LTS
- python : 3.8
- Django : 2.2.24 with DRF
- Docker Engine : 23.0.3
- Docker-compose : 2.13.0
- Postgres 13.11
--------
## Git Clone 시 참고 사항!!
- 해당 레포의 데이터는 Clone 시 환경이 충족한다면 컨테이너 환경에서 바로 동작할 수 있도록 DB, 비밀키 등을 동봉해두었습니다.

--------
### requirements.txt
- 기존에 작성된 requirements.txt가 아닌 pip freeze 과정으로 생성된 정보입니다.
- 테스트 시 라이브러리 설치에 오류가 발생하는 경우 참고해주세요.

```txt
certifi==2023.5.7
charset-normalizer==3.1.0
codecov==2.1.13
coreapi==2.3.3
coreschema==0.0.4
coverage==7.2.6
Django==2.2.24
djangorestframework==3.13.1
drf-writable-nested==0.7.0
drf-yasg==1.20.0
exceptiongroup==1.1.1
execnet==1.9.0
idna==3.4
inflection==0.5.1
iniconfig==2.0.0
itypes==1.2.0
Jinja2==3.1.2
MarkupSafe==2.1.2
packaging==23.1
pluggy==1.0.0
psycopg2-binary==2.9.6
pytest==7.3.1
pytest-cov==4.0.0
pytest-django==4.5.2
pytest-xdist==3.3.1
pytz==2023.3
requests==2.31.0
ruamel.yaml==0.17.26
ruamel.yaml.clib==0.2.7
sqlparse==0.4.4
tomli==2.0.1
uritemplate==4.1.1
urllib3==2.0.2
```
--------
### Swagger && API Document

```shell
    API Document 접속 : {URL}/doc/ # ex) 192.168.0.10/doc/
    Swagger 접속 : {URL}/swagge/  # ex) 192.168.0.10/swagger/
```
--------

### Action CI 설정 참고 사항
```shell
    # Repository의 GitHub Action CI  설정 파일 위치
    # FileName = .github/workflows/action.yml
    
```
- 개발 시 소스코드의 CI 및 테스트를 위한 Github Action 연동 관련 스크린샷
<img width="1203" alt="image" src="https://github.com/basicgrammer/simple-project3/assets/55322993/d94fc542-de0c-4138-9e22-2f657ac9beb8">
--------
### Codecov 관련 정보

```shell
    # Codecov에 코드 커버리지 측정 결과 업로드 시, Public으로 설정된 GitHub의 Repository와 연결이 설정된 경우 Token값이 필요하지 않음
    # 즉 Codecov에서 Public 레포와 연결되면서 코드 커버리지 업데이트시 Token 정보가 필요하지 않음
```

- Github Action과 연동된 Codecov 관련 스크린샷
<img width="1042" alt="image" src="https://github.com/basicgrammer/simple-project3/assets/55322993/5cbb69dd-4e54-4588-b11d-79fff26ba1f7">

--------

### Postman 관련 정보
- Publish doc 주소 
- URL : https://www.postman.com/satellite-astronaut-70983143/workspace/my-workspace/collection/23508973-b49059fd-9048-4b41-bbf0-e344ddbb6d9b?action=share&creator=23508973


--------
### Docker 명령어

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

    # 컨테이너 내부 접속
    $ docker exec -it {container_name} /bin/bash

    # 일부 컨테이너 정지
    $ docker-compose stop {container_name}
```

### pytest (테스트 코드)

```shell
    # 파일 위치 : /backend/pytest
    # 테스트 참고 파일 위치 : /backend/pytest.ini
```

### pytest 테스트 실행 방법 

```shell

    # Action에서 테스트 되는 환경이 아니라면 pytest.ini의 맞춤형 설정 변경이 필요함
    
    # pytest.ini 파일
    DJANGO_SETTING_MODULE = project_core.pytest_settings  # Github Action 버전
    DJNAGO_SETTING_MODULE = project_core.settings # 도커 컨테이너 구동 버전
    python_files = test_*.py  # 테스트를 위해 test_로 시작하는 파일은 모두 테스트를 수행합니다.

    # 코드 커버리지 검사를 진행하는 명령어
    $ pytest --cov

    # 코드 커버리지 검사 및 Codecov 업로드를 위한 xml 파일 생성 명령어 (Action 환경에서 사용하는 명령어)
    $ pytest --cov --cov-report=xml

    # 테스트를 통해 코드 결함을 확인하는 명령어
    $ python -m pytest {pytest_dir}  # ex) python -m pytest pytest

    # 파일 하나만 테스트를 진행하는 경우
    $ pytest {file_name}  # ex) pytest ./pytest/test_create_api.py
    
    # pytest.ini 설정이 되어있기 때문에 아래 명령어도 동작함
    $ pytest -k  # 특정 테스트 함수만 실행
    $ pytest -v  # 각 테스트 함수 실행 결과를 함께 출력
    $ pytest -vv  # verbosity level을 높혀 더욱 자세한 테스트 결과를 출력
    $ pytest -s  # Failed 작업에 대한 stdout, stderr 메시지 캡처

    # 테스트 하면서 보편적으로 가장 많이 사용했었던 명령어
    $ pytest -svv


```