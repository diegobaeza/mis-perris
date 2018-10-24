from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Region)
admin.site.register(Estado)
admin.site.register(TipoUsuario)
admin.site.register(TipoVivienda)
admin.site.register(Rescatado)
admin.site.register(Ciudad)
admin.site.register(Usuario)
admin.site.register(RegistroAdopcion)

