'''Programa do curso de Engenharia Civil.
   Materia de Estradas'''

from math import sqrt

e = float(input('E: '))
bf = float(input('bf: '))
fy = float(input('fy: '))
zx = float(input('Zx: '))
tf = float(input('tf: '))
fr = float(input('fr: '))
wx = float(input('wx: '))
h = float(input('h: '))
tw = float(input('tw: '))
ry = float(input('ry: '))
cb = float(input('cb: '))
rt = float(input('rt: '))
d = float(input('d: '))
lb = float(input('lb: ')) # medida de uma ponta até um proximo apoio
print('-='*30)

#MPL
Mpl = zx*10**-6 * fy*10**3
print(f'Momento de Platificação = Mpl = {zx}*{fy} = {Mpl:.2f}kNm')

#FLM
print('-='*30)
print('FLM')
print('-='*30)

lambida = bf/(2*tf)
lambida_p = 0.38*(sqrt(e*10**3/fy))
print(f'lambida = {bf}/2x{tf} = {lambida:.2f}')
print(f'lambida_p = 0.38x rais{e}/{fy} = {lambida_p:.2f}')

print('-='*30)

tipo = str(input('O perfil é soldado,[S/N]:')).upper()[0]
if tipo == 'S':
     #Perfil Soldado
    lambida_r1 = 0.62*(sqrt(e*10**3/(fy-fr)))
    print(f'lambida_r1 = Perfil Soldado= 0,62xraiz{e}/{fy}-{fr} {lambida_r1:.2f}')

    print('-=' * 30)

else:
    #Perfil Laminado
    lambida_r2 = 0.82*(sqrt(e*10**3/(fy-fr)))
    print(f'lambida_r2 = Perfil Laminado= 0,82xraiz{e}/{fy}-{fr} = {lambida_r2:.2f}')

    print('-='*30)

Mr = ((wx/10) * ((fy/10) - (fr/10)))/10
print(f'Mr = {wx} x ({fy}-{fr}) = {Mr:.2f}KNm')

lambida_r2 = 0.82 * (sqrt(e * 10 ** 3 / (fy - fr)))
lambida_r1 = 0.62*(sqrt(e*10**3/(fy-fr)))
if lambida_p < lambida < lambida_r1 and lambida_r2:
    Mn = Mpl - ((lambida - lambida_p)/(lambida_r1 - lambida_p)) * (Mpl - Mr)
    print(f'Mn = {Mn:.2f}KNm')

    print('-='*30)

elif lambida <= lambida_p:
    Mn = Mpl

#FLA
print('FLA')
print('-='*30)
lambida_1 = h/tw
lambida_p1 = 3.5*(sqrt(e*10**3/fy))
lambida_r3 = 5.6 * (sqrt(e * 10 ** 3 / fy))
print(f'lambida FLA = {lambida_1:.2f}')
print(f'lambida_p de FLA = {lambida_p1:.2f}')
print(f'lambida_r de FLA = {lambida_r3:.2f}')

Mr_1 = Mr = ((wx/10) * (fy/10)) / 10
print(f'Mr de FLA = {Mr_1:.2f}kNm')

if lambida_1 <= lambida_p1:
    print(f'Mn = Mpl = {Mpl:.2f}')
    print('-=' * 30)

elif lambida_p1 < lambida_1 < lambida_r3:
    Mn = Mpl - ((lambida_1 - lambida_p1) / (lambida_r3 - lambida_p1)) * (Mpl - Mr_1)
    print(f'Mn = {Mn:.2f}KNm')
print('-='*30)

#FLT
print('FLT')
print('-='*30)

lp = (1.75 * ry * (sqrt(e*10**3/fy)))/100
print(f'Lp = {lp:.2f}m')

x1 = (40.75/(cb*e*10**3)) * ((fy/10) - (fr/10))
a = ((rt * (d/10))/((bf/10) * (tf/10)))**2
x = x1*a*10
print(f'X = {x:.3f}')

rais = sqrt(1+x**2)
Lr = (((19.9 * (rt**2) * (d/10)/((bf/10) * (tf/10)))/x) * sqrt(1+rais))/100
print(f'Lr = {Lr:.2f}m')

Mr = ((wx/10) * ((fy/10) - (fr/10)))/10
print(f'Mr = {wx} x ({fy}-{fr}) = {Mr:.2f}KNm')

if lb < lp:
    Mn = Mpl
    print(f'Seção compacta = Mn = Mpl = {Mpl:.2f}kNm')

else:
    Mn_1 = Mpl - ((Mpl - Mr)/(Lr - lp)) * (lb - lp)
    print(f'Mn = {Mn_1:.2f}kNm')

print('-='*30)

#Flecha
print('Flecha')
Mn_2 = 1.25 * (fy/10) * (wx/10)
print(f'Mn da Flecha = {Mn_2/10:.2f}kNm')

print('-='*30)

#Resistenci ao ao momento fletor
print('Resistenciao ao momento fletor')
if lb < lp:
    Md = 0.9 * Mpl
    print(f'Md = {Md:.2f}kNm')

else:
    Md = 0.9 * Mn_1
    print(f'Md = {Md:.2f}kNm')






