from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import Test

# Create your views here.

# get 요청 시 html 파일 그대로 return한다
def test_html(request) :
    return render(request, 'test/test.html')

# get 요청 시 html + data return
def test_html_data(request) :
    my_name = "Lee"
    return render(request, 'test/test.html',{'name':my_name})
# name:my_name을 딕셔너리 형태로 던져주게 된다. 

# get 요청 시 html + multi data return (json느낌의... 그러나 템플릿엔진인..)
def test_html_multi_data(request) :
    data = {
        'name' : "Lee",
        'age' : 20
    }   
    return render(request, 'test/test.html',{'data':data})
# 'data' = key data = values 


# get 요청 시 html + data return
def test_Json_data(request) :
    data = {
        'name' : "Lee",
        'age' : 20
    }    
    return JsonResponse(data)
# render는 웹개발에서 화면을 return해줄때 사용하는 용어다.
# 그냥 리턴하면 파이썬의 자료 형태이므로 변환을 해줘야한다. 파이썬에 dict와 유사한 json형태로 변환해서 return한다.

# 사용자가 get방식으로 쿼리파라미터 방식 데이터를 넣어놓을 때
# 1. 쿼리 파라미터 방식 : localhost:8000/author?id=10&name=lee
# 2. pathvariable 방식 (현대적인 방식) : localhost:8000/author/10
def test_html_parameter_data(request) :
    id = request.GET.get('id')
    name = request.GET.get('name')
    print(id)
    print(name)
    return render(request, 'test/test.html',{})
# GET방식 > get 꺼내온다 정보 안에서 id 정보를  


# 사용자가 get방식으로 쿼리파라미터 방식 데이터를 넣어놓을 때
# 1. 쿼리 파라미터 방식 : localhost:8000/author?id=10&name=lee
def test_html_parameter_data(request) :
    myname = request.GET.get('name')
    email = request.GET.get('email')
    password = request.GET.get('password')
    data = {
        'name':myname,
        'email' : email,
        'password' : password
    }
    return render(request, 'test/test.html',{'data':data})


# 2. pathvariable 방식 (현대적인 방식) : localhost:8000/author/10
def test_html_parameter_data2(request, my_id) :
    print(my_id)
    return render(request, 'test/test.html',{})



# form 태그를 활용한 post 방식
# 화면을 rendering(화면 리턴) 해주는 method 필요
def test_post_form(request):
    return render(request, 'test/test_post_form.html')


# POST방식
def test_post_handle(request):
   
   if request.method == 'POST':
    my_name = request.POST['user_name']
    my_email = request.POST['user_email']
    my_password = request.POST['user_password']

    # DB에 INSERT -> save함수 사용 
    # DB의 테이블과 SYNC가 맞는 TEST클래스에서 객체를 만들어 SAVE
    t1 = Test()
    t1.name = my_name
    t1.email = my_email
    t1.password = my_password
    t1.save()
    return redirect('/') # http://localhost:8000/ 으로 이동해라 
   else :
        return render(request, 'test/test_post_form.html')
       
#post 요청은 요청 후 적절한 상태코드를 줘야 한다.get처럼 html 화면 응답을 줄게 없으니 200 이런거. return HttpResponse('가입을 축하드립니다') 

# select하기 (단건)
def test_select_one(request, my_id) :
    # 단건만을 조회할 때는 get함수 사용 
    t1 = Test.objects.get(id = my_id)
    
    return render(request, 'test/test_select_one.html', {'data':t1})


# select하기 (all)

def test_select_all(request) :
    # 모든 데이터 조회 : select * from xxx; all()함수 사용 
    # 머라고 검색했는지 ? 
    # 객체형식이기 떄문에 i[name]가 아닌 i.name 으로 표현

    tests = Test.objects.all()
    # for i in tests:
    #     print(i.name)
    return render(request, 'test/test_select_all.html',{'datas':tests})

# where조건으로 다건을 조회할 때는 filter()사용 . 
# http://localhost:8000/test_select_multi?name=haemin 쿼리파라미터방식

def test_select_multi(request) :
    my_name=request.GET.get('name')
    test1=Test.objects.filter(name = my_name)
    return render(request, 'test/test_select_multi.html',{'data':test1})
# 조건을 걸려는 칼럼을 변수화 : my_name = ~
# filter 함수를 이용해서 조회하겠다는 것을 객체화 시킴
#

# update하기 위해서는 해당 건을 사전에 조회하기 위한 id 값이 필요
# method는 등록과 동일하게 save() 함수 사용
# save 함수는 신규객체를 save하면 insert, 기존객체를 save하면 update
def test_update(request):
   if request.method == 'POST':
    my_id = request.POST['user_id'] ## id를 먼저 입력하고 원래 있던 id를 get하겠다는 의미 
    t1 = Test.objects.get(id = my_id)
    my_name = request.POST['user_name']
    my_email = request.POST['user_email']
    my_password = request.POST['user_password']
    print(type(my_id))
    # t1 = Test() # 객체를 만드는 부분이라 x 
    # 기존에 존재하는 t1을 가져와서 다시 정보를 입력하는 거라서 update임.
    t1.name = my_name
    t1.email = my_email
    t1.password = my_password
    t1.save()
    return redirect('/')
   else :
        return render(request, 'test/test_update.html')

# delete() 함수 사용해서 삭제함. update와 마찬가지롤 기존객체 조회 후 delete()
# 조회 후 삭제 

# def test_update(request):
#    if request.method == 'POST':
#     my_id = request.POST['user_id']
#     t1 = Test.objects.get(id = my_id)
#     t1.delete()
#     return redirect('/')
#    else :
#         return render(request, 'test/test_update.html')


