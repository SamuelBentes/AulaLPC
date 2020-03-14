from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField('Nome',max_length = 40, null = True, blank = True)
    email = models.EmailField('Email')

    def __str__(self):
        return self.nome

class PessoaFisica(Pessoa):
    cpf = models.CharField('CPF',max_length = 14, null = True, blank = True)

    def __str__(self):
        return self.cpf

class Evento(models.Model):
    nome = models.CharField('Nome',max_length = 40, null = True, blank = True)
    sigla = models.CharField('Sigla',max_length = 5, null = True, blank = True)
    data_inicio = models.DateField('Data Inicio')
    descrição = models.TextField('Descrição')

    def __str__(self):
        return self.nome

class Ingresso(models.Model):
    descrição = models.CharField('Descrição',max_length = 40, null = True, blank = True)
    valor = models.FloatField('Valor',max_length = 6, null = True, blank = True)
    evento = models.ForeignKey(Evento, on_delete = models.CASCADE,related_name = 'Evento', blank = True, null = True)

    def __str__(self):
        return self.descrição

class Inscrição(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete = models.CASCADE, verbose_name = 'Pessoa', blank = True, null = True)
    evento = models.ForeignKey(Evento, on_delete = models.CASCADE, verbose_name = 'Evento', blank = True, null = True)
    ingresso = models.ForeignKey(Ingresso, on_delete = models.CASCADE, verbose_name = 'Ingresso', blank = True, null = True)

    def __str__(self):
        return 'Inscrição Realizada'