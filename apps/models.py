class technicalReserve(object):
    def __init__(self, data, nivel, tipo, conta, reduzido, descricao, anterior, debito, credito, movimento, saldoAtual):
        self.data = data
        self.nivel = nivel
        self.tipo = tipo
        self.conta = conta
        self.reduzido = reduzido
        self.descricao = descricao
        self.anterior = anterior
        self.debito = debito
        self.credito = credito
        self.movimento = movimento
        self.saldoAtual = saldoAtual 

    def to_dict(self):
        data = {}
        data['data'] = self.data
        data['nivel'] = self.nivel
        data['tipo'] = self.tipo
        data['conta'] = self.conta
        data['reduzido'] = self.reduzido
        data['descricao'] = self.descricao
        data['anterior'] = self.anterior
        data['debito'] = self.debito
        data['credito'] = self.credito
        data['movimento'] = self.movimento
        data['saldoAtual'] = self.saldoAtual

        return data

    def from_dict(self, data):
        self.data = data['data'] 
        self.nivel = data['nivel']
        self.tipo = data['tipo']
        self.conta = data['conta']
        self.reduzido = data['reduzido'] 
        self.descricao = data['descricao']
        self.anterior = data['anterior']
        self.debito = data['debito']
        self.credito = data['credito']
        self.movimento = data['movimento']
        self.saldoAtual = data['saldoAtual']
    

class insuranceIndicators(object):
    def __init__(self, data, nivel, tipo, conta, reduzido, descricao, anterior, debito, credito, movimento, saldoAtual):
        self.data = data
        self.nivel = nivel
        self.tipo = tipo
        self.conta = conta
        self.reduzido = reduzido
        self.descricao = descricao
        self.anterior = anterior
        self.debito = debito
        self.credito = credito
        self.movimento = movimento
        self.saldoAtual = saldoAtual

    def to_dict(self):
        data = {}
        data['data'] = self.data
        data['nivel'] = self.nivel
        data['tipo'] = self.tipo
        data['conta'] = self.conta
        data['reduzido'] = self.reduzido
        data['descricao'] = self.descricao
        data['anterior'] = self.anterior
        data['debito'] = self.debito
        data['credito'] = self.credito
        data['movimento'] = self.movimento
        data['saldoAtual'] = self.saldoAtual

        return data

    def from_dict(self, data):
        self.data = data['data'] 
        self.nivel = data['nivel']
        self.tipo = data['tipo']
        self.conta = data['conta']
        self.reduzido = data['reduzido'] 
        self.descricao = data['descricao']
        self.anterior = data['anterior']
        self.debito = data['debito']
        self.credito = data['credito']
        self.movimento = data['movimento']
        self.saldoAtual = data['saldoAtual']


class assets(object):
    def __init__(self, data, nivel, tipo, conta, reduzido, descricao, anterior, debito, credito, movimento, saldoAtual):
        self.data = data
        self.nivel = nivel
        self.tipo = tipo
        self.conta = conta
        self.reduzido = reduzido
        self.descricao = descricao
        self.anterior = anterior
        self.debito = debito
        self.credito = credito
        self.movimento = movimento
        self.saldoAtual = saldoAtual

    def to_dict(self):
        data = {}
        data['data'] = self.data
        data['nivel'] = self.nivel
        data['tipo'] = self.tipo
        data['conta'] = self.conta
        data['reduzido'] = self.reduzido
        data['descricao'] = self.descricao
        data['anterior'] = self.anterior
        data['debito'] = self.debito
        data['credito'] = self.credito
        data['movimento'] = self.movimento
        data['saldoAtual'] = self.saldoAtual

        return data

    def from_dict(self, data):
        self.data = data['data'] 
        self.nivel = data['nivel']
        self.tipo = data['tipo']
        self.conta = data['conta']
        self.reduzido = data['reduzido'] 
        self.descricao = data['descricao']
        self.anterior = data['anterior']
        self.debito = data['debito']
        self.credito = data['credito']
        self.movimento = data['movimento']
        self.saldoAtual = data['saldoAtual']


class liabilities(object):
    def __init__(self, data, nivel, tipo, conta, reduzido, descricao, anterior, debito, credito, movimento, saldoAtual):
        self.data = data
        self.nivel = nivel
        self.tipo = tipo
        self.conta = conta
        self.reduzido = reduzido
        self.descricao = descricao
        self.anterior = anterior
        self.debito = debito
        self.credito = credito
        self.movimento = movimento
        self.saldoAtual = saldoAtual

    def to_dict(self):
        data = {}
        data['data'] = self.data
        data['nivel'] = self.nivel
        data['tipo'] = self.tipo
        data['conta'] = self.conta
        data['reduzido'] = self.reduzido
        data['descricao'] = self.descricao
        data['anterior'] = self.anterior
        data['debito'] = self.debito
        data['credito'] = self.credito
        data['movimento'] = self.movimento
        data['saldoAtual'] = self.saldoAtual

        return data

    def from_dict(self, data):
        self.data = data['data'] 
        self.nivel = data['nivel']
        self.tipo = data['tipo']
        self.conta = data['conta']
        self.reduzido = data['reduzido'] 
        self.descricao = data['descricao']
        self.anterior = data['anterior']
        self.debito = data['debito']
        self.credito = data['credito']
        self.movimento = data['movimento']
        self.saldoAtual = data['saldoAtual']


