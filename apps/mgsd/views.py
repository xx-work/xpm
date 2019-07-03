from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
try:
    from django.core.urlresolvers import reverse
except:
    from django.urls import reverse
# Create your views here.


def homepage(request):
    return HttpResponseRedirect(reverse('dashboard'))


def dashboard(request):
    return render(request, 'cso/index.html')