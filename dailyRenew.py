import fireWhale
import sys 

# Check if a parameter was provided
if len(sys.argv) > 1:
    # Get the first parameter
    parametro = sys.argv[1]
    print(f"Parámetro recibido: {parametro}")


fireWhale.editaDato("quota", 'iri', "segundos", 1500)
print("Servidor Iri actualizado.")
