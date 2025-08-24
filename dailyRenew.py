import sys 
import fireWhale

# Check if a parameter was provided
if len(sys.argv) > 1:
    # Get the first parameter
    parametro = sys.argv[1]
    print(f"Parámetro recibido: {parametro}")


fireWhale.editaDato("quota", parametro, "segundos", 1500)
print(f"Servidor {parametro} actualizado.")
