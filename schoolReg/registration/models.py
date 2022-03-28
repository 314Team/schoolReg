from statistics import mode
from tabnanny import verbose
from django.db import models

# Create your models here.
class Student(models.Model):
    #id -> pk(primary key)
    name = models.CharField(max_length=20, verbose_name='Имя')
    surname = models.CharField(max_length=20, verbose_name='Фамилия')
    fathername = models.CharField(max_length=20,blank=True,  verbose_name='Отчество')

    mom = models.CharField(max_length=50,blank=True,  verbose_name='ФИО матери')
    momPhone = models.CharField(max_length=20,blank=True,  verbose_name='Тел. номер матери')
    dad = models.CharField(max_length=50,blank=True,  verbose_name='ФИО отца')
    dadPhone = models.CharField(max_length=20,blank=True,  verbose_name='Тел. номер отца')
    
    birhDate = models.DateField( verbose_name='Дата рождения')
    sex = models.BooleanField(null=True,  verbose_name='Пол') #0-f 1-m n-nonbin
    grade = models.SmallIntegerField( verbose_name='Класс')
    address = models.CharField(max_length=100, verbose_name='Адрес')    
    photo = models.ImageField(upload_to='students/photo/%Y/%m/%d',blank=True, verbose_name='Фото')
    additional = models.TextField(blank=True, verbose_name='Дополнительно')
    phone = models.CharField(max_length=20, verbose_name='Тел. номер')
    email = models.EmailField(blank=True, verbose_name='Эл. почта')
    
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.surname+' '+self.name+' '+self.birhDate

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'