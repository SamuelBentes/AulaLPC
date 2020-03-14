from django.contrib import admin
from .models import Pessoa
from .models import Evento
from .models import Ingresso
from .models import Inscrição
from .models import PessoaFisica

# Register your models here.

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    pass

@admin.register(Ingresso)
class IngressoAdmin(admin.ModelAdmin):
    pass

@admin.register(Inscrição)
class InscriçãoAdmin(admin.ModelAdmin):
    pass

@admin.register(PessoaFisica)
class PessoaFisicaAdmin(admin.ModelAdmin):
    pass
