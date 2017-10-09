import cv2
CV_CAP_PROP_FRAME_WIDTH = 3
CV_CAP_PROP_FRAME_HEIGHT = 4
CV_CAP_PROP_FPS = 5

def main() :
    cap = cv2.VideoCapture(0) #Abre Camera padrão(0)
    cap.set(CV_CAP_PROP_FRAME_WIDTH,640);
    cap.set(CV_CAP_PROP_FRAME_HEIGHT,480);
    cap.set(CV_CAP_PROP_FPS,15);

    if(not cap.isOpened()) : # Se nao conseguir abrir o video, fecha o programa
        return

    cv2.namedWindow("Frame") # Cria uma janela chamada MyVideo

    while(True) :
        ret ,frame = cap.read() # Pega no novo frame do video
        if ret:
            cv2.imshow('Frame',frame) 
            if cv2.waitKey(1) & 0xFF == ord('q'): #Aguarda pelo clique da telca "q" pelo usuario
                break
        else:
            break
            
    cap.release()
    cv2.destroyAllWindows()
    
main()