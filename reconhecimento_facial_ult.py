from ultralytics import YOLO
import cv2

modelo = YOLO("yolov8n.pt")

camera = cv2.VideoCapture(0)

while True:

    ret, frame = camera.read()

    resultados = modelo(frame)

    imagem = resultados[0].plot()

    cv2.imshow("YOLO", imagem)

    if cv2.waitKey(1) == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()