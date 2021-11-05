from rest_framework import serializers
from avaliacoes import models

class AvaliacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Avaliacoes
        fields = '__all__'