from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, cadastro, confirmacao  

urlpatterns = [
    path('', home, name='home'),
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', redirect_authenticated_user=True), name='login'),  
    path('confirmacao/', confirmacao, name='confirmacao'),
]
