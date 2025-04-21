from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_lambda as lambda_,
    aws_iam as iam,
    aws_s3_notifications as s3n,
    RemovalPolicy
)
from constructs import Construct

class LambdaS3Stack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # 1. Buckets S3 con políticas de eliminación
        source_bucket = s3.Bucket(self, "SourceBucket",
            removal_policy=RemovalPolicy.DESTROY,  # Elimina el bucket al destruir el stack
            auto_delete_objects=True               # Borra objetos automáticamente
        )
        
        destination_bucket = s3.Bucket(self, "DestinationBucket",
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )

        # 2. Rol IAM para Lambda (optimizado)
        lambda_role = iam.Role(
            self,
            "LambdaS3Role",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3ReadOnlyAccess"),  # Solo lectura para el bucket fuente
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
            ]
        )
        
        # Permiso de escritura específico para el bucket destino
        destination_bucket.grant_write(lambda_role)

        # 3. Función Lambda con política de eliminación
        parser_lambda = lambda_.Function(
            self,
            "FileParserLambda",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="parser.handler",
            code=lambda_.Code.from_asset("lambda"),
            role=lambda_role,
            environment={
                "DESTINATION_BUCKET": destination_bucket.bucket_name
            }
        )
        parser_lambda.apply_removal_policy(RemovalPolicy.DESTROY)

        # 4. Trigger S3 → Lambda
        source_bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED,
            s3n.LambdaDestination(parser_lambda)
        )