from .models import Proceso

def global_processes(request):
    return {
        'processes': Proceso.objects.filter(activo=True).order_by('orden')
    }
