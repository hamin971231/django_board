from django.shortcuts import render, redirect
from .models import Author, Post
from django.http import HttpResponse, HttpResponseNotFound
def home(request) :
    return render(request,'home.html')

## 회원 목록 조회
def author_list(request) :
    authors=Author.objects.all()
    return render(request,'author/author_list.html',{'authors':authors})
# author 탬플릿으로 찾아가서 author_list.html을 열어라
# 근데 urls.py에 매핑되어있는 url로 들어가서 author_list.html을 열것임.



## 회원가입  -> 회원가입은 뎅이터를 리턴해줄 필요가 없어서 {'authors':authors}
def author_new(request) :
    if request.method == 'POST':
        my_name = request.POST['user_name']
        my_email = request.POST['user_email']
        my_password = request.POST['user_password']
        a1 = Author()
        a1.name = my_name
        a1.email = my_email
        a1.password = my_password
        a1.save()
        return redirect('/')  
    else :
        return render(request, 'author/author_new.html')
    
## 회원 상세 조회
def author_detail(request,my_id) :
    author=Author.objects.get(id=my_id)
  
    ## author.posts author에 post 레프트 조인한 것 한사람이 쓴 글의수를 알수있음 
    return render(request,'author/author_detail.html',{'author':author})

## 회원 정보 수정
def author_update(request,my_id):
   author = Author.objects.get(id = my_id)
   if request.method == 'POST':
    my_name = request.POST['user_name']
    my_email = request.POST['user_email']
    my_password = request.POST['user_password']
    author.name = my_name
    author.email = my_email
    author.password = my_password
    author.save()
    return redirect('/')
   else :
        return render(request, 'author/author_update.html',{'author':author})


# 게시글 목록 페이지   
def post_list(request) :
    return render(request,'post/post_list.html')

# post 탬플릿으로 찾아가서 post_list.html을 열어라
# 근데 urls.py에 매핑되어있는 url로 들어가서 post_list.html을 열것임.

## 게시글 목록 조회
## order_by('-칼럼명') : 이렇게 주면 내림차순 정렬
def post_list(request) :
    ##[ {id:1, title: ,contents: ...author:{id=, name='aaa',email=...}}]
    ## post.author.name : aaa 출력
    posts=Post.objects.filter().order_by('-created_at')

    return render(request,'post/post_list.html',{'posts':posts})
# author 탬플릿으로 찾아가서 author_list.html을 열어라
# 근데 urls.py에 매핑되어있는 url로 들어가서 author_list.html을 열것임.

## 새 글 작성하기 
def post_new(request) :
    if request.method == 'POST':
        my_title = request.POST["user_title"]
        my_contents = request.POST["user_textarea"]
        my_email = request.POST['user_email']
        p1 = Post()
        if my_email :
            try :
                a1 = Author.objects.get(email=my_email) ##이메일이 없을떄 에러가 발생하는 부분임.
                p1.author = a1 #{id=1,name='hong', email='adf@naver.com}이 a1인데 
            # 장고에서 a1객체에서 id 값만 빼서 db에 저장할 때는 author_id에 id값만뺴와서 저장한다.          
            except Author.DoesNotExist :
                ## HttpResponse 는 200 ok가 나옴. 
                return HttpResponseNotFound('존재하지 않는 이메일입니다.')
                
        p1.title = my_title
        p1.contents = my_contents
        p1.email = my_email
        p1.save()
        return redirect('/')  
    else :
        return render(request, 'post/post_new.html')
    
## 게시글 상세 조회하기
def post_detail(request,my_id) :
    post=Post.objects.get(id=my_id)
    return render(request,'post/post_detail.html',{'post':post})

## 게시글 수정 
def post_update(request,my_id):
   post = Post.objects.get(id = my_id)
   if request.method == 'POST':
    my_title = request.POST['user_title']
    my_contents = request.POST['user_textarea']
    post.title = my_title
    post.contents = my_contents
    post.save()
    return redirect('/')
   else :
        return render(request, 'post/post_update.html',{'post':post})