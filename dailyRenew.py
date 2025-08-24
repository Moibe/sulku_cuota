import sys 
import fireWhale

if len(sys.argv) > 1:    
    parametro = sys.argv[1]

fireWhale.editaDato("quota", parametro, "segundos", 1500)
print(f"Servidor {parametro} actualizado.")