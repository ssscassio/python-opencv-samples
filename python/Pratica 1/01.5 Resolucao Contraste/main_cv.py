import cv2

def colorReduce(entrada, iBit = 1):
    numberOfLines, numberOfColumns, numberOfChannels =  entrada.shape
    
    # Copia da imagem de entrada para ser manipulada
    destino = entrada.copy()

    # Iteracao por cada pixel em cada um dos canais 
    for line in range(0, numberOfLines):
        for column in range(0, numberOfColumns):
            for channel in range(0, numberOfChannels):
                # bitwise Right Shift no valor do pixel para diminuir a resolucao
                destino[line, column, channel] = destino[line, column, channel] >> iBit
    
    # Necessario normalizar o valor dos pixel pois caso contrario a imagem apenas fica mais escura
    cv2.normalize(destino, destino, 0, 255, cv2.NORM_MINMAX )
    return destino

def main() :
    #Le a imagem (colored, 3-channel, BGR)
    img256 = cv2.imread("len_std.png")
    if img256 is None:
        print "Erro na leitura da imagem"
        return -1;
    
    #cv2.normalize https://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html#normalize
    cv2.namedWindow("256 Tons",cv2.WINDOW_AUTOSIZE)
    cv2.normalize(img256, img256, 0, 255, cv2.NORM_MINMAX )
    cv2.imshow("256 Tons", img256)

    img128 = colorReduce(img256, 1)
    cv2.namedWindow("128 Tons",cv2.WINDOW_AUTOSIZE)
    cv2.imshow("128 Tons", img128);
    
    img64 = colorReduce(img256, 2)
    cv2.namedWindow("64 Tons",cv2.WINDOW_AUTOSIZE)
    cv2.imshow("64 Tons", img64);
    
    img32 = colorReduce(img256, 3)
    cv2.namedWindow("32 Tons",cv2.WINDOW_AUTOSIZE)
    cv2.imshow("32 Tons", img32);

    img16 = colorReduce(img256, 4)
    cv2.namedWindow("16 Tons",cv2.WINDOW_AUTOSIZE)
    cv2.imshow("16 Tons", img16);

    img8 = colorReduce(img256, 5)
    cv2.namedWindow("8 Tons",cv2.WINDOW_AUTOSIZE)
    cv2.imshow("8 Tons", img8);

    img4 = colorReduce(img256, 6)
    cv2.namedWindow("4 Tons",cv2.WINDOW_AUTOSIZE)
    cv2.imshow("4 Tons", img4);

    img2 = colorReduce(img256, 7)
    cv2.namedWindow("2 Tons",cv2.WINDOW_AUTOSIZE)
    cv2.imshow("2 Tons", img2);

    cv2.waitKey(0)

    
main()