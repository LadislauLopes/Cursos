# import cv2

# # Carrega o classificador pré-treinado para detecção de faces
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# # Inicializa a captura de vídeo da webcam
# video_capture = cv2.VideoCapture(0)

# while True:
#     # Lê o frame da captura de vídeo
#     ret, frame = video_capture.read()
    
#     # Converte o frame para escala de cinza
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
#     # Detecta os rostos no frame
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
#     # Desenha um quadrado verde em torno de cada rosto detectado
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
#     # Exibe o vídeo resultante
#     cv2.imshow('Video', frame)
    
#     # Verifica se a tecla 'q' foi pressionada para sair do loop
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# video_capture.release()
# cv2.destroyAllWindows()


print('''ESTAGIÁRIO • SCRETARIA DE EDUCAÇÃO • (11/19 – 12/21)
FUNCIONÁRIO EFETIVO • SUATS SEGURANÇA • (05/22 – 9/22) '''.capitalize())