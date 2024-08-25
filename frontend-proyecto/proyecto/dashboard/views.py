from django import render
from django.shortcuts import render, redirect
from .models import Process, Report
from .forms import ReportForm

def index(request):
    return render(request, 'dashboard/index.html')

def anadir_informe(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReportForm()
    
    processes = Process.objects.all()
    return render(request, 'dashboard/anadir_informe.html', {'form': form, 'processes': processes})
    # return render(request, 'dashboard/anadir_informe.html')


def anadir_proceso(request):
    return render(request, 'dasboard/anadir_proceso.html')

def gestionar_informe(request):
    return render(request, 'dashboard/gestionar_informe.html')

def gestionar_proceso(request):
    return render(request, 'dashboard/gestionar_proceso.html')

def log(request):
    return render(request, 'dashboard/log.html')
