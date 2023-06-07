from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Departement)
admin.site.register(Arrondissement)
admin.site.register(Ville)
admin.site.register(Quartier)
admin.site.register(Adresse)