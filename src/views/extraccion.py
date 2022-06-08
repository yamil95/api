import logging
import io
from datetime import datetime, timedelta

import pandas as pd
import azure.storage.blob as blob
from flask import request
from flask_restful import Resource

from utilities import (
    finish,
    validar_campos,
    identificar
)


class ExtraccionView(Resource):

    def __init__(self):
        super(ExtraccionView).__init__()

    def post(self):
        # INICIO PRIMER VALIDACION. SE VALIDA QUE SE HAYAN RECIBIDO TODOS LOS ELEMENTOS NECESARIOS EN EL INPUT.
        logging.info('Comenzando validación del input.')
        containerName = request.headers.get('container')
        
        try:
            inputJson = request.get_json()
            idEstacion = inputJson["idEstacion"]
            allData = inputJson["rows"]
        except:
            return finish("Error al intentar leer el JSON. No se encontraron los campos 'rows' y/o 'idEstacion'",
                          "Null or invalid JSON data on body", 422)
        if (not containerName):
            return finish("Error. No se especificó el nombre del container en el header.",
                          "Invalid input. Missing container value on header input.", 422)
       
        #codIdentificador = token[0:1]
      
        # INICIO CUARTA VALIDACION. SE VALIDA QUE EN LOS CAMPOS DEL JSON RECIBIDO NO HAYA STRINGS VACIOS, NULL Y QUE SOLO CONTENGAN [a-zA-Z0-9.-_]+
        valoresValidos = validar_campos(inputJson['rows'])
        if (valoresValidos != "ok"):
            return finish("Error, los campos del json sólo pueden contener [a-zA-Z0-9.-_:/,*°()]+",
                          "Invalid data on json. Use only [a-zA-Z0-9.-_:/,*]+", 422)
        # FIN CUARTA VALIDACION.
        codIdentificador = identificar ("1")
        inputJson["rows"].append(f"EESS:{codIdentificador}")
        
        
        logging.info('Input valido. Comenzando conexion a BD.')
        now = str((datetime.now() - timedelta(hours=3)).strftime('%Y%m%d_%H%M%S%f'))
        
        blobName = "input/" + codIdentificador + "_" + inputJson[
            "idEstacion"] + "_" + now + ".json"  # SE ASIGNA NOMBRE AL JSON OUTPUT.
        try:
            # CONEXION A LA BD Y POSTERIOR UPLOAD DEL JSON.
           #retrieved_secret =    #getConnectionString()
            
            blobServiceClient = blob.BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=raizenarbistorage01qat;AccountKey=e9JZXxlC4aiLF4fZq0pynwrwdOScbzMWamJWyikOlyC4EuyQimAp5WZaRyURi7wIs405xtyZzSCoBjhTU/vzHA==;EndpointSuffix=core.windows.net")
            blob_client = blobServiceClient.get_blob_client(container=containerName, blob=blobName)
            
            buf = io.StringIO(str(inputJson["rows"]))
            blob_client.upload_blob(buf.getvalue())
        except Exception as e:
            print (e)
            return finish("Error while connecting to database.", "Blob Storage not found.", 400)

        return finish("Success", "Success", 200)
