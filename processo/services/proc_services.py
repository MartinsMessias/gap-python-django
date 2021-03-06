import os

from GProcessos import settings
from ..models import *


def cadastrar_processo(new):
    Processo.objects.create(
        numero_processo=new.numero_processo, protocolo_processo=new.protocolo_processo,
        nome_parte_processo=new.nome_parte_processo, assunto_processo=new.assunto_processo,
        data_abertura_processo=new.data_abertura_processo, numero_caixa_processo=new.numero_caixa_processo,
        divisao_processo=new.divisao_processo, tipo_processo=new.tipo_processo, arquivo_processo=new.arquivo_processo
    )


def busca_processo(id):
    processo = Processo.objects.get(id=id)
    return processo


def remover_processo(processo):
    processo.delete()
    try:
        os.remove(os.path.join(settings.MEDIA_ROOT, processo.arquivo_processo.name))
    except:
        pass


def editar_processo(processo_ant, new):
    processo_ant.numero_processo = new.numero_processo
    processo_ant.protocolo_processo = new.protocolo_processo
    processo_ant.nome_parte_processo = new.nome_parte_processo
    processo_ant.assunto_processo = new.assunto_processo
    processo_ant.data_abertura_processo = new.data_abertura_processo
    processo_ant.numero_caixa_processo = new.numero_caixa_processo
    processo_ant.divisao_processo = new.divisao_processo
    processo_ant.tipo_processo = new.tipo_processo
    processo_ant.arquivo_processo = new.arquivo_processo
    processo_ant.save(force_update=True)


def verificar_exist_numproc(nume_proc):
    try:
        if Processo.objects.get(numero_processo=nume_proc):
            return True
    except:
        return False


def verificar_exist_numprot(nume_prot):
    try:
        if Processo.objects.get(numero_processo=nume_prot):
            return True
    except:
        return False


def verificar_exist_pro_div(div):
    try:
        if Processo.objects.get(divisao_processo=div):
            return True
    except:
        return False


def verificar_exist_pro_tipo(tipo):
    try:
        if Processo.objects.get(tipo_processo=busca_tipo(tipo)):
            return True
    except:
        return False


def verificar_exist_div(div):
    try:
        tipo_a = str(div).upper().replace(" ", "")
        tipo_b = Divisao.objects.all().only('nome_divisao')

        for value in tipo_b:
            b = str(value).upper().replace(" ", "")

            if tipo_a == b:
                return True
    except:
        return False


def verificar_exist_tipo(tipo):
    try:
        tipo_a = str(tipo).upper().replace(" ", "")
        tipo_b = TipoDeProcesso.objects.all().only('nome_tipo')

        for value in tipo_b:
            b = str(value).upper().replace(" ", "")

            if tipo_a == b:
                return True
    except:
        return False


def editar_divisao(div_ant, new):
    div_ant.nome_divisao = new.nome_divisao
    div_ant.save(force_update=True)


def busca_div(id):
    div = Divisao.objects.get(id=id)
    return div


def remover_divisao(divisao):
    divisao.delete()


def cadastrar_div(new):
    Divisao.objects.create(nome_divisao=new.nome_divisao)


def editar_tipo(tipo_ant, new):
    tipo_ant.nome_tipo = new.nome_tipo
    tipo_ant.save(force_update=True)


def busca_tipo(id):
    tipo = TipoDeProcesso.objects.get(id=id)
    return tipo


def remover_tipo(tipo):
    busca_tipo(tipo).delete()


def cadastrar_tipo(new):
    TipoDeProcesso.objects.create(nome_tipo=new.nome_tipo)
