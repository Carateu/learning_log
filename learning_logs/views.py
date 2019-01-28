from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse

from .models import Topic,Entry
from .forms import TopicForm,EntryForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
	"""a pagina inicial do projeto"""
	return render(request,'learning_logs/index.html')

@login_required
def topics(request):
	"""a  pagina de topicos do projeto"""
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	context = {'topics':topics}
	return render(request,'learning_logs/topics.html',context)
	
@login_required	
def topic(request,topic_id):
	"""as entradas de cada topico do projeto"""
	#pega todos os objetos de Topic que tenham o topic_id
	topic = Topic.objects.get(id=topic_id)
	# garantindo que o topico pertence ao usuário logado
	if topic.owner!= request.user:
		raise Http404
		
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic':topic,'entries':entries}
	return render(request, 'learning_logs/topic.html',context)

@login_required
def new_topic(request):
	"""adiciona um novo topico"""
	if request.method!='POST':
		#nenhum dado passado, criar novo formulario
		form = TopicForm()
	else:
		# Dados submetidos com POST
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic= form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))
			
	context = {'form':form}
	return render(request,'learning_logs/new_topic.html',context)

@login_required
def new_entry(request,topic_id):
	"""adiciona uma nova entrada"""
	topic = Topic.objects.get(id=topic_id)
	if request.method!='POST':
		form = EntryForm()
	else:
		form = EntryForm(request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))
			
	context = {'topic':topic,'form':form}
	return render(request,'learning_logs/new_entry.html',context)
	
@login_required
def edit_entry(request,entry_id):
	"""editando uma entrada"""
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	if topic.owner!= request.user:
		raise Http404
		
	if request.method!='POST':
		# criando um formulario preenchido com a entrada anterior
		form = EntryForm(instance=entry)
	else:
		form = EntryForm(instance=entry,data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
		
	context = {'entry':entry,'topic':topic,'form':form}
	return render(request,'learning_logs/edit_entry.html',context)
