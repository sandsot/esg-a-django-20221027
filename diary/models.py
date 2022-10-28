from django.db import models
from django.core.validators import MaxValueValidator

class Memory(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) :
        return f'[{self.pk}]{self.title}'
    
    def get_absolute_url(self):
        return f'/diary/{self.pk}/'

class Meta:
    # 쿼리셋에서 order_by를 지정하지 않았을 때, 사용되는 기본 정렬
    ordering =['-id']