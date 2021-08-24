'''Primeira coisa, trocar o valor do 'delta'
Depois colocar para rodar e informar os valor de 'RC', 'V','Primeiro ponto da estaca 01' e 'segundo ponto da estaca 01'.'''

from math import pi
import math

def grau( grau, minuto , segundo):
    n = grau + ((minuto * (1 / 60)) + (segundo * (1 / 3600)))
    return n

media = 0
delta = grau(40, 00, 00)
rc = float(input('Valor raio circular:rc: '))
print(delta)
v = float(input('v: '))
est1 = float(input('Primeiro valor da estaca:est1: '))
est2 = float(input('Segundo valor da estaca:est2: '))
n = 3.5
b = 6
print(f'Estaca {est1} + {est2}')
print('-='*20)

print('#01 Comprimento do trecho em espiral')
lsmin = 0.036 * (v**3/rc)
print(f'lsmin = {lsmin}m')
lsmax = rc * delta * pi /180
print(f'lsmax = {lsmax:.3f}m')
ls = 3*lsmin
print(f'ls = {ls}m')
if ls > lsmax:
    print('ls - Não cabe')
    media = int((lsmax+lsmin)/2)
    print(f'media do lsmin e lsmax = {media:.3f}m')
    print(f'O valor de ls utilizado será de = {media}m')
elif lsmin < ls < lsmax:
    media = int(ls)
print('-='*20)
#media = 120
print('#02 Angulo de transição espiral')
angulo = media /(2*rc)
print(f'{angulo:.6f} radianos')
o = 180 * angulo/pi
g = int(o)
m = (o-int(o))*60
s = (m-int(m))*60
print(f'{angulo:.6f} radianos = {g}º {int(m)}min {s:.2f}seg')
print('-='*20)

print('#03 Abcissa dos pontos cs e sc')
xs = media * (1 - (angulo**2/10) + (angulo**4/216))
print(f'Xs = {xs:.3f}m')
print('-='*20)

print('#04 Ordenadas dos pontos sc e cs')
ys = media*((angulo/3) - (angulo**3/42))
print(f'Ys = {ys:.3f}m')
print('-='*20)

print('#05 Angulo central do trecho circular')
fi = delta - 2 * o
g1 = int(fi)
m1 = (fi-int(fi))*60
s1 = (m1-int(m1))*60
print(f'fi = {g1}º {int(m1)}min {s1:.4}seg')
print('-='*20)

print('#06 Desenvolvimento circular')
d = (pi * rc * fi)/180
print(f'Desenvolvimento circular = {d:.3f}m')
print('-='*20)

print('#07 Abcissa do centro da curva circular')
q = xs - rc * math.sin(angulo)
print(f'q = {q:.3f}m')
print('-='*20)

print('#08 Afastamento da curva circular')
p = ys - rc *(1 - math.cos(angulo))
print(f'p = {p:.3f}m')
print('-='*20)

print('#09 Tangente total')
aa = math.tan(math.radians(delta/2))
tt = q + ((rc + p) * (aa))
print(f'tt = {tt:.3f}m')
print('-='*20)

print('#10 Estaca Ts')
ts = ((est1*20) + est2 - tt) / 20
print(f'ts = {int(ts)} + {(ts - int(ts)) * 20:.3f}')
print('-='*20)

print('#11 Estaca Sc')
sc = ((int(ts)*20) + ((ts - int(ts)) * 20) + media) / 20
print(f'sc = {int(sc)} + {(sc - int(sc)) * 20:.3f}')
print('-='*20)

print('#12 Estaca Cs')
cs = ((int(sc)*20) + ((sc - int(sc)) * 20) + d) / 20
print(f'cs = {int(cs)} + {(cs - int(cs)) * 20:.3f}')
print('-='*20)

print('#13 Estaca St')
st = ((int(cs)*20) + ((cs - int(cs)) * 20) + media) / 20
print(f'st = {int(st)} + {(st - int(st)) * 20:.3f}')
print('-='*20)

print('#14 Deflexão total da espiral')
o1 = o/3
g1 = int(o1)
m1 = (o1-int(o1))*60
s1 = (m1-int(m1))*60
is_ = g/3 + (((m * (1 / 60))/3) + ((s * (1 / 3600))/3))
print(f'is = {g1}º {int(m1)}min {s1:.2f}seg')
print('-='*20)

print('#15 Corda total do trecho em espiral')
cs1 = xs/math.cos(math.radians(is_))
print(f'Cs = {cs1:.3f}')
print('-='*20)

print('#16 Angulo de locação da tangente até a curva circular no ponto sc ')
js = o - o/3
g2 = int(js)
m2 = (js-int(js))*60
s2 = (m2-int(m2))*60
print(f'js = {g2}º {int(m2)}min {s2:.2f}seg')
print('-='*20)

print('#17 Flexa')
e = ((rc + p)/(math.cos(math.radians(delta/2)))) - rc
print(f'E = {e:.3f}m')
print('-='*20)

print('Superlargura')
S = ((2) * (rc - (math.sqrt(rc**2 - b**2))) + (v/(10 * math.sqrt(rc))))
print(f'S = {S:.3f}m = {round(S*100)}cm\nLargura total da Pista = {n * 2 + S:.2f}m')
print('-='*20)

print('Superelevação')
emax = float(input('emax: '))
rmin = float(input('rmin: '))
e = emax * ((2 * rmin/rc) - (rmin**2/rc**2))
print(f'e = {e:.3f}m/m = {e*100:.2f}%')



