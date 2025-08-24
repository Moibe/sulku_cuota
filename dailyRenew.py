import sys 
import fireWhale

if len(sys.argv) > 1:    
    parametro = sys.argv[1]

if parametro == 'iri':
    segundos = 240
else: 
    segundos = 1500

fireWhale.editaDato("quota", parametro, "segundos", 1500)
print(f"Servidor {parametro} actualizado.")