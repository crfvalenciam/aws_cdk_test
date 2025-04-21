#!/usr/bin/env python3
import aws_cdk as cdk
from mi_proyecto_cdk.lambda_s3_stack import LambdaS3Stack

app = cdk.App()

# Define la cuenta y región (opcional, pero recomendado)
env = cdk.Environment(
    account="071021222485",  # Reemplaza con tu ID de cuenta
    region="us-east-1"
)

LambdaS3Stack(app, "LambdaS3Stack", env=env)

app.synth()