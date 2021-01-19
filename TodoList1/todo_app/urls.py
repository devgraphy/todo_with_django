from django.urls import path
from . import views
# controller의 누가 응답할건지 url 매핑
urlpatterns = [
    # 아무것도 명시되지 않았을 때 todo_app의 views의 index 함수가 응답해라
    path('',views.index, name="index"), # name 은 옵션. alias
    path('createTodo/', views.createTodo, name="createTodo")
]
