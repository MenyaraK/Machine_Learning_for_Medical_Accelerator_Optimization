from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
from config import MODEL_PATH, PLOT_PATH

def evaluate_model(X_test_normalized, y_test):
    model = load_model(MODEL_PATH)
    loss = model.evaluate(X_test_normalized, y_test)
    print("Test loss:", loss)
    return loss

def make_predictions(X_test_normalized):
    model = load_model(MODEL_PATH)
    predictions = model.predict(X_test_normalized)
    return predictions

def plot_predictions(y_test, predictions):
    plt.figure(figsize=(10, 6))
    plt.scatter(range(len(y_test)), y_test, color='blue', label='Actual')
    plt.scatter(range(len(predictions)), predictions, color='red', label='Predicted', alpha=0.5)
    plt.title('Comparison of Actual and Predicted Values')
    plt.xlabel('Sample Index')
    plt.ylabel('Energy')
    plt.legend()
    plt.savefig(PLOT_PATH + 'predictions_comparison.png')
    plt.show()
