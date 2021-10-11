import json
import os
import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    lista_instancias = os.environ['INSTANCIAS']
    instancias = lista_instancias.split(',')

    action = event["action"]
    
    if action == 'Start':
        ec2.start_instances(InstanceIds=instancias)
        response = "Iniciando as Instancias: " + str(instancias)
    elif action == 'Stop':
        ec2.stop_instances(InstanceIds=instancias)
        response = "Parando as Instancias: " + str(instancias)

    return {
        'body': json.dumps(response)
    }