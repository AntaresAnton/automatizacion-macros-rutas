# informes/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Proceso, Informe
from .forms import ProcesoForm, InformeForm
from django.shortcuts import render, redirect
from .models import Proceso, Informe
from .forms import InformeForm
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Informe
import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Informe


# def index(request):
#     informes = Informe.objects.all()
#     return render(request, 'index.html', {'informes': informes})

# informes/views.py

def index(request):
    informes = Informe.objects.all()
    return render(request, 'informes/index.html', {'informes': informes})


# def anadir_informe(request):
#     if request.method == 'POST':
#         form = InformeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = InformeForm()
#     return render(request, 'informes/anadir-informe.html', {'form': form})



def anadir_informe(request):
    if request.method == 'POST':
        form = InformeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestionar_informes')
    else:
        form = InformeForm()
    
    procesos = Proceso.objects.filter(activo=True)
    context = {
        'form': form,
        'procesos': procesos,
    }
    return render(request, 'informes/anadir-informe.html', context)


# def anadir_proceso(request):
#     if request.method == 'POST':
#         form = ProcesoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = ProcesoForm()
#     # return render(request, 'anadir-proceso.html', {'form': form})
#     return render(request, 'informes/anadir-proceso.html', context)


def anadir_proceso(request):
    if request.method == 'POST':
        form = ProcesoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # or any other view you want to redirect to after saving
    else:
        form = ProcesoForm()
   
    context = {
        'form': form,
    }
    return render(request, 'informes/anadir-proceso.html', context)

def gestionar_informes(request):
    informes = Informe.objects.all()
    return render(request, 'informes/gestionar-informes.html', {'informes': informes})

# def gestionar_procesos(request):
#     procesos = Proceso.objects.all()
#     return render(request, 'informes/gestionar-procesos.html', {'procesos': procesos})



def gestionar_procesos(request):
    processes = Proceso.objects.all().order_by('orden')
    context = {
        'processes': processes
    }
    return render(request, 'informes/gestionar_procesos.html', context)



def logs(request):
    # Implementar lógica para mostrar logs
    return render(request, 'informes/logs.html')

def delete_report(request, report_id):
    # Logic to delete the report
    return JsonResponse({'status': 'success'})


def edit_process(request, process_id):
    process = get_object_or_404(Proceso, id=process_id)
    if request.method == 'POST':
        form = ProcesoForm(request.POST, instance=process)
        if form.is_valid():
            form.save()
            return redirect('gestionar_procesos')
    else:
        form = ProcesoForm(instance=process)
    return render(request, 'informes/edit_process.html', {'form': form, 'process': process})

def delete_process(request, process_id):
    process = get_object_or_404(Proceso, id=process_id)
    if request.method == 'POST':
        process.delete()
        return redirect('gestionar_procesos')
    return render(request, 'informes/delete_process_confirm.html', {'process': process})




@require_http_methods(["POST"])
def edit_informe(request, informe_id):
    data = json.loads(request.body)
    informe = Informe.objects.get(id=informe_id)
    
    # Update the informe fields
    informe.nombre = data.get('nombre', informe.nombre)
    informe.proceso_id = data.get('proceso', informe.proceso_id)
    informe.workflow = data.get('workflow', informe.workflow)
    informe.macro = data.get('macro', informe.macro)
    informe.source_path = data.get('source_path', informe.source_path)
    informe.destination_path = data.get('destination_path', informe.destination_path)
    informe.email_recipients = data.get('email_recipients', informe.email_recipients)
    informe.email_message = data.get('email_message', informe.email_message)
    informe.is_sequential = data.get('is_sequential', informe.is_sequential)
    
    informe.save()
    
    return JsonResponse({'status': 'success'})




@require_http_methods(["POST"])
def delete_informe(request, informe_id):
    try:
        informe = Informe.objects.get(id=informe_id)
        informe.delete()
        return JsonResponse({'status': 'success'})
    except Informe.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Informe not found'}, status=404)
