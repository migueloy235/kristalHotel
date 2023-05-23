from django.contrib import admin
from .models import *

# Register your models here.
class ArticleAdmin (admin.ModelAdmin):
    readonly_fields = ('fecha', 'actualizo')
admin.site.register(Folios, ArticleAdmin)
admin.site.register(seguridad)
admin.site.register(amallaves)
admin.site.register(empleado, )
