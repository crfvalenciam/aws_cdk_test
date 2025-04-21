# aws_cdk_test
1. Configuración Inicial

a. Instalar AWS CDK
bash
npm install -g aws-cdk

c. Configurar Entorno Virtual (Python)
bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
-- .venv\Scripts\activate   # Windows

2. Instalar Dependencias

pip install aws-cdk-lib constructs


3. Despliegue en AWS
a. Bootstrap del Entorno (solo primera vez)
    cdk bootstrap aws://TU_ACCOUNT_ID/us-east-1
b. Desplegar el Stack
    cdk deploy

4. Prueba de Funcionamiento
bash
    aws s3 ls

# Subir archivo de prueba
echo "Hola CDK" > test.txt
aws s3 cp test.txt s3://lambdas3stack-sourcebucketXXXX/test.txt

# Verificar resultado


aws s3 ls s3://aws s3 cp test.txt s3://lambdas3stack-sourcebucketddd2130a-0gso0go5mldw/test.txt/processed_test.txt

5. Eliminación de Recursos
cdk destroy --force

