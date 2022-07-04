#Corrigir a execucao da busca
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Tarefa
from .forms import TarefaForm
from django.contrib import messages

# Create your views here.
@login_required
def ListaTarefas(request):
	search = request.GET.get('search')
	filter = request.GET.get('filter')

	if search:
		tarefas = Tarefa.objects.filter(title__icontains=search, user=request.user)
	
	elif filter:
		tarefas = Tarefa.objects.filter(feito=filter, user=request.user)	

	else:
		tarefas_lista = Tarefa.objects.all().filter(user=request.user)
		paginator = Paginator(tarefas_lista, 4)
		pagina = request.GET.get('pagina')
		tarefas = paginator.get_page(pagina)

	return render(request, 'tarefas/tarefas.html', {'tarefas': tarefas})

@login_required
def VerTarefa(request, id):
	tarefa = get_object_or_404(Tarefa, pk=id)
	return render(request, 'tarefas/tarefa.html', {'tarefa': tarefa})

@login_required
def NovaTarefa(request):
	if request.method == 'POST':
		form = TarefaForm(request.POST)

		if form.is_valid():
			tarefa = form.save(commit=False)
			tarefa.done = 'fazendo'
			tarefa.user = request.user
			tarefa.save()
			return redirect('/')

	form = TarefaForm()
	return render(request, 'tarefas/addTarefa.html', {'form': form})

@login_required
def EditarTarefa(request, id):
	tarefa = get_object_or_404(Tarefa ,pk=id)
	form = TarefaForm(instance=tarefa)

	if(request.method == 'POST'):
		form = TarefaForm(request.POST, instance=tarefa)

		if(form.is_valid()):
			tarefa.save()
			return redirect('/')
		else:
			return render(request, 'tarefas/editartarefa.html', {'form': form, 'tarefa': tarefa})

	else:
		return render(request, 'tarefas/editartarefa.html', {'form': form, 'tarefa': tarefa})

@login_required
def DeletarTarefa(request, id):
	tarefa = get_object_or_404(Tarefa, pk=id)
	tarefa.delete() 
	messages.info(request, 'Tarefa deletada com sucesso!')

	return redirect('/')

@login_required
def ChangeStatus(request, id):
	tarefa = get_object_or_404(Tarefa, pk=id)

	if(tarefa.feito == 'fazendo'):
		tarefa.feito = 'feito'
	else:
		tarefa.feito = 'fazendo'

	tarefa.save()
	return redirect('/')