from django.db import models

# python manage.py makemigrations
# 우리가 models.py에 작성하는 python file을 database와 연결하기 위한 파일로 변환시켜 준다
#python manage.py migrate
#database로 연결 시켜주기 위한 파일을 만들었다면, 그 이후에는 그 파일을 연결 시켜주는 명령어 필요.
#그게 위 명령어

class HelloWorld(models.Model):
    text = models.CharField(max_length= 255, null=False)