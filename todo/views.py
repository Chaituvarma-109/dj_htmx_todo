from django.shortcuts import render, redirect, get_object_or_404

from .forms import TodoForm
from .models import Todo

def index(request):
    todos = Todo.objects.all().order_by('-id')

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = TodoForm()

    context = { 'todos': todos, 'form': form }
    return render(request, "todo/index.html", context)


def delete(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    todo.delete()

    return redirect('index')
