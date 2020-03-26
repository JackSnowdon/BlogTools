from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.


@login_required
def toolshome(request):
    if request.user.profile.staff_access:
        return render(request, "toolshome.html")
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("blog_home")


@login_required
def checklist(request):
    if request.user.profile.staff_access:
        user = request.user
        profile = user.profile
        tasks = Todo.objects.filter(done_by=profile)
        return render(request, "checklist.html", {"tasks": tasks})
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("blog_home")
        

@login_required
def add_checklist(request):
    if request.user.profile.staff_access:
        if request.method == "POST":
            item = TodoForm(request.POST)
            if item.is_valid():
                unit = item.save(commit=False)
                messages.error(
                    request, "Added {0}".format(unit.task), extra_tags="alert"
                )
                user = request.user
                unit.done_by = user.profile
                unit.save()
                return redirect("checklist")
        else:
            item = TodoForm()
        return render(request, "add_check_item.html", {"item": item})
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("blog_home")


@login_required
def edit_checklist(request, pk):
    if request.user.profile.staff_access:
        this_task = get_object_or_404(Todo, pk=pk)
        if request.method == "POST":
            task_form = TodoForm(request.POST, instance=this_task)
            if task_form.is_valid():
                task = task_form.save(commit=False)
                messages.error(
                    request, "Added {0}".format(task.task), extra_tags="alert"
                )
                task.save()
                return redirect("checklist")
        else:
            task_form = TodoForm(instance=this_task)
        return render(request, "edit_check_item.html", {"task_form": task_form, "this_task": this_task })
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("blog_home")


@login_required
def delete_task(request, pk):
    if request.user.profile.staff_access:
        instance = Todo.objects.get(pk=pk)
        messages.error(
                    request, "Deleted {0}".format(instance.task), extra_tags="alert"
                )
        instance.delete()
        return redirect(reverse("checklist"))
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("blog_home")


@login_required
def complete_task(request, pk):
    if request.user.profile.staff_access:
        instance = Todo.objects.get(pk=pk)
        if instance.completed == True:
            instance.completed = False
            messages.error(
                        request, "Uncompleted {0}".format(instance.task), extra_tags="alert"
                    )
        else:
            instance.completed = True
            messages.error(
                        request, "Completed {0}".format(instance.task), extra_tags="alert"
                    )
        instance.save()
        return redirect(reverse("checklist"))
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("blog_home")