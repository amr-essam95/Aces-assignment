from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .forms import UserForm
from django.contrib.auth import authenticate, login


def index(request):
    return render(request,'aces/login.html',{})



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return render(request, 'aces/aces1.html', {'user':user})
            else:
                return render(request, 'aces/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'aces/login.html', {'error_message': 'Invalid login'})
    return render(request, 'aces/login.html')

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                context={'username':user}
                return render(request, 'aces/aces1.html', context)
    context = {
        "form": form,
    }
    return render(request, 'aces/register.html', context)

