from django.db import models

class Process(models.Model):
    name = models.CharField(max_length=100)

class Report(models.Model):
    process = models.ForeignKey(Process, on_delete=models.CASCADE)
    use_workflow = models.BooleanField(default=False)
    workflow_name = models.CharField(max_length=200, blank=True)
    use_macro = models.BooleanField(default=False)
    macro_path = models.CharField(max_length=200, blank=True)
    use_copy = models.BooleanField(default=False)
    source_path = models.CharField(max_length=200, blank=True)
    destination_path = models.CharField(max_length=200, blank=True)
    use_email = models.BooleanField(default=False)
    email_recipients = models.TextField(blank=True)
    email_message = models.TextField(blank=True)
    is_sequential = models.BooleanField(default=True)
