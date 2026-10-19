"""Data augmentation com rotação e translação. Veja o README para instruções."""

import os

import cv2
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.utils import img_to_array, load_img

PASTA_IMAGENS = "imagens"
PASTA_SAIDA = "saida"

# (arquivo, transformação, valor, descrição)
EXEMPLOS = [
    ("dog.jpg", "rotacao", -30, "Cachorro"),
    ("dog.jpg", "translacao", 200, "Cachorro"),
    ("starry_night.jpg", "rotacao", 40, "Noite Estrelada"),
    ("cat.jpg", "rotacao", 180, "Gato"),
    ("paisagem.jpg", "translacao", 300, "Paisagem"),
    ("predios.jpg", "translacao", 800, "Prédios"),
]


def carregar_imagem(caminho):
    return img_to_array(load_img(caminho, color_mode="rgb"))


def rotacionar(data, angulo):
    altura, largura, _ = data.shape
    matriz = cv2.getRotationMatrix2D((largura / 2, altura / 2), angulo, 1)
    return cv2.warpAffine(data, matriz, (largura, altura))


def transladar(data, deslocamento):
    resultado = data.copy()
    resultado[:, :-deslocamento, :] = resultado[:, deslocamento:, :]
    return resultado


def matriz_rotacao(theta_graus):
    t = np.deg2rad(theta_graus)
    return np.array([[np.cos(t), -np.sin(t), 0],
                     [np.sin(t), np.cos(t), 0],
                     [0, 0, 1]])


def matriz_translacao(dx, dy=0):
    return np.array([[1, 0, dx],
                     [0, 1, dy],
                     [0, 0, 1]])


def aplicar_ao_ponto(matriz, x=2, y=2):
    return matriz @ np.array([x, y, 1])


def mostrar_e_salvar(original, transformada, titulo, nome_arquivo):
    fig, eixos = plt.subplots(1, 2, figsize=(10, 5))
    for eixo, imagem, nome in zip(eixos, (original, transformada), ("Original", "Sintética")):
        eixo.imshow(np.uint8(imagem))
        eixo.set_title(nome)
        eixo.axis("off")
    fig.suptitle(titulo)
    plt.tight_layout()

    os.makedirs(PASTA_SAIDA, exist_ok=True)
    caminho = os.path.join(PASTA_SAIDA, nome_arquivo)
    fig.savefig(caminho, dpi=150)
    print(f"  salvo em {caminho}")
    plt.show()


def main():
    for theta in (40, 180):
        x, y, _ = aplicar_ao_ponto(matriz_rotacao(theta))
        print(f"Rotação de {theta}°: ({x:.2f}, {y:.2f})")
    for dx in (300, 800):
        x, y, _ = aplicar_ao_ponto(matriz_translacao(dx))
        print(f"Translação de {dx}px: ({x:.0f}, {y:.0f})")

    for arquivo, tipo, valor, descricao in EXEMPLOS:
        caminho = os.path.join(PASTA_IMAGENS, arquivo)
        if not os.path.exists(caminho):
            print(f"[pulando] {caminho} não encontrado")
            continue

        data = carregar_imagem(caminho)
        if tipo == "rotacao":
            resultado = rotacionar(data, valor)
            titulo = f"{descricao}: rotação de {valor}°"
        else:
            resultado = transladar(data, valor)
            titulo = f"{descricao}: translação de {valor}px"

        nome = os.path.splitext(arquivo)[0]
        mostrar_e_salvar(data, resultado, titulo, f"{nome}_{tipo}_{valor}.png")


if __name__ == "__main__":
    main()