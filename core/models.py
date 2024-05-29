from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to="imgs")
    short_description = models.TextField()
    full_description = models.TextField()

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"

    def __str__(self):
        return self.name

class Message(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    subject = models.CharField(max_length=200, verbose_name='Тема')
    message = models.TextField(verbose_name='Сообщение')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Сервисы')

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return self.subject
    
class Project(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to="imgs")
    full_description = models.TextField()
    address = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.name
    

class Blog(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to="imgs")
    full_description = models.TextField()
    short_description = models.TextField()
    date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"

    def __str__(self):
        return self.name