import cv2
import numpy as np

# Função callback para as trackbars
def nothing(x):
    pass


aperture_sizes_values = [3, 5, 7]



# Cria uma janela de imagem vazia
cv2.namedWindow('Edge Detection')

# Cria as trackbars para os valores de limite superior e inferior
cv2.createTrackbar('Limite Inferior', 'Edge Detection', 0, 255, nothing)
cv2.createTrackbar('Limite Superior', 'Edge Detection', 0, 255, nothing)
cv2.createTrackbar('Aperture size', 'Edge Detection', 0, len(aperture_sizes_values) -1 , nothing)

# Define a imagem de entrada (substitua pela sua imagem)
img = cv2.imread('./pato.jpg')

while True:
    # Obtém os valores atuais das trackbars
    lower_limit = cv2.getTrackbarPos('Limite Inferior', 'Edge Detection')
    upper_limit = cv2.getTrackbarPos('Limite Superior', 'Edge Detection')
    aperture_size_idx  = cv2.getTrackbarPos('Aperture size', 'Edge Detection')
    
    aperture_size = aperture_sizes_values[aperture_size_idx]

    # Aplica a detecção de borda Canny com os valores dos trackbars
    edges = cv2.Canny(img, lower_limit, upper_limit, apertureSize=aperture_size)

    # Exibe a imagem de borda
    cv2.imshow('Edge Detection', edges)

    # Sai do loop quando a tecla 'q' é pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Fecha todas as janelas abertas
cv2.destroyAllWindows()
