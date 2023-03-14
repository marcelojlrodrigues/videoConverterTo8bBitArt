import os
from multiprocessing import Pool, freeze_support
from skimage import io
from pyxelate import Pyx
import itertools

# Define o diretório de entrada e saída
input_dir = "frames/"
output_dir = "frames_convertidos/"

# Verifica se a pasta de saída existe, caso contrário, cria-a
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define os parâmetros de conversão
downsample_by =  5 # nova imagem será 1/7 do tamanho original
palette = 5  # utilizar 7 cores
n_workers = 4 # número de processos paralelos

# Lista todos os arquivos na pasta de entrada
files = os.listdir(input_dir)
# Filtra apenas os arquivos de imagem
image_files = [f for f in files if f.endswith(".png")]

# Define uma função para processar cada imagem
def process_image(filename):
    # Carrega a imagem
    image = io.imread(os.path.join(input_dir, filename))
    # Cria um novo nome de arquivo para a imagem convertida
    new_filename = os.path.splitext(filename)[0] + "_convertido.png"
    # Define o caminho completo para o arquivo de saída
    output_path = os.path.join(output_dir, new_filename)
    # Converte a imagem para arte em pixel
    pyx = Pyx(factor=downsample_by, palette=palette)
    pyx.fit(image)
    new_image = pyx.transform(image)
    # Salva a imagem convertida na pasta de saída
    io.imsave(output_path, new_image)

if __name__ == '__main__':
    freeze_support()
    
    # Divide a lista de imagens em lotes
    batch_size = len(image_files) // n_workers
    batches = [image_files[i:i+batch_size] for i in range(0, len(image_files), batch_size)]
    file_list = list(itertools.chain.from_iterable(batches))

    # Processa os lotes em paralelo
    with Pool(processes=n_workers) as pool:
        pool.map(process_image, file_list)
