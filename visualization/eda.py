def create_train_test_hists(x_train, x_test):
    """Plots histograms for column comparison bewteen the train and test set. Useful to find inbalances in the dataset.

    Args:
        x_train ([type]): [description]
        x_test ([type]): [description]
    """
    columns = x_train.columns

    plt.figure(figsize=(10, 100))
    for i, col in enumerate(columns[:-1]):
        plt.subplot(34, 3, i + 1)
        plt.hist(x=x_train[col], bins=25, color="teal", label="train")
        plt.hist(x=x_test[col], bins=25, color="azure", alpha=0.5, label="test")
        plt.title(f"{col}")
        plt.xticks(rotation=45)
        plt.legend()
    plt.tight_layout()
