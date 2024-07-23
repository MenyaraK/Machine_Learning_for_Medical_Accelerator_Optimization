from src import load_data, preprocess, train, test, visualize

def main():
    data = load_data.load_data()
    processed_data = preprocess.preprocess_data(data)
    model = train.train_model(processed_data['X_train'], processed_data['y_train'])
    test_results = test.test_model(model, processed_data['X_test'], processed_data['y_test'])
    visualize.plot_results(test_results)

if __name__ == '__main__':
    main()
