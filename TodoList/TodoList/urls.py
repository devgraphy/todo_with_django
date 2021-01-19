from django.contrib import admin
from django.urls import path, include

# 어떤 액션에 어떤 view의 어떤 template을 호출할 것인지
urlpatterns = [ 
    # path('admin/', admin.site.urls),
    path('',include('todo_app.urls'))   #아무 것도 없이 들어올 때 # 해당 dir에 파일없으니 생성 필요

]
