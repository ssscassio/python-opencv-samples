import cv2

def main() :
    #Le a imagem
    image = cv2.imread("len_std.png", 1) # cv2.IMREAD_UNCHANGED = -1 / cv2.IMREAD_GRAYSCALE = 0 / cv2.IMREAD_COLOR = 1
    #Mostra a imagem na janela
    cv2.namedWindow("Imagem Original") # define a janela
    cv2.imshow("Imagem Original", image) 
    #Mostra o tamanho da imagem
    height, width, channels = image.shape
    print "Tamanho: %dx%d" % (height, width)
    cv2.waitKey(0)

main()