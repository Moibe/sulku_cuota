import sys 
import fireWhale

if len(sys.argv) > 1:    
    parametro = sys.argv[1]

if parametro == 'irina':
    segundos = 240
else: 
    segundos = 1500

fireWhale.editaDato("power", parametro, "segundos", segundos)
print(f"Servidor {parametro} actualizado.")