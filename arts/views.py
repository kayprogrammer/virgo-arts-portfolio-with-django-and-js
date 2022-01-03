from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import *
from . forms import *

# Create your views here.

def home(request):
    arts = Art.objects.all().order_by('-date_created')
    virg = Virgo.objects.all()
    about = About.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'arts':arts, 'virg':virg, 'about': about, 'form':form}

    if request.is_ajax():
            
        html = render_to_string('arts/contact_form.html', context, request=request)
        return JsonResponse({'form': html})


    return render(request, 'arts/index.html', context)
