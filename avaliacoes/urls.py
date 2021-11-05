from django.urls import path
from .views import AvaliacoesAPIView


urlpatterns = [

    path('avaliacoes', AvaliacoesAPIView.as_view(), name='avaliacoes')
    
]
