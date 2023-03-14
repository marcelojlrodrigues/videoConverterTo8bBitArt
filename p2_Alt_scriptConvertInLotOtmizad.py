from skimage import io
from pyxelate import Pyx, Pal
import os

# Define o diretório de entrada e saída
input_dir = "frames/"
output_dir = "frames_convertidos/"

# Verifica se a pasta de saída existe, caso contrário, cria-a
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define os parâmetros de conversão
downsample_by = 5  # nova imagem será 1/7 do tamanho original
palette = 5  # utilizar 7 cores
n_workers = 4  # utilizar 4 núcleos de CPU para processamento paralelo

# Percorre todos os arquivos na pasta de entrada
for filename in os.listdir(input_dir):
    # Verifica se é um arquivo de imagem
    if filename.endswith(".png"):
        # Carrega a imagem e reduz sua resolução
        image = io.imread(os.path.join(input_dir, filename))
        image = image[::downsample_by, ::downsample_by, :]
        
        # Cria um novo nome de arquivo para a imagem convertida
        new_filename = os.path.splitext(filename)[0] + ".png"
        
        # Define o caminho completo para o arquivo de saída
        output_path = os.path.join(output_dir, new_filename)
        
        # Converte a imagem para arte em pixel
        pyx = Pyx(factor=1, palette=palette, dither=False)
        pyx.fit(image)
        new_image = pyx.transform(image, n_workers=n_workers)
        
        # Salva a imagem convertida na pasta de saída
        io.imsave(output_path, new_image)
