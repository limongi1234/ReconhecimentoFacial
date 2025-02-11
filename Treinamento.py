# Treinamento
model.fit(train_data, epochs=10)


cap = cv2.VideoCapture(0)  # Usa a webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detectar faces
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        face_resized = cv2.resize(face, (224, 224))  # Tamanho adequado para o classificador
        prediction = model.predict(face_resized)

        # Exibir resultado
        cv2.putText(frame, str(prediction), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 0), 2)

        # Desenhar o retângulo
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Face Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
