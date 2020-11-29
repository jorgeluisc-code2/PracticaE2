from django.contrib import admin

from .models import Distrito,Institucion,TipoInstitucion,Provincia,Departamento
admin.site.register(Distrito)
admin.site.register(Institucion)
admin.site.register(TipoInstitucion)
admin.site.register(Provincia)
admin.site.register(Departamento)

