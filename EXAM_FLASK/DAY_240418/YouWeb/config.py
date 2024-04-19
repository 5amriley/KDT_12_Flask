# 모듈 로딩
import os

# 다양한 DBMS URI - SQLITE
BASE_DIR = os.path.dirname(__file__)
DB_NAME_SQLITE = 'app.db'

## 다양한 DBMS URI
DB_SQLITE_URI = f'sqlite:///{os.path.join(BASE_DIR, DB_NAME_SQLITE)}'
##                               ID   PW             PORT  DB
DB_MYSQL_URI = f'mysql+pymysql://root:2018@localhost:3306/flask_db1'

# DB_MARIA_URI = 'mariadb+mariadb://root:pw@localhost:3306/testdb'
# DB_POST_URI = 'postgresql+pg8000://scott:tiger@localhost/test'

## 사용할 DBMS 설정 / SQLALCHEMY_시작 변수명 고정
SQLALCHEMY_DATABASE_URI = DB_MYSQL_URI
SQLALCHEMY_TRACK_MONIFICATIONS = False
