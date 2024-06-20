# Usar uma imagem base do Python mais específica, como o Python 3.11.0-slim-buster
FROM python:3.11.0-slim-buster

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copiar todo o conteúdo do diretório atual para o diretório de trabalho no contêiner /app
COPY . .

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expor porta 8000 para permitir conexões com o servidor Django
EXPOSE 8000

# Executar o comando para coletar os arquivos estáticos
RUN python manage.py collectstatic --noinput

CMD ["bash", "-c", "python manage.py makemigrations && python manage.py migrate && daphne -b 0.0.0.0 -p 8090 project.asgi:application"]