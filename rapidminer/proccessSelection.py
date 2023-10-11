import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.feature_selection import SelectKBest, f_regression, VarianceThreshold
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import os


def process(f):
    name = os.path.basename(f)
    data = pd.read_csv(f)

    # Label inputs and output
    inputs = data.iloc[:, :-1].values
    outputs = data.iloc[:, -1].values
    size = len(inputs)

    # Original model without any selection
    process_case(inputs, outputs, size, name, "a")

    # Feature selection with feature filter
    selected_features = feature_filter(inputs, threshold=0.1)
    process_case(selected_features, outputs, size, name, "b")

    # Vector selection
    selected_vectors = vector_selection(inputs, outputs, k="all")
    process_case(selected_vectors, outputs, size, name, "c")

    # Feature and vector selection
    selected_features_vectors = vector_selection(selected_features, outputs, k="all")
    process_case(selected_features_vectors, outputs, size, name, "d")


def process_case(inputs, outputs, size, name, case):
    # Normalize
    scaler = MinMaxScaler()
    inputs_normalized = scaler.fit_transform(inputs)

    # Split the dataset
    input_train, input_test, output_train, output_test = train_test_split(
        inputs_normalized,
        outputs,
        test_size=0.2,
        random_state=42,
        # shuffle = False # (if same order is required)
    )

    # Train model
    scores = {}
    models = []
    for k in range(1, 21):
        knn = KNeighborsRegressor(n_neighbors=k)
        cv_scores = cross_val_score(
            knn,
            inputs_normalized,
            outputs,
            cv=5,
            scoring="neg_mean_squared_error",
        )
        rmse_scores = (-cv_scores) ** 0.5
        scores[k] = rmse_scores.mean()
        models.append(knn)

    best_k = min(scores, key=scores.get)
    print(f"Case {case}: k = {best_k}, Mean cross-validation score: {scores[best_k]}")

    # Train model with best k
    knn = models[best_k - 1]
    knn.fit(input_train, output_train)

    # Test model
    output_pred = knn.predict(input_test)
    mse = ((output_pred - output_test) ** 2).mean()
    rmse = mse**0.5
    print(f"Case {case}: Root Mean Squared Error: {rmse}")

    dataset_range = (min(output_test), max(output_test))
    with open(f"./output2/{name}_{case}.txt", "w") as f:
        f.write(
            f"Name: {name}\nCase: {case}\nRoot Mean Squared Error: {rmse}\nbest k: {best_k}\ndata range: {dataset_range}\ndataset size: {size}\n"
        )
        f.write(f"Predicted Data\tRaw Data\n")
        for i in range(len(output_pred)):
            f.write("{:.2f}\t{:.2f}\n".format(output_pred[i], output_test[i]))

    # plot displaying comparison of data
    plt.clf()
    plt.scatter(output_test, output_pred)
    plt.xlabel("True Values")
    plt.ylabel("Predictions")
    plt.axis("equal")
    plt.xlim(plt.xlim())
    plt.ylim(plt.ylim())
    plt.plot([-100000, 100000], [-100000, 100000])
    plt.savefig(f"output2/{name}_{case}.png")


def feature_filter(inputs, threshold):
    # Perform feature filtering using VarianceThreshold
    selector = VarianceThreshold(threshold=threshold)
    selected_features = selector.fit_transform(inputs)
    return selected_features


def vector_selection(inputs, outputs, k):
    # Perform vector selection using SelectKBest and f_regression
    selector = SelectKBest(score_func=f_regression, k=k)
    selected_vectors = selector.fit_transform(inputs, outputs)
    return selected_vectors
