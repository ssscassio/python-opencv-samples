import cv2

def main() :
    #Le a imagem
    image = cv2.imread("len_std.png")
    #Mostra a imagem na janela
    cv2.namedWindow("Imagem 256x256") # define a janela
    cv2.imshow("Imagem 256x256", image)
    #Redimensiona a imagem
    redimensionada = cv2.resize(image, (128, 128))
    #redimensionada = cv2.resize(image, (0,0), fx=0.5, fy=0.5) #Redimensiona baseado os eixos
    #Mostra a imagem na janela
    cv2.namedWindow("Imagem 128x128"); # define a janela
    cv2.imshow("Imagem 128x128", redimensionada);
    #Salvar a imagem redimensionada
    cv2.imwrite("lena128x128.png",redimensionada); 

    cv2.waitKey(0)
    
main()