from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
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


@login_required
def account(request):
    if request.user.profile.staff_access:
        user = request.user
        profile = user.profile
        items = AccountItem.objects.filter(done_by=profile).order_by('-amount')
        income_total = 0
        expense_total = 0
        for i in items:
            if i.expense == True:
                expense_total += i.amount
            else:
                income_total += i.amount
        balance = (income_total - expense_total)
        extras = ExtraItem.objects.filter(done_by=profile).order_by('-amount')
        extra_total = 0
        for e in extras:
            extra_total += e.amount
        remaining = (balance - extra_total)
        return render(request, "account.html", {"items": items, "income_total": income_total, 
        "expense_total": expense_total, "balance": balance, "extras": extras, "extra_total": extra_total,
        "remaining": remaining})
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("blog_home")
        

@login_required
def add_account_item(request):
    if request.user.profile.staff_access:
        if request.method == "POST":
            item_form = AccountForm(request.POST)
            if item_form.is_valid():
                item = item_form.save(commit=False)
                messages.error(
                    request, "Added {0}".format(item.item), extra_tags="alert"
                )
                user = request.user
                item.done_by = user.profile
                item.created_on = datetime.now()
                item.save()
                return redirect("account")
        else:
            item_form = AccountForm()
        return render(request, "add_account_item.html", {"item_form": item_form})
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("blog_home")


@login_required
def view_account_item(request, pk):
    if request.user.profile.staff_access:
        item = get_object_or_404(AccountItem, pk=pk)
        return render(request, "view_account_item.html", {"item": item})
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("blog_home")


@login_required
def edit_account_item(request, pk):
    if request.user.profile.staff_access:
        this_item = get_object_or_404(AccountItem, pk=pk)
        if request.method == "POST":
            item_form = AccountForm(request.POST, instance=this_item)
            if item_form.is_valid():
                item = item_form.save(commit=False)
                messages.error(
                    request, "Added {0}".format(item.item), extra_tags="alert"
                )
                item.save()
                return redirect("account")
        else:
            item_form = AccountForm(instance=this_item)
        return render(request, "edit_account_item.html", {"item_form": item_form, "this_item": this_item })
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("blog_home")


@login_required
def delete_account_item(request, pk):
    if request.user.profile.staff_access:
        this_item = get_object_or_404(AccountItem, pk=pk)
        messages.error(
                    request, "Deleted {0}".format(this_item.item), extra_tags="alert"
                )
        this_item.delete()
        return redirect(reverse("account"))
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("blog_home")


@login_required
def add_extra_item(request):
    if request.user.profile.staff_access:
        if request.method == "POST":
            item_form = ExtraItemForm(request.POST)
            if item_form.is_valid():
                item = item_form.save(commit=False)
                messages.error(
                    request, "Added Extra {0}".format(item.item), extra_tags="alert"
                )
                user = request.user
                item.done_by = user.profile
                item.created_on = datetime.now()
                item.save()
                return redirect("account")
        else:
            item_form = ExtraItemForm()
        return render(request, "add_extra_item.html", {"item_form": item_form})
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("blog_home")


@login_required
def view_extra_item(request, pk):
    if request.user.profile.staff_access:
        item = get_object_or_404(ExtraItem, pk=pk)
        return render(request, "view_extra_item.html", {"item": item})
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("blog_home")


@login_required
def edit_extra_item(request, pk):
    if request.user.profile.staff_access:
        this_item = get_object_or_404(ExtraItem, pk=pk)
        if request.method == "POST":
            item_form = ExtraItemForm(request.POST, instance=this_item)
            if item_form.is_valid():
                item = item_form.save(commit=False)
                messages.error(
                    request, "Edit Extra {0}".format(item.item), extra_tags="alert"
                )
                item.save()
                return redirect("account")
        else:
            item_form = ExtraItemForm(instance=this_item)
        return render(request, "edit_extra_item.html", {"item_form": item_form})
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("blog_home")


@login_required
def delete_extra_item(request, pk):
    if request.user.profile.staff_access:
        this_item = get_object_or_404(ExtraItem, pk=pk)
        messages.error(
                    request, "Deleted {0}".format(this_item.item), extra_tags="alert"
                )
        this_item.delete()
        return redirect(reverse("account"))
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("blog_home")