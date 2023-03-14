import os
import cv2

# Define o diretório de entrada e saída
input_dir = "frame"
output_file = "video_in_8bits.mp4"

# Lista todos os arquivos da pasta de entrada ordenados por nome
files = sorted(os.listdir(input_dir), key=lambda x: int(x.split("_")[1].split(".")[0]))

# Define as configurações do vídeo
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
fps = 30.0

# Lê a primeira imagem para obter as dimensões do vídeo
img = cv2.imread(os.path.join(input_dir, files[0]))
height, width, _ = img.shape

# Cria o objeto de vídeo
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

# Escreve cada imagem no objeto de vídeo
for file in files:
    img = cv2.imread(os.path.join(input_dir, file))
    out.write(img)

# Libera o objeto de vídeo
out.release()
