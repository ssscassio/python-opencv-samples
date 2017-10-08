import cv2
CV_CAP_PROP_POS_FRAMES = 0
CV_CAP_PROP_FRAME_COUNT = 7

def main() :
    cap = cv2.VideoCapture('Megamind.avi') #Abre o video para leitura

    if(not cap.isOpened()) : # Se nao conseguir abrir o video, fecha o programa
        print "Cannot open the video file"
        return

    fps = cap.get(cv2.CAP_PROP_FPS) # Pega o frames por segundo do video
    print "Frames per second : {0}".format(fps)
    cv2.namedWindow("MyVideo") # Cria uma janela chamada MyVideo

    frame_counter = 0
    
    while(True) :
        ret ,frame = cap.read() # Pega no novo frame do video
        frame_counter += 1

        if (frame_counter == cap.get(CV_CAP_PROP_FRAME_COUNT)) :
             frame_counter = 0;
             cap.set(CV_CAP_PROP_POS_FRAMES, 0); # Define o video de volta ao frame inicial

        if ret :
            cv2.imshow('MyVideo',frame) # Mostra o frame na janela "MyVideo"
            cv2.waitKey(1)
        else :
            break
            
    cap.release()
    cv2.destroyAllWindows()
    
main()