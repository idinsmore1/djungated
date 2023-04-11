from django.urls import path
from variant import views

urlpatterns = [
    path('', views.variant_index, name='variant_index'),
    path('<str:variant>', views.phewas, name='phewas_view'),
]
