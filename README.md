# OBS:

> todos os arquivos .ipynb foram feitos no ambiente google colab devem se executados nesse mesmo ambiente
> 
> já a questão 6 (arquivo q6.py) usa funcionalidade não suportada no colab deve ser executado local ou no jupyter notebook
# Q-6

```
img = cv2.imread('./pato.jpg')
edges_img1 = cv2.Canny(img,100,200, apertureSize=3)
edges_img2 = cv2.Canny(img,100,200, apertureSize=5)
edges_img3 = cv2.Canny(img,100,200, apertureSize=7)

fig, (original, edges1, edges2, edges3) = plt.subplots(1,4, figsize=(20,6))

original.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), cmap='gray')
original.set_title('Original')

edges1.imshow(cv2.cvtColor(edges_img1, cv2.COLOR_BGR2RGB), cmap='gray')
edges1.set_title('edges1')

edges2.imshow(cv2.cvtColor(edges_img2, cv2.COLOR_BGR2RGB), cmap='gray')
edges2.set_title('edges2')

edges3.imshow(cv2.cvtColor(edges_img3, cv2.COLOR_BGR2RGB), cmap='gray')
edges3.set_title('edges3')

```
-----------------------------------
```
edges = cv2.Canny(img, lower_limit, upper_limit, apertureSize=aperture_size)
```

## lower_limit
> O primeiro limite para o detector de bordas. É usado na fase de detecção de bordas para identificar as bordas mais fracas. Qualquer gradiente abaixo deste limite é desconsiderado como uma borda.


## upper_limit
>O segundo limite para o detector de bordas. É usado na fase de detecção de bordas para identificar as bordas mais fortes (que são mais propensas a serem bordas reais). É comum que threshold2 seja aproximadamente o dobro de threshold1.

## apertureSize
>Tamanho do kernel para o operador Sobel, que é usado internamente para cálculos de gradiente. Ele determina a precisão da operação de detecção de bordas. Valores menores capturam detalhes finos das bordas, mas também podem ser mais sensíveis ao ruído na imagem.
