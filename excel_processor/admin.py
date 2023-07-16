from django.contrib import admin
from .models import Kit_data,\
                    Kit,\
                    Modulo,\
                    Inversor,\
                    Cabo,\
                    Pares,\
                    Stringbox,\
                    Estrutura

admin.site.register(Kit_data)
admin.site.register(Kit)
admin.site.register(Modulo)
admin.site.register(Inversor)
admin.site.register(Cabo)
admin.site.register(Pares)
admin.site.register(Stringbox)
admin.site.register(Estrutura)