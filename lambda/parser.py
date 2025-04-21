import os
import boto3

s3 = boto3.client('s3')

def handler(event, context):
    # Obtener información del evento S3
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Descargar archivo
    response = s3.get_object(Bucket=source_bucket, Key=key)
    content = response['Body'].read().decode('utf-8')
    
    # Procesar (ejemplo: convertir a mayúsculas)
    processed_content = content.upper()
    
    # Subir al bucket destino
    destination_bucket = os.environ['DESTINATION_BUCKET']
    s3.put_object(
        Bucket=destination_bucket,
        Key=f"processed_{key}",
        Body=processed_content.encode('utf-8')
    )
    
    return {"statusCode": 200, "body": "Archivo procesado correctamente!"}