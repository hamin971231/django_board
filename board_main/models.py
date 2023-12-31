from django.db import models

# Create your models here.
# models.py의 클래스와 db의 테이블과 싱크를맞춰 테이블(칼럼정보)자동생성

# 클래스 명 = 테이블 명, 변수 = 컬럼명
class Test(models.Model):
    name= models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    # max_length의 디폴트는 255


class Author(models.Model):
    name= models.CharField(max_length=20)
    email = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=20)
    # DB설정에 default timestamp가 걸리는 것이 아닌, 장고가 현재시간을 insert 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    # FK를 설정한 변수명에 _id가 붙게된다
    #  on_delete = models.CASCADE 옵션 가능 
    # FK에 db에서 조회할때 나오는 author_id 는 파이선에서는 author객체와 같은것이다. 
    author = models.ForeignKey(Author, on_delete = models.SET_NULL, null=True, related_name='posts')
    ## related_name 은 author를 조회할때 post테이블이랑 같이 조회하고 싶은데 그 이름을 'posts'라고 지정하겠다는 말임
    ## -> author.posts.count() => 근데 이건 리스트 형태임 
    
## docker 에서 test