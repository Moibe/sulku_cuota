import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials.
cred = credentials.Certificate('config.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def obtenDato(coleccion, dato, info):
       
    #Future: Tentativamente ésta parte podría solo hacerse una vez y vivir en la app para ser reutilizado.
    ###
    #Primero debemos definir la referencia al documento, o sea a la hoja de usuario.
    doc_ref = db.collection(coleccion).document(dato)
    #Éste es el documento que tiene los datos de ella.
    documento = doc_ref.get()
    ###

    #Recuerda la conversión a diccionario.
    diccionario = documento.to_dict()

    return diccionario.get(info)

def editaDato(coleccion, dato, info, contenido):

    #Primero debemos definir la referencia al documento, o sea a la hoja de usuario.
    doc_ref = db.collection(coleccion).document(dato)
    
    doc_ref.update({
        # 'quote': quote,
        info: contenido,
    })

def modificar_campo_numerico(collection_name, document_id, field_name, amount=1):
    """
    Incrementa un campo numérico en un documento de Firestore de forma atómica.
    Si el documento no existe, lo crea e inicializa el campo con el 'amount'.
    Si el campo no existe en un documento existente, lo inicializa y aplica el incremento.

    Args:
        collection_name (str): El nombre de la colección.
        document_id (str): El ID del documento.
        field_name (str): El nombre del campo numérico a incrementar.
        amount (int/float): La cantidad por la cual incrementar (puede ser negativo para decrementar).
    """
    doc_ref = db.collection(collection_name).document(document_id)

    try:
        # Usamos .set() con merge=True para comportamiento de "upsert".
        # Si el documento no existe, lo crea.
        # Si el campo no existe, lo crea e inicializa con 'amount'.
        # Si el campo ya existe, lo incrementa con 'amount'.
        doc_ref.set(
            {field_name: firestore.Increment(amount)},
            merge=True  # Esta es la clave para que se cree si no existe y no sobrescriba otros campos
        )
        print(f"✔️ Campo '{field_name}' en el documento '{document_id}' actualizado/creado e incrementado en {amount}.")
    except Exception as e:
        print(f"❌ Error al operar en el campo '{field_name}' del documento '{document_id}': {e}")

