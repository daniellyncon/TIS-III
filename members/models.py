from django.db import models


# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=10, verbose_name='Nome')
    last_name = models.CharField(max_length=50, verbose_name='Sobrenome')
    e_mail = models.EmailField(verbose_name='E-mail')
    department = models.CharField(max_length=30, verbose_name='Area')
    post = models.CharField(max_length=30, verbose_name='Cargo')
    leader = models.CharField(max_length=50, verbose_name='Lider')

    def __str__(self):
        return self.name


