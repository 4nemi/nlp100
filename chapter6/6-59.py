#grid searchをする
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn import ensemble
from sklearn.model_selection import GridSearchCV
import joblib

if __name__ == "__main__":
    df = pd.read_csv('train.feature.txt', sep='\t')
    X_train = df.drop('CATEGORY', axis=1)
    Y_train = df['CATEGORY']

    df = pd.read_csv('valid.feature.txt', sep='\t')
    X_valid = df.drop('CATEGORY', axis=1)
    Y_valid = df['CATEGORY']

    classifier = ensemble.RandomForestClassifier(n_jobs=-1, random_state=42)

    param_grid = {
        'n_estimators': [10, 50, 100, 200],
        'max_depth': [1, 3, 5, 10, 20, 50, 100],
        "criterion": ["gini", "entropy"]
    }

    model = GridSearchCV(
        estimator=classifier,
        param_grid=param_grid,
        scoring='accuracy',
        verbose=2,
        n_jobs=-1,
        cv=5
    )
    
    model.fit(X_train, Y_train)
    print(f"Best score: {model.best_score_}")

    print(f"Best parameters set:")
    best_parameters = model.best_estimator_.get_params()
    for param_name in sorted(param_grid.keys()):
        print(f"{param_name}: {best_parameters[param_name]}")
    
    joblib.dump(model, 'model.joblib')