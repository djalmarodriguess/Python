def notas(*n, sit=False):
    r = dict()
    r['Quantidade'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['Situação'] = 'MUITO BEM'
        elif r['media'] >= 5:
            r['Situação'] = 'RAZOAVEL'
        else:
            r['Situação'] = 'MUITO RUIM'
    return r

resp = notas( 8.6, 9.1, sit=True)
print(resp)