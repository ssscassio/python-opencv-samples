import cv2

def main() :
    #Le a imagem
    image = cv2.imread("len_std.png", cv2.IMREAD_GRAYSCALE)
    #Salva a imagem modificada
    cv2.imwrite('len_gray.png', image)

main()