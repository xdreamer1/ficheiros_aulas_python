# importar a biblioteca OpenCV, utilizada para processamento de imagem e vídeo
import cv2

# mostrar no terminal a versão instalada do OpenCV
print(cv2.__version__)

# abrir a câmara do computador
# o valor 0 indica a webcam principal
video_capture = cv2.VideoCapture(0)

# carregar o classificador Haar Cascade para deteção de rostos
# este ficheiro XML já vem incluído no OpenCV
faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# carregar o classificador Haar Cascade para deteção de olhos
eyeCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml'
)

# carregar o classificador Haar Cascade para deteção de sorrisos
smileCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_smile.xml'
)

# iniciar um ciclo infinito para capturar vídeo em tempo real
while True:

    # ler uma frame (imagem) da webcam
    # ret indica se a captura foi bem-sucedida
    # frame contém a imagem capturada
    ret, frame = video_capture.read()

    # converter a imagem de cores (BGR) para escala de cinzentos
    # isto melhora o desempenho da deteção
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detetar rostos na imagem em tons de cinzento
    faces = faceCascade.detectMultiScale(
        gray,              # imagem onde será feita a deteção
        scaleFactor=1.1,   # fator de redução da imagem em cada escala
        minNeighbors=5,    # número mínimo de vizinhos para validar deteção
        minSize=(30, 30)   # tamanho mínimo do objeto a detetar
    )

    # percorrer todos os rostos detetados
    for (x, y, w, h) in faces:

        # desenhar um retângulo verde à volta do rosto
        # (x,y) = canto superior esquerdo
        # (x+w,y+h) = canto inferior direito
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # detetar olhos na imagem em tons de cinzento
    eyes = eyeCascade.detectMultiScale(gray, 1.2, 18)

    # percorrer todos os olhos detetados
    for (x, y, w, h) in eyes:

        # desenhar um retângulo azul à volta dos olhos
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # detetar sorrisos na imagem
    smiles = smileCascade.detectMultiScale(gray, 1.7, 20)

    # percorrer todos os sorrisos detetados
    for (x, y, w, h) in smiles:

        # desenhar um retângulo vermelho à volta do sorriso
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # mostrar a frame com as deteções numa janela chamada "video"
    cv2.imshow('video', frame)

    # esperar 1 milissegundo por uma tecla
    # se a tecla pressionada for "q", termina o programa
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# libertar a webcam após terminar
video_capture.release()

# fechar todas as janelas abertas pelo OpenCV
cv2.destroyAllWindows()