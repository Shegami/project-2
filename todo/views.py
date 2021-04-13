from django.shortcuts import render, redirect, HttpResponse
from todo.forms import NewTaskForm
from todo.models import NotCompletedTasks, CompletedTasks


def main(request):
    if request.method == 'GET':
        return render(request, 'main.html')


def get_tasks(request):
    context = {
        'tasks': NotCompletedTasks.objects.all().order_by('order')
    }
    return render(request, 'get_tasks.html', context)


def create_task(request):
    if request.method == 'GET':
        context = {
            'form': NewTaskForm()
        }
        return render(request, 'create_task.html', context)
    else:
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_task')
        errors = form.errors
        return HttpResponse(f'error in {errors}')


def edit_task(request, task_id):
    if request.method == 'GET':
        context = {
            'form': NewTaskForm(),
            'task_id': task_id
        }
        return render(request, 'edit_task.html', context)
    task = NotCompletedTasks.objects.get(pk=task_id)
    edited_task = NewTaskForm(request.POST, instance=task)
    edited_task.save()
    return redirect('get_tasks')


def delete_task(request, task_id):
    task_to_delete = NotCompletedTasks.objects.get(pk=task_id)
    task_order = task_to_delete.order
    task_to_delete.delete()
    update_order_tasks(task_order)

    return redirect('get_tasks')


def task_up_down(request, task_id, button):
    task_to_move = NotCompletedTasks.objects.get(pk=task_id)
    task_to_down = NotCompletedTasks.objects.filter(
        order=task_to_move.order-1).first()
    task_to_up = NotCompletedTasks.objects.filter(
        order=task_to_move.order+1).first()

    if button == 'up':
        if task_to_down:
            task_to_move.order -= 1
            task_to_down.order += 1
            task_to_move.save()
            task_to_down.save()

    elif button == 'down':
        if task_to_up:
            task_to_move.order += 1
            task_to_up.order -= 1
            task_to_move.save()
            task_to_up.save()

    return redirect('get_tasks')


def task_completed(request, task_id):
    task = NotCompletedTasks.objects.get(pk=task_id)
    CompletedTasks.objects.create(
        name=task.name,
        priority=task.priority
    )
    return redirect('delete_task', task_id)


def filter_by_priority(request):
    button = request.POST['button']
    if button == 'H-L':
        context = {
            'tasks': NotCompletedTasks.objects.all(
            ).order_by('priority')
        }
    else:
        context = {
            'tasks': NotCompletedTasks.objects.all(
            ).order_by('-priority')
        }
    return render(request, 'get_tasks.html', context)


def mr_redirect(request, task_id):
    button = request.POST['button']
    if button == 'edit':
        return redirect('edit_task', task_id)
    elif button == 'delete':
        return redirect('delete_task', task_id)
    elif button == 'up' or button == 'down':
        return redirect('task_up_down', task_id, button)
    elif button == 'completed':
        return redirect('task_completed', task_id)


def update_order_tasks(task_order):
    tasks = NotCompletedTasks.objects.filter(order__gt=task_order)
    for task in tasks:
        order_update = task.order
        NotCompletedTasks.objects.filter(
            order=order_update
        ).update(order=order_update-1)
