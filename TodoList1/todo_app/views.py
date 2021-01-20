from django.shortcuts import render # 브라우저에
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Todo    # entity 불러오기


# Create your views here.

# todo_app/
def index(request): # request는 장고에서 받은 것   
    todos = Todo.objects.all()
    content = {"todos": todos}

    # 앱을 한번에 렌더링할 경우 충돌하기 때문에 templates 폴더 안에 앱명과 같은 폴더를 생성하여 파일 관리!
    return render(request, 'todo_app/index.html', content)   
    # return HttpResponse("my todo app")              #OK
    

# todo_app/createTodo - insert -> save메서드
# 입력받아온 정보를 DB에 반영-POST 
def createTodo(request):
    # request.POST : 키로 전송된 자료에 접근할 수 있도록 해주는 사전과 같은 객체
    # 반환 값은 항상 문자열이다.
    # 인자로 키값을 명시한다.
    todoContent = request.POST['Content'] # 해당 태그의 name과 매칭
    new_todo = Todo(content=todoContent)    # model 인자 문법
    new_todo.save() # model.save()
    return HttpResponseRedirect(reverse("index"))   # Redirect vs. forward

# todo_app/deleteTodo - delete -> remove
# 인덱스 초기화 필요
def deleteTodo(request):
    delete_todo_id = request.GET['id']
    todo=Todo.objects.get(id=delete_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse("index"))
