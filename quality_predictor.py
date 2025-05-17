import tensorflow as tf
import numpy as np

class QualityMetricsPredictor:
    def __init__(self):
        self.model = self._build_model()

    def _build_model(self):
        """Build and compile the neural network model"""
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='relu', input_shape=(3,)),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(3, activation='linear')
        ])
        
        model.compile(
            optimizer='adam',
            loss='mse',
            metrics=['mae']
        )
        return model

    def train(self, X_train, y_train, epochs=100, batch_size=32):
        """Train the model with experimental data"""
        self.model.fit(
            X_train, 
            y_train, 
            epochs=epochs, 
            batch_size=batch_size,
            validation_split=0.2
        )

    def predict(self, approx_metrics):
        """Predict true quality metrics from approximated ones"""
        return self.model.predict(np.array(approx_metrics))