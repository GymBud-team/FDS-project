from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime

class Caracteristicas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    idade = models.PositiveIntegerField(default=None)
    peso_inicial = models.FloatField(default=None)
    peso_atual = models.FloatField(default=None)
    altura =  models.FloatField(default=None)
    inicio = models.DateField(auto_now_add=True)


class Metas(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    peso = models.FloatField(default=None)
    calorias = models.PositiveIntegerField(default=None)

    um = 1
    um_meio = 1.5
    dois = 2
    dois_meio = 2.5
    tres = 3
    tres_meio = 3.5
    quatro = 4
    quatro_meio = 4.5
    cinco = 5

    AGUA = (
    (um, '1 litro'),
    (um_meio, '1.5 litros'),
    (dois, '2 litros'),
    (dois_meio, '2.5 litros'),
    (tres, '3 litros'),
    (tres_meio, '3.5 litros'),
    (quatro, '4 litros'),
    (quatro_meio, '4.5 litros'),
    (cinco,'5 litros'),
    )
  
    agua = models.FloatField(default=None, choices=AGUA)

class PesoHistory(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    peso = models.FloatField(default=None)
    created = models.DateField(auto_now_add=True)

class IngestaoAgua(models.Model):
    agua = models.PositiveIntegerField(default=None)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateField(auto_now_add=True)

    @property
    def get_day(self):
        return self.created.day
    
    def get_month(self):
        return self.created.month

class IngestaoCalorias(models.Model):
    calorias = models.PositiveIntegerField(default=None)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateField(auto_now_add=True)

    @property
    def get_day(self):
        return self.created.day
    
    def get_month(self):
        return self.created.month
    
class Post(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField(default=None)
    created = models.DateTimeField(default=datetime.now)
    likes = models.ManyToManyField(User, related_name='blogpost_like')

    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comentario = models.CharField(max_length = 300)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)

    def number_of_comentario(self):
        return self.comentario.count()

class RequestWorkout(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    perda = 'Perda de Peso'
    ganho = 'Ganho de Massa'
    definicao = 'Definição'
    bemestar = 'Bem-Estar'
    manutencao = 'Manutenção de Físico'
    goal_choices = (
        (perda,'Perda de Peso') ,
        (ganho,'Ganho de Massa'),
        (definicao,'Definição'),
        (bemestar,'Bem-Estar'),
        (manutencao,'Manutenção de Físico'),
    )

    goal = models.TextField(default = None, choices = goal_choices)

    segunda = 'Segunda-Feira'
    terca = 'Terça-Feira'
    quarta = 'Quarta-Feira'
    quinta = 'Quinta-Feira'
    sexta = 'Sexta-Feira'
    sab = 'Sábado'
    dom = 'Domingo'
    days_choices = (
        (segunda,'Segunda-Feira'),
        (terca,'Terça-Feira'),
        (quarta,'Quarta-Feira'),
        (quinta,'Quinta-Feira'),
        (sexta,'Sexta-Feira'),
        (sab,'Sábado'),
        (dom,'Domingo'),
    )
    hours_per_day = models.PositiveIntegerField(default = None)
    # availability = models.BooleanField(default = None, choices = days_choices)

    problemas = models.TextField(default = None)