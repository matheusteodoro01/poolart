from avaliacoes import models
from rest_framework import viewsets
from avaliacoes import serializers
from avaliacoes import models


class AvaliacoesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AvaliacoesSerializer
    queryset = models.Avaliacoes.objects.all()