class resultDemonstration(object):
    def __init__(self, data, nivel, tipo, conta, reduzido, descricao, anterior, debito, credito, movimento, saldoAtual):
        self.data = data
        self.nivel = nivel
        self.tipo = tipo
        self.conta = conta
        self.reduzido = reduzido
        self.descricao = descricao
        self.anterior = anterior
        self.debito = debito
        self.credito = credito
        self.movimento = movimento
        self.saldoAtual = saldoAtual

    def to_dict(self):
        data = {}
        data['data'] = self.data
        data['nivel'] = self.nivel
        data['tipo'] = self.tipo
        data['conta'] = self.conta
        data['reduzido'] = self.reduzido
        data['descricao'] = self.descricao
        data['anterior'] = self.anterior
        data['debito'] = self.debito
        data['credito'] = self.credito
        data['movimento'] = self.movimento
        data['saldoAtual'] = self.saldoAtual

        return data

    def from_dict(self, data):
        self.data = data['data'] 
        self.nivel = data['nivel']
        self.tipo = data['tipo']
        self.conta = data['conta']
        self.reduzido = data['reduzido'] 
        self.descricao = data['descricao']
        self.anterior = data['anterior']
        self.debito = data['debito']
        self.credito = data['credito']
        self.movimento = data['movimento']
        self.saldoAtual = data['saldoAtual']


class administrativeExpense(object):
    def __init__(self, data, nivel, tipo, conta, reduzido, descricao, anterior, debito, credito, movimento, saldoAtual):
        self.data = data
        self.nivel = nivel
        self.tipo = tipo
        self.conta = conta
        self.reduzido = reduzido
        self.descricao = descricao
        self.anterior = anterior
        self.debito = debito
        self.credito = credito
        self.movimento = movimento
        self.saldoAtual = saldoAtual

    def to_dict(self):
        data = {}
        data['data'] = self.data
        data['nivel'] = self.nivel
        data['tipo'] = self.tipo
        data['conta'] = self.conta
        data['reduzido'] = self.reduzido
        data['descricao'] = self.descricao
        data['anterior'] = self.anterior
        data['debito'] = self.debito
        data['credito'] = self.credito
        data['movimento'] = self.movimento
        data['saldoAtual'] = self.saldoAtual

        return data

    def from_dict(self, data):
        self.data = data['data'] 
        self.nivel = data['nivel']
        self.tipo = data['tipo']
        self.conta = data['conta']
        self.reduzido = data['reduzido'] 
        self.descricao = data['descricao']
        self.anterior = data['anterior']
        self.debito = data['debito']
        self.credito = data['credito']
        self.movimento = data['movimento']
        self.saldoAtual = data['saldoAtual']


class financialExpense(object):
    def __init__(self, data, nivel, tipo, conta, reduzido, descricao, anterior, debito, credito, movimento, saldoAtual):
        self.data = data
        self.nivel = nivel
        self.tipo = tipo
        self.conta = conta
        self.reduzido = reduzido
        self.descricao = descricao
        self.anterior = anterior
        self.debito = debito
        self.credito = credito
        self.movimento = movimento
        self.saldoAtual = saldoAtual

    def to_dict(self):
        data = {}
        data['data'] = self.data
        data['nivel'] = self.nivel
        data['tipo'] = self.tipo
        data['conta'] = self.conta
        data['reduzido'] = self.reduzido
        data['descricao'] = self.descricao
        data['anterior'] = self.anterior
        data['debito'] = self.debito
        data['credito'] = self.credito
        data['movimento'] = self.movimento
        data['saldoAtual'] = self.saldoAtual

        return data

    def from_dict(self, data):
        self.data = data['data'] 
        self.nivel = data['nivel']
        self.tipo = data['tipo']
        self.conta = data['conta']
        self.reduzido = data['reduzido'] 
        self.descricao = data['descricao']
        self.anterior = data['anterior']
        self.debito = data['debito']
        self.credito = data['credito']
        self.movimento = data['movimento']
        self.saldoAtual = data['saldoAtual']


class taxExpense(object):
    def __init__(self, data, nivel, tipo, conta, reduzido, descricao, anterior, debito, credito, movimento, saldoAtual):
        self.data = data
        self.nivel = nivel
        self.tipo = tipo
        self.conta = conta
        self.reduzido = reduzido
        self.descricao = descricao
        self.anterior = anterior
        self.debito = debito
        self.credito = credito
        self.movimento = movimento
        self.saldoAtual = saldoAtual

    def to_dict(self):
        data = {}
        data['data'] = self.data
        data['nivel'] = self.nivel
        data['tipo'] = self.tipo
        data['conta'] = self.conta
        data['reduzido'] = self.reduzido
        data['descricao'] = self.descricao
        data['anterior'] = self.anterior
        data['debito'] = self.debito
        data['credito'] = self.credito
        data['movimento'] = self.movimento
        data['saldoAtual'] = self.saldoAtual

        return data

    def from_dict(self, data):
        self.data = data['data'] 
        self.nivel = data['nivel']
        self.tipo = data['tipo']
        self.conta = data['conta']
        self.reduzido = data['reduzido'] 
        self.descricao = data['descricao']
        self.anterior = data['anterior']
        self.debito = data['debito']
        self.credito = data['credito']
        self.movimento = data['movimento']
        self.saldoAtual = data['saldoAtual']

