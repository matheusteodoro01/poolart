from django.db import models
from uuid import uuid4

# Create your models here.


class Avaliacoes(models.Model):

    id_avaliacao = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)

    descricao = models.CharField(max_length=255)
    classificao = models.CharField(max_length=255)
    id_author = models.IntegerField()
    id_artista = models.IntegerField()


create_at = models.DateField(auto_now_add=True)
