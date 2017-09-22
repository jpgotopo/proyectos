#esto sería abriendo un fichero donde quieres que te cuente.
f = open(nombreDelFichero, 'r')
texto = f.read()
f.close()
 
##esto sería leyendo una cadena que existe.
#texto = 'Leerá las letras en este string'
 
##esto sería leyendo una cadena que des.
#texto = raw_input()
 
cuenta = 0
cuenta2 = 0
cuenta3 = 0
for carac in texto:
    if carac == 'a':
        cuenta += 1
    if carac == 'b':
        cuenta2 += 1
    if carac == 'b':
        cuenta3 += 1
print 'Existen:', cuenta, 'a,', cuenta2, 'b, y', cuenta3, 'c.'
