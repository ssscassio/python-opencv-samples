import cv2

def main() :
    cap = cv2.VideoCapture(0) #Abre camera Default instalada
    # No Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2.
    # No Windows: DIVX
    # No OSX: MJPG (.mp4), DIVX (.avi), X264 (.mkv).
    fourcc = cv2.VideoWriter_fourcc(*'DIVX') #Especifica o codec do video
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480)) # (fileName, FourCC_code, framesPerSecond, frameSize)
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True: #Verifica se houve retorno em cap.read()
            # frame = cv2.flip(frame,1) #Inverte o video
            out.write(frame) #Escreve o frame
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'): #Aguarda pelo clique da telca "q" pelo usuario
                break
        else:
            break

    # Libera tudo se o trabalho for concluido
    cap.release()
    out.release()
    cv2.destroyAllWindows()

main()