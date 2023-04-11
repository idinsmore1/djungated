from django.urls import path
from pheno import views

urlpatterns = [
    path('', views.assoc_index, name='pheno_index'),
    path('<str:phecode>', views.gwas, name='gwas_view'),
]