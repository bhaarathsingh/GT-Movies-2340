from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    return render(request, 'home.html', {'user': request.user})
def index(request):
    template_data = {}
    template_data['title'] = 'Movies Store'
    return render(request, "home/index.html", {'template_data': template_data})
def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, "home/about.html", {'template_data': template_data})
