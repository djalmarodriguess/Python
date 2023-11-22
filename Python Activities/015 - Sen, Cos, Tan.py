from math import radians, sin, cos, tan
an = float(input('Qual o ângulo?'))
sen = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print('Para o ângulo de {}º\nSENO = {:.2f}\nCOSSENO = {:.2f}\nTANGENTE = {:.2f}' .format(an, sen, cos, tan))