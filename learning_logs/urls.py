"""definindo URL patterns para o app learning_logs"""

from django.conf.urls import url
from .import views
from django.urls import path

urlpatterns =[
	#Home page
	url(r'^$',views.index, name='index'),
	# mostrando os topicos
	url(r'^topics/$',views.topics, name='topics'),
	#mostrando cada topico
	path('topics/<int:topic_id>/', views.topic, name= 'topic'),
	# pagina de formulario para adicionar novo topico
	path('new_topic/',views.new_topic,name='new_topic'),
	# pagina pra adicionar uma nova entrada
	path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry'),
	# pagina praeditar as entradas
	path('ediT_entry/<int:entry_id>/',views.edit_entry,name='edit_entry'),
	
	]
