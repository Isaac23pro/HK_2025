import logging

# Configura el logger para el proyecto
logger = logging.getLogger("memoria_viva")
logger.setLevel(logging.INFO)

handler = logging.FileHandler("memoria_viva_auditoria.log")
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)

if not logger.hasHandlers():
    logger.addHandler(handler)
