from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('categoria/<uuid:categoria_id>/', views.post_list, name='post_list'),
    path('form_emprendimiento/', views.formulario, name = "FormEmp" ),
    path('post/<uuid:post_id>/', views.post_detail, name='post_detail'),
    path('buscar/', views.buscar_posts, name='buscar_posts'),
    path('buscar_categorias/', views.buscar_categorias, name='buscar_categorias'),
    
    

]