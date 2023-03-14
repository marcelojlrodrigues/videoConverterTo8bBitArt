# Turorial de como usar

## Recomendação: Busque processar vídeos curtos, pois esse processamento demora bastante, a não ser que você tenha uma máquina muito boa mesmo

1. Execute o arquivo p1_exatractImmagesFromVieo.py
    a. Se atente, ao caminho e ao nome do arquivo do vídeo, se não especificar ele o pegará na pasta raiz, com o nome "meuvideo.pm4"
    
    ```python 
    # Abre o vídeo de entrada
    cap = cv2.VideoCapture('meuvideo.mp4')
    
    b. Feito isso, execute esse arquivo, e os vídeos estarão extraídos dentro da pasta "frame"

2. Execute o arquivo "P2_convertImagesInLot.py" ou se preferir execute o script otimizado "P2_Alt_scriptConvertInLotOtmizado.py"

    a. Se atente ao diretório de entrada e saída e o nome do arquivos:

    ```python 
    # Define o diretório de entrada e saída
    input_dir = "frame"  
    output_dir = "frames_convertidos"

    b. Feito isso execute este arquivo escolhido

3. Por último, execute o arquivo "P3_convertImagesInVideo.py" quer irá criar o seu vídeo convertido

    ```python
    # Define o diretório de entrada e saída
    input_dir = "frame"
    output_file = "video_in_8bits.mp4"


## Pessoal no passo 2, deixei dois arquivos otimizados, pois um deles funciona bem, como não tive tempo de testar qual deles, peço que teste um, mas seguindo estes passos com atenção tudo deve funcionar bem

## Se quiser contribuir com melhorias desse código, me chame: marcelorodrigues2005@gmail.com
    