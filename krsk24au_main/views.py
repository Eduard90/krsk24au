from django.shortcuts import render_to_response, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import request, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth import logout

# Create your views here.
@login_required
def index(request):
    # request.session['django_language'] = 'ru'
    if request.user.is_authenticated():
    # template_name = 'krsk24au_main/index.html'
       return render_to_response('krsk24au_main/index.html')

# def auth(request):
#     form = AuthenticationForm()
#     return render_to_response('krsk24au_main/auth.html', {'form': forms.FormWrapper(form)})

def logoutview(request):
    logout(request)
    return redirect("/")
    # return HttpResponse("Logout")
    #redirect("/")