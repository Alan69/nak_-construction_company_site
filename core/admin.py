from django.contrib import admin
from .models import Service, Project, Blog
# Register your models here.

admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Blog)