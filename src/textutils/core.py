import string
import re
from unicodedata import normalize

def slugify(text: str) -> str:
    """
    Convierte `text` en un slug seguro:
    - Convierte a minúsculas.
    - Normaliza caracteres unicode (elimina acentos).
    - Elimina caracteres que no son letras o números.
    - Sustituye espacios y separadores por guiones.
    - Quita guiones duplicados, al inicio y final.
    - Devuelve una cadena vacía si no hay texto útil.
    """
    if not isinstance(text, str) or not text.strip():
        return ''
    
    # Convertir a minúsculas y normalizar unicode
    t = text.lower()
    t = normalize('NFKD', t).encode('ascii', 'ignore').decode('ascii')
    
    # Reemplazar todo lo que no sea letra, número o espacio por espacio
    t = re.sub(r'[^a-z0-9\s-]', '', t)
    
    # Reemplazar espacios y guiones múltiples por un solo guion
    t = re.sub(r'[\s-]+', '-', t)
    
    # Quitar guiones al inicio y final
    t = t.strip('-')
    
    return t
