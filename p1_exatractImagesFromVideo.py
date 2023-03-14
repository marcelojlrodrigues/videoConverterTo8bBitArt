import cv2

# Abre o vídeo de entrada
cap = cv2.VideoCapture('meuvideo.mp4')

# Define o contador de frames
frame_count = 0

# Processa cada frame do vídeo de entrada
while cap.isOpened():
    # Lê o próximo frame do vídeo de entrada
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Define o nome do arquivo de saída
    filename = f'frame_{frame_count:04d}.png'
    
    # Salva o frame como uma imagem
    cv2.imwrite(filename, frame)
    
    # Atualiza o contador de frames
    frame_count += 1

# Libera os recursos utilizados
cap.release()
