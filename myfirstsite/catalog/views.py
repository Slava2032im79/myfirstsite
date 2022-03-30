from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm, EditTaskDescriptionForm, ReviewForm, LoginForm, RegisterForm
from .models import Task, Review
from django.shortcuts import render
from .forms import ImageForm


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task.objects.create(**form.cleaned_data)
            return redirect('task_detail', task.id)
    else:
        form = TaskForm()
        return render(request, 'catalog/form.html', {'form': form})


@login_required
def edit_task(request, task_id):
    if request.method == 'POST':
        form = EditTaskDescriptionForm(request.POST)
        if form.is_valid():
            task = get_object_or_404(Task, pk=task_id)
            task.description = form.cleaned_data["description"]
            task.save()
            return redirect('task_detail', task.id)
    else:
        form = EditTaskDescriptionForm()
        return render(request, 'catalog/form.html', {'form': form})


@login_required
def edit_task(request, task_id):
    if request.method == 'POST':
        form = EditTaskDescriptionForm(request.POST)
        if form.is_valid():
            task = get_object_or_404(Task, pk=task_id)
            task.description = form.cleaned_data["description"]
            task.save()
            return redirect('task_detail', task.id)
    else:
        form = EditTaskDescriptionForm()
        return render(request, 'catalog/form.html', {'form': form})


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    user = request.user
    if review.user == user:
        review.delete()
        return redirect('task_review_list', review.task.id)
    return HttpResponse('You can delete only your reviews!')


@login_required
def edit_review(request, review_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            user = request.user
            review = get_object_or_404(Review, pk=review_id)
            if review.user == user:
                review.text = form.cleaned_data["text"]
                review.save()
                return redirect('task_review_list', review.task.id)
            return HttpResponse('You can edit only your reviews!')
    else:
        form = ReviewForm()
        return render(request, 'catalog/form.html', {'form': form})


def index(request):
    return render(request, 'catalog/index.html')


def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'catalog/task_detail.html', {'task': task})


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'catalog/task_list.html', {'tasks': tasks})


def review_detail(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    return render(request, 'catalog/review_detail.html', {'review': review})


def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'catalog/review_list.html', {'reviews': reviews})


def task_review_list(request, task_id):
    reviews = Review.objects.filter(task=task_id)
    return render(request, 'catalog/review_list.html', {'reviews': reviews})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("index")
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'catalog/form.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect("index")


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("login_user")
        else:
            return HttpResponse('Invalid registration')
    else:
        form = RegisterForm()

        return render(request, "catalog/form.html", {"form": form})


def add_review():
    return None



def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})