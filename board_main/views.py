from django.shortcuts import render, redirect
from .models import Author, Post
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
   
def post_list(request) :
    return render(request,'post/post_list.html')

# post 탬플릿으로 찾아가서 post_list.html을 열어라
# 근데 urls.py에 매핑되어있는 url로 들어가서 post_list.html을 열것임.


