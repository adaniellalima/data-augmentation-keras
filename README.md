# Aumento de Dados Sintéticos: Utilizando a Biblioteca Keras

Trabalho de Conclusão de Curso (Técnico em Informática)
Instituto Federal de São Paulo, Câmpus Itapetininga, 2023

**Autora:** Daniella Lima de Oliveira
**Orientador:** Prof. Dr. Carlos Henrique da Silva Santos

## Sobre o projeto

O trabalho explora o *data augmentation* (aumento de dados), técnica usada em
aprendizado de máquina para ampliar conjuntos de dados com variações
artificiais das amostras originais. O foco está em duas transformações
geométricas aplicadas a imagens, com o embasamento matemático de cada uma:

- **Rotação:** matriz de rotação 2D aplicada em torno do centro da imagem.
- **Translação:** deslocamento horizontal da imagem por um vetor (Δx, Δy).

O texto completo está em [`TCC_Daniella_Lima.pdf`](TCC_Daniella_Lima.pdf).

## Estrutura do repositório

```
.
├── data_augmentation.py   # código das transformações
├── requirements.txt       # dependências
├── imagens/               # imagens de entrada (veja abaixo)
├── saida/                 # imagens geradas pelo script
└── TCC_Daniella_Lima.pdf  # texto do trabalho
```

## Como executar

**Pré-requisitos:** Python 

# 1. instalar as dependências
pip install -r requirements.txt

# 2. rodar
python data_augmentation.py
```

O script mostra a imagem original ao lado da sintética e salva os resultados
na pasta `saida/`. Imagens que não estiverem em `imagens/` são puladas.

## Imagens de entrada

Coloque as imagens na pasta `imagens/` com estes nomes:

| Arquivo            | Transformação      | Exemplo no TCC |
|--------------------|--------------------|----------------|
| `dog.jpg`          | Rotação -30° e translação 200 px | Figs. 4 a 12 |
| `starry_night.jpg` | Rotação 40°        | Fig. 13 |
| `cat.jpg`          | Rotação 180°       | Fig. 15 |
| `paisagem.jpg`     | Translação 300 px  | Fig. 17 |
| `predios.jpg`      | Translação 800 px  | Fig. 19 |

## Créditos das Imagens
https://pixabay.com/pt/photos/retroiluminado-estrelas-c%C3%A9u-noturno-1845281/
https://pixabay.com/pt/photos/cachorro-cadela-bernese-mountain-dog-2668993/
https://pixabay.com/pt/photos/cat-pet-portrait-eyes-net-5128590/
https://pixabay.com/pt/photos/m%C3%BChlviertel-rural-n%C3%A9voa-%C3%A1ustria-7544316/
https://pixabay.com/pt/photos/cidade-rua-arquitetura-o-neg%C3%B3cio-4667143/

## Tecnologias

Python, Keras (TensorFlow), OpenCV, NumPy e Matplotlib.

## Observação sobre os cálculos

As funções `matriz_rotacao` e `matriz_translacao` reproduzem as matrizes das
Figuras 6 e 8 do trabalho. Nelas, os ângulos são interpretados em **graus**.