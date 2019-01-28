from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
	
def logout_view(request):
	"""logout users"""
	logout(request)
	return HttpResponseRedirect(reverse('learning_logs:index'))
	
	
def register(request):
	"""registrando novos usuarios"""
	if request.method != 'POST':
		#mostra um formulario de registro em branco
		form = UserCreationForm()
	else:
		#processando formulario preenchido
		form = UserCreationForm(data=request.POST)
		if form.is_valid():
			new_user = form.save()
			# logando o usuario e redirecionando para home page
			authenticated_user = authenticate(username=new_user.username,
			password = request.POST['password1'])
			login(request,authenticated_user)
			return HttpResponseRedirect(reverse('learning_logs:index'))
	
	context = {'form':form}
	return render(request,'users/register.html',context)
