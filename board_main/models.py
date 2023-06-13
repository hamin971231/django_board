from django.db import models

# Create your models here.
# models.py의 클래스와 db의 테이블과 싱크를맞춰 테이블(칼럼정보)자동생성

# 클래스 명 = 테이블 명, 변수 = 컬럼명
class Test(models.Model):
    name= models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    # max_length의 디폴트는 255