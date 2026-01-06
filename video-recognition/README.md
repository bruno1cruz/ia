1. Reconhecimento facial
2. Analise as expressões
3. Detecção de atividades

## Como rodar com Docker

### Build da imagem
```bash
docker build -t video-recognition .
```

### Executando com vídeo externo
Supondo que você tenha um arquivo `video.mp4` em `/caminho/para/seu/video.mp4`:

```bash
# Com nome padrão (video.mp4 → output.mp4)
docker run --rm \
    -v /caminho/para/seu/video.mp4:/app/video.mp4 \
    -v /caminho/para/salvar/output.mp4:/app/output.mp4 \
    video-recognition
```