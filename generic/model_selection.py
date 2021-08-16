"""
This script contains a clean blueprint to setup GridSearch cross-validation.
"""
from sklearn import model_selection
from skearn import ensemble, neighbors

import matplotlib.pyplot as plt

# define a list that will contain the models you want to test
models = []
models.append(("RandomForest", ensemble.RandomForestClassifier()))
models.append(("KNC", neighbors.KNeighborsClassifier()))

# define number of folds
n_folds = 5
results = []
names = []

# iterate through every tuple specified in the previosu list 
for name, model in models:
    kfold = model_selection.KFold(n_splits=n_folds)
    print("Testing model:", name)
    # remember to update the scoring function
    cv_results = model_selection.cross_val_score(
        model, X_train, y_train, cv=kfold, scoring="f1_weighted", verbose=0, n_jobs=-1
    )
    results.append(cv_results)
    names.append(name)
    msg = f"{name}, {cv_results.mean()}, {cv_results.std()}"
    print(msg + "\n")

# boxplot algorithm comparison
fig = plt.figure(figsize=(12, 7))
fig.suptitle("Algorithm Comparison")
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()
