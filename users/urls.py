"""urls patterns pra users"""

from django.conf.urls import url
from django.contrib.auth.views import LoginView

from .import views

urlpatterns = [
			#página de login
			url(r'^login/$',LoginView.as_view(template_name='users/login.html'),name = 'login'),
			#página de logout
			url(r'^logout/$',views.logout_view,name='logout'),
			#página de registro
			url(r'^register/$',views.register,name='register'),
]
