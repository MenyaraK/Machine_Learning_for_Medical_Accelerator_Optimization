from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from config import MODEL_PATH

def train_model(X_train, y_train):
    model = keras.Sequential([
        layers.Dense(10, activation='relu', input_shape=(3,)),
        # Add the rest of your model layers here
    ])
    # Compile, train, and save the model
    model.save(MODEL_PATH)
    return model
