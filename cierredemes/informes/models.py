from django.db import models

# class Proceso(models.Model):
#     nombre = models.CharField(max_length=255)
#     descripcion = models.TextField(blank=True, null=True)
#     orden = models.PositiveIntegerField()
#     activo = models.BooleanField(default=True)

#     def __str__(self):
#         return self.nombre
    

class Proceso(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    orden = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


    
# class Informe(models.Model):
#     nombre = models.CharField(max_length=255)
#     proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)
#     workflow = models.CharField(max_length=255, blank=True, null=True)
#     macro_path = models.CharField(max_length=255, blank=True, null=True)
#     source_path = models.CharField(max_length=255, blank=True, null=True)
#     destination_path = models.CharField(max_length=255, blank=True, null=True)
#     email_recipients = models.TextField(blank=True, null=True)
#     email_message = models.TextField(blank=True, null=True)
#     secuencial = models.BooleanField(default=True)

#     def __str__(self):
#         return self.nombre



class Informe(models.Model):
    proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    workflow = models.CharField(max_length=255, blank=True, null=True)
    macro = models.CharField(max_length=255, blank=True, null=True)
    source_path = models.CharField(max_length=255, blank=True, null=True)
    destination_path = models.CharField(max_length=255, blank=True, null=True)
    email_recipients = models.TextField(blank=True, null=True)
    email_message = models.TextField(blank=True, null=True)
    is_sequential = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
