from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListaTarefas, name='ListaTarefas'),
    path('novatarefa/', views.NovaTarefa, name='nova-tarefa'),
    path('editar/<int:id>', views.EditarTarefa, name='editar-tarefa'),
    path('changestatus/<int:id>', views.ChangeStatus, name='change-status'),
    path('deletar/<int:id>', views.DeletarTarefa, name='deletar-tarefa'),
    path('tarefa/<int:id>', views.VerTarefa, name='lista-tarefas'),
]
