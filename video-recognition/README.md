# Video Recognition - Análise de Atividades e Emoções

**Tech Challenge - Fase 4 | Pós-Tech FIAP - IA para Devs**

Sistema inteligente de análise de vídeo que detecta **atividades físicas**, **emoções** e **anomalias**.

---

## Equipe

- **Bruno Lima da Cruz**
- **Matheus Braz Giudice dos Santos**
- **Mislene Dalila da Silva**

---

## Visão Geral

Este projeto foi desenvolvido como solução para o **Tech Challenge da Fase 4** do curso de Pós-Tech em IA para Devs da FIAP. O sistema analisa vídeos para:

- ✅ **Reconhecimento Facial**: Identifica e marca rostos presentes no vídeo
- ✅ **Análise de Emoções**: Detecta expressões emocionais dos rostos identificados
- ✅ **Detecção de Atividades**: Categoriza atividades físicas realizadas
- ✅ **Detecção de Anomalias**: Identifica movimentos atípicos ou comportamentos fora do padrão
- ✅ **Geração de Relatório**: Resume automaticamente as principais atividades, emoções e anomalias detectadas

---

## Funcionalidades

### Atividades Detectadas

O sistema classifica as seguintes atividades baseado na análise de pose corporal:

- **Standing** (Parado): Pessoa em pé sem movimento significativo
- **Walking** (Caminhando): Movimento moderado com deslocamento
- **Dancing** (Dançando): Movimentos rápidos e expressivos
- **Sitting** (Sentado): Postura sentada
- **Raising Arm** (Levantando braço): Braços elevados acima dos ombros
- **Unknown** (Desconhecido): Atividade não classificada

### Emoções Detectadas

Análise facial que reconhece 7 emoções principais:

- **Happy** (Feliz)
- **Sad** (Triste)
- **Angry** (Raiva)
- **Surprise** (Surpresa)
- **Fear** (Medo)
- **Disgust** (Nojo)
- **Neutral** (Neutro)


---

## Tecnologias Utilizadas

| Tecnologia | Versão | Função |
|------------|--------|--------|
| **Python** | 3.9 | Linguagem principal |
| **MediaPipe** | 0.10.8 | Detecção de pose corporal e landmarks |
| **DeepFace** | 0.0.75 | Análise facial e reconhecimento de emoções |
| **OpenCV** | 4.8.1 | Processamento e manipulação de vídeo |
| **TensorFlow** | 2.10.0 | Backend de deep learning |
| **NumPy** | 1.24.3 | Operações numéricas e vetoriais |
| **Docker** | Latest | Containerização e isolamento de ambiente |

---

## Como Executar

### Opção 1: Docker (Recomendado) 🐳

**Pré-requisito:** [Instalar Docker Desktop](https://www.docker.com/products/docker-desktop/)

```bash
# 1. Clonar repositório
git clone https://github.com/bruno1cruz/ia.git
cd ia/video-recognition

# 2. Build da imagem (primeira vez - ~5-10 min)
docker build -t video-recognition .

# 3. Executar com vídeo
docker run --rm \
    -v /caminho/completo/do/seu/video.mp4:/app/video.mp4 \
    -v $(pwd)/output.mp4:/app/output.mp4 \
    video-recognition

# 4. Ver resultado
open output.mp4
```

**Exemplo prático:**
```bash
docker run --rm \
    -v ~/Downloads/video_teste.mp4:/app/video.mp4 \
    -v $(pwd)/output.mp4:/app/output.mp4 \
    video-recognition
```

---

### Opção 2: Ambiente Local 💻

**Pré-requisitos:** Python 3.9+, pip

```bash
# 1. Clonar repositório
git clone https://github.com/bruno1cruz/ia.git
cd ia/video-recognition

# 2. Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Instalar dependências
pip install --upgrade pip
pip install -r requirements.txt

# 4. Executar
python main.py                              # Usa video.mp4 padrão
python main.py /caminho/para/video.mp4       # Vídeo específico
python main.py input.mp4 output.mp4          # Input e output customizados
```

---

## Relatório Gerado

O sistema gera automaticamente um **relatório completo** ao final do processamento.


---

## Vídeo de Saída

O vídeo `output.mp4` gerado conterá:

- ✅ **Landmarks corporais**: Pontos e conexões desenhados sobre o corpo
- ✅ **Bounding boxes**: Retângulos verdes ao redor das faces detectadas
- ✅ **Rótulos de emoções**: Texto mostrando a emoção detectada
- ✅ **Indicadores de anomalias**: Marcadores visuais quando anomalias são detectadas
- ✅ **Mesma resolução e FPS**: Mantém qualidade do vídeo original

---

## Estrutura do Projeto

```
video-recognition/
├── Dockerfile              # Configuração Docker
├── requirements.txt        # Dependências Python
├── main.py                # Script principal
├── README.md              # Este arquivo
├── video.mp4              # Vídeo de entrada (fornecido pela FIAP)
└── output.mp4             # Resultado processado (gerado)
```

---

## Demonstração

**Link do vídeo de demonstração no YouTube:**  
🎥 https://www.youtube.com/watch?v=24hJtaRv4gA


---

## Links Importantes

- 📂 **Repositório GitHub**: https://github.com/bruno1cruz/ia
- 🎥 **Vídeo no YouTube**: https://www.youtube.com/watch?v=24hJtaRv4gA

---
