from django.shortcuts import render_to_response, redirect, render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import request, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth import logout
from krsk24au_main.forms import AuthForm
from django.template import RequestContext

# Create your views here.
@login_required
def index(request):
    # request.session['django_language'] = 'ru'
    context_instance=RequestContext(request)
    if request.user.is_authenticated():
       return render_to_response('krsk24au_main/index.html', {}, context_instance=RequestContext(request))

# def auth(request):
#     form = AuthenticationForm()
#     return render_to_response('krsk24au_main/auth.html', {'form': forms.FormWrapper(form)})

def loginview(request):
    form = AuthForm()
    return render_to_response('krsk24au_main/auth.html', {'form': form}, context_instance=RequestContext(request))

@login_required
def logoutview(request):
    logout(request)
    return redirect("/")