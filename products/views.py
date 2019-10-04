from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils.timezone import localtime, now
from django.contrib.auth.decorators import login_required
from .models import Products
from django.http import HttpResponse


def home(request):
    products = Products.objects
    return render(request, 'home.html', {'products': products})


@login_required(login_url="/accounts/signup/")
def create(request):
    if request.method == 'POST':
        products = Products()
        products.title = request.POST['title']
        products.body = request.POST['body']
        products.url = request.POST['url']
        products.image = request.FILES['image']
        products.icon = request.FILES['icon']
        products.hunter = request.user
        products.pub_date = localtime(now())
        products.save()
        return redirect('/products/' + str(products.id))
    else:
        return render(request, 'create.html')


def detail(request, products_id):
    products = get_object_or_404(Products, pk=products_id)
    return render(request, 'detail.html', {'products': products})


@login_required()
def upvote(request, products_id):
    if request.method == 'POST':
        products = get_object_or_404(Products, pk=products_id)
        products.votes_total = products.votes_total + 1
        products.save()
        return redirect('/products/' + str(products.id))
