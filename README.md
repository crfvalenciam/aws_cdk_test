# aws_cdk_test
1. Configuración Inicial

a. Instalar AWS CDK
bash
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
    nvm install 20
    nvm use 20
    node -v
    npm install -g aws-cdk

c. Configurar Entorno Virtual (Python)
bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
-- .venv\Scripts\activate   # Windows

2. Instalar Dependencias

pip install -r requirements


3. Despliegue en AWS

export AWS_ACCESS_KEY_ID='AWS_ACCESS_KEY_ID' #------------------ MODIFICAR VALOR 
export AWS_SECRET_ACCESS_KEY='AWS_SECRET_ACCESS_KEY' #---------- MODIFICAR VALOR 
export AWS_REGION='AWS_REGION' # MODIFICAR VALOR 
aws sts get-caller-identity

a. Bootstrap del Entorno (solo primera vez)
    cdk bootstrap aws://ACCOUNT_ID/us-east-1 #----------------- MODIFICAR VALOR 
b. Desplegar el Stack
    cdk deploy

1. Prueba de Funcionamiento
bash
    aws s3 ls

# Subir archivo de prueba
echo "Hola CDK" > test.txt
aws s3 cp test.txt s3://lambdas3stack-sourcebucketXXXX/test.txt

# Verificar resultado


aws s3 ls s3://aws s3 cp test.txt s3://lambdas3stack-sourcebucketddd2130a-0gso0go5mldw/test.txt/processed_test.txt

5. Eliminación de Recursos
cdk destroy --force

