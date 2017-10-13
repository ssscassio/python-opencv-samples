import cv2
import random

def main():
    #Le a imagem
    image = cv2.imread("len_std.png")

    #Mostra a imagem na janela
    cv2.namedWindow("Imagem Original") # define a janela
    cv2.imshow("Imagem Original", image)

    image = saltPepperNoise(image,1000,0) #Adiciona ruido tipo pimenta na imagem
    image = saltPepperNoise(image,1000,255) #Adiciona ruido tipo sal na imagem

    cv2.namedWindow("Imagem com ruido") #define a janela
    cv2.imshow("Imagem com ruido",image)

    cv2.imwrite("ImagemRuido.png",image)

    cv2.waitKey(0)

    return 1

def saltPepperNoise(image, numberOfNoise, noiseType):
    """ 
    Adiciona ruido estilo sal e pimenta na imagem
    
    Parametros
    ----------
    image : image
        Imagem a ser adicionado o ruido
    numberOfNoise : int
        Quantidade de pixels que serao randomicamente escolhidos para sofrer a alteracao
    noiseType: int
        Tipo do ruido, valor entre 0 e 255 definindo a cor do ruido a ser aplicado.
        0 -> preto / 100 -> cinza / 255 -> branco
    
    Returns
    -------
    image
        imagem com ruido aplicado
    """
    numberOfLines, numberOfColumns, numberOfChannels =  image.shape
    for k in range(0, numberOfNoise) :
        line = random.randint(0, numberOfLines - 1)
        column = random.randint(0, numberOfColumns - 1)
        for channel in range(0, numberOfChannels) :
            image[line,column,channel] = noiseType
    return image

main()