
from django.db import models # 자동으로 쿼리 생성

# Create your models here.
# entity 저장될 예정
# entity - models.Model 상속
# model 작성하고 view 작성
class Todo(models.Model):   # table 명 Todo
    # DB에 반영할 column list 작성
    objects = models.Manager()
    content = models.CharField(max_length=255)  # content 라는 컬럼의 타입 지정
                                                # id는 PK로 기본적으로 들어감


