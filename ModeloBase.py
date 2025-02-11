import tensorflow as tf
from tensorflow.keras import layers, models

# Carregar um modelo base, como o MobileNetV2
base_model = tf.keras.applications.MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights='imagenet')

# Congelar as camadas base
base_model.trainable = False

# Construir a arquitetura do modelo
model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')  # 10 classes (ou pessoas)
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
