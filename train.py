import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split


def parse_game_data(filename):
    problems = []
    results = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) == 4:
                problem, user_answer, correct_answer, correct = parts
                problems.append(problem)
                results.append(int(correct))
    return problems, results


def preprocess_data(problems, results):
    # Extract features from problems
    features = []
    for problem in problems:
        parts = problem.split()
        if len(parts) == 3:
            num1, op, num2 = parts
            features.append([int(num1), int(num2), ord(op)])

    return np.array(features), np.array(results)


def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(10, activation='relu', input_shape=(3,)),
        tf.keras.layers.Dense(5, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model


def train_model(model, X_train, y_train):
    model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2, verbose=0)


def main():
    # Parse the game data
    problems, results = parse_game_data('game_data.txt')

    # Preprocess the data
    X, y = preprocess_data(problems, results)

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the model
    model = create_model()
    train_model(model, X_train, y_train)

    # Evaluate the model on test data
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f"Test set accuracy: {accuracy:.2f}")

    # Make predictions on sample problems
    sample_problems = [
        "2 + 2",
        "10 - 7",
        "43 * 68",
        "11 % 18",
        "6 + 3",
        "15 + 29",
        "75 - 30",
        "96 + 4",
        "100 - 47",
        "8 * 7",
        "12 * 15",
        "5 % 2",
        "100 % 33",
        "23 + 11",
        "67 + 89",
        "58 - 22",
        "89 * 45",
        "76 * 3",
        "81 % 8",
        "44 + 9",
        "19 - 12",
        "17 * 13",
        "100 % 17",
        "45 + 15",
        "38 - 7",
        "7 * 9",
        "72 % 5",
        "9 + 14",
        "63 - 27",
        "14 * 6",
        "89 % 10",
        "55 + 28",
        "99 - 63",
        "5 * 23",
        "91 % 7",
        "34 + 61",
        "77 - 35",
        "12 * 12",
        "123 % 10",
        "2 + 6",
        "5 - 3",
        "17 * 7",
        "65 % 4",
        "28 + 19",
        "50 - 40",
        "33 * 11",
        "150 % 13",
        "4 + 18",
        "75 - 48",
        "22 * 13",
        "85 % 6",
        "3 + 9",
        "90 - 75",
        "99 * 33",
        "19 % 5"
    ]

    # Predict the probability for each sample problem
    for problem in sample_problems:
        parts = problem.split()
        num1, op, num2 = parts
        input_data = np.array([[int(num1), int(num2), ord(op)]])
        prediction = model.predict(input_data)[0][0]
        print(f"Problem: {problem}")
        print(f"Probability of correct answer: {prediction:.2f}")
        print()


if __name__ == "__main__":
    main()
