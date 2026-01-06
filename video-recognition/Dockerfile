# Dockerfile para video-recognition
FROM python:3.10-slim

# Instala dependências de sistema necessárias para opencv e deepface
RUN apt-get update && \
    apt-get install -y ffmpeg libgl1 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copia requirements e instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código fonte
COPY main.py .

# Permite passagem de argumentos para o vídeo de entrada e saída
ENTRYPOINT ["python", "main.py"]
# O caminho do vídeo pode ser passado via variável de ambiente ou modifique main.py para aceitar argumentos
