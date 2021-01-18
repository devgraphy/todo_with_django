from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Todo

# Create your views(Controller) here.
# request로부터 파라미터 valid 체크
# 비즈니스 메소드 호출 또는 구현. 원래는 역할을 분리하여 호출하는 게 맞음
# view(template)에서 참조할 데이터 저장
# view(template) 선택(렌더링)

# todo_app/
def index(request): # request는 장고에서 받은 것
    todos = Todo.objects.all()
    content = {"todos": todos}
    return render(request, 'todo_app/index.html', content)   #렌더링

# todo_app/createTodo
def createTodo(request):
    todoContent = request.POST['todoContent']
    new_todo = Todo(content=todoContent)
    new_todo.save()
    return HttpResponseRedirect(reverse("index"))

# todo_app/deleteTodo
def deleteTodo(request):
    delete_todo_id = request.GET['id']
    todo=Todo.objects.get(id=delete_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))