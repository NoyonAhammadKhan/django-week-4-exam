from django.shortcuts import render, redirect
from categories_app.forms import CategoryForm
from categories_app.models import Category
# Create your views here.


def create_category(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('show_tasks')
    else:
        category_form = CategoryForm()
    return render(request, 'add_category.html', {'form': category_form})


def update_category(request, id):
    category = Category.objects.get(pk=id)
    category_form = CategoryForm(instance=category)
    if request.method == 'POST':
        category_form = CategoryForm(request.POST, instance=category)
        if category_form.is_valid():
            category_form.save()
            return redirect('home.html')
    return render(request, 'update_category.html', {'form': category_form})
