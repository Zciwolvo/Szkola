import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import os


def process(f):
    name = os.path.basename(f)
    data = pd.read_csv(f)

    # Label inputs and output
    input = data.iloc[:, :-1].values
    ouput = data.iloc[:, -1].values
    size = len(input)

    # Normalize
    scaler = MinMaxScaler()
    inputs_normalized = scaler.fit_transform(input)

    # Split the dataset
    input_train, input_test, output_train, output_test = train_test_split(
        inputs_normalized,
        ouput,
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
            ouput,
            cv=5,
            scoring="neg_mean_squared_error",
        )
        rmse_scores = (-cv_scores) ** 0.5
        scores[k] = rmse_scores.mean()
        models.append(knn)

    best_k = min(scores, key=scores.get)
    print(
        "k =",
        best_k,
        "\nMean cross-validation score:",
        scores[best_k],
    )

    # Train model with best k
    knn = models[best_k - 1]
    knn.fit(input_train, output_train)

    # Test model
    output_pred = knn.predict(input_test)
    mse = ((output_pred - output_test) ** 2).mean()
    rmse = mse**0.5
    print("Root Mean Squared Error:", rmse)

    dataset_range = (min(output_test), max(output_test))
    with open(f"output/{name}.txt", "w") as f:
        f.write(
            f"Name:\t{name} \nRoot Mean Squared Error:\t{rmse}\nbest k:\t{best_k}\ndata range:\t{dataset_range}\ndataset size:\t{size}\n"
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
    plt.savefig(f"output/{name}.png")
