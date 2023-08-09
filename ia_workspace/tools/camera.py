import cv2

def camera():
    # Inicializa o objeto para acessar a câmera (0 representa a câmera padrão do notebook)
    cap = cv2.VideoCapture(0)

    while True:
        # Lê o próximo frame do fluxo de vídeo
        ret, frame = cap.read()

        # Exibe o frame na janela
        cv2.imshow('Camera', frame)

        # Verifica se a tecla 'q' foi pressionada para sair do loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera os recursos
    cap.release()
    cv2.destroyAllWindows()

def showCamera():
    return 0
camera()