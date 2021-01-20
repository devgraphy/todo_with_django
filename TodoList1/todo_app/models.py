"""
클래스 각각은 모델이라 부른다.
각 모델은 django.db.model.Model을 상속받는 클래스로 표현한다.
그 안에 변수를 선언할 수 있는데, 그 변수들은 모델에서 DB 속성을 표현한다.
"""
from django.db import models

# Create your models here.
class Todo(models.Model):   # table 명 Todo
    # DB에 반영할 column list 작성
    objects = models.Manager() # all, get 메서드
    content = models.CharField(max_length=255)