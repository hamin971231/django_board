# url path mapping하는 곳 
from django.urls import path
from . import views_test, views


urlpatterns = [  
    # path('',views_test.test_html_multi_data),     
    # path('test_json',views_test.test_Json_data),   
    # path('parameter_data',views_test.test_html_parameter_data),  
    # path('parameter_data2/<int:my_id>',views_test.test_html_parameter_data2),   
    # path('test_post_handle',views_test.test_post_handle), 
    # path('test_select_one/<int:my_id>',views_test.test_select_one), 
    # path('test_select_all',views_test.test_select_all), 
    # path('test_select_multi',views_test.test_select_multi), 
    # path('test_update',views_test.test_update), 
    path('',views.home),
    path('authors/',views.author_list),
    path('author/new',views.author_new),
    path('author/<int:my_id>',views.author_detail),
    path('author/<int:my_id>/update',views.author_update),
    path('posts/',views.post_list),
    
    


]

# path('test_select_one/<int:my_id>' -> 값 넣어야함.
# /test_json 으로 가게 된다. 
# path('주소',파일주소.함수명)
