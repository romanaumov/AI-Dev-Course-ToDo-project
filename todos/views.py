from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Todo
from .forms import TodoForm


def todo_list(request):
    """Display all todos"""
    todos = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})


def todo_create(request):
    """Create a new todo"""
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo created successfully!')
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todos/todo_form.html', {'form': form, 'action': 'Create'})


def todo_edit(request, pk):
    """Edit an existing todo"""
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo updated successfully!')
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/todo_form.html', {'form': form, 'action': 'Edit'})


def todo_delete(request, pk):
    """Delete a todo"""
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        messages.success(request, 'Todo deleted successfully!')
        return redirect('todo_list')
    return render(request, 'todos/todo_confirm_delete.html', {'todo': todo})


def todo_toggle(request, pk):
    """Toggle todo completion status"""
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_completed = not todo.is_completed
    todo.save()
    status = 'completed' if todo.is_completed else 'reopened'
    messages.success(request, f'Todo marked as {status}!')
    return redirect('todo_list')
