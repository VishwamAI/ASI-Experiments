import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.model_selection import GridSearchCV

class DecisionMaking:
    def __init__(self):
        pass

    def evaluate_strategies(self, data, labels):
        """
        Evaluate different decision-making strategies based on the provided data.

        Parameters:
        - data: numpy array or pandas DataFrame
            The data to be used for evaluating strategies.
        - labels: numpy array or pandas Series
            The true labels for the data.

        Returns:
        - dict
            A dictionary containing the evaluation results for each strategy.
        """
        strategies = ['logistic_regression', 'decision_tree', 'svm']
        results = {}
        for strategy in strategies:
            predictions, y_test = self._predict_with_model(data, labels, strategy)
            results[strategy] = {
                'accuracy': accuracy_score(y_test, predictions),
                'precision': precision_score(y_test, predictions, average='weighted'),
                'recall': recall_score(y_test, predictions, average='weighted'),
                'f1_score': f1_score(y_test, predictions, average='weighted')
            }
        return results

    def assess_risks(self, data):
        """
        Assess risks associated with different decisions based on the provided data.

        Parameters:
        - data: numpy array or pandas DataFrame
            The data to be used for risk assessment.

        Returns:
        - dict
            A dictionary containing the risk assessment results for each decision.
        """
        decisions = ['decision_1', 'decision_2', 'decision_3']
        risks = {}
        for decision in decisions:
            risks[decision] = np.var(data) * np.mean(data)  # Example risk calculation
        return risks

    def predict_outcomes(self, data):
        """
        Predict outcomes of different decisions based on the provided data.

        Parameters:
        - data: numpy array or pandas DataFrame
            The data to be used for outcome prediction.

        Returns:
        - dict
            A dictionary containing the predicted outcomes for each decision.
        """
        decisions = ['decision_1', 'decision_2', 'decision_3']
        outcomes = {}
        for decision in decisions:
            outcomes[decision] = float(np.mean(data) + np.std(data))  # Example outcome prediction
        return outcomes

    def _predict_with_model(self, data, labels, model_type):
        """
        Generate predictions using different machine learning models.

        Parameters:
        - data: numpy array or pandas DataFrame
            The data to be used for generating predictions.
        - labels: numpy array or pandas Series
            The true labels for the data.
        - model_type: str
            The type of model to use for predictions.

        Returns:
        - tuple
            A tuple containing the predictions and the true labels for the testing set.
        """
        if model_type == 'logistic_regression':
            model = LogisticRegression(random_state=0)
            param_grid = {'C': [0.1, 1, 10, 100]}
        elif model_type == 'decision_tree':
            model = DecisionTreeClassifier(random_state=0)
            param_grid = {'max_depth': [None, 10, 20, 30]}
        elif model_type == 'svm':
            model = SVC(random_state=0)
            param_grid = {'C': [0.1, 1, 10, 100], 'kernel': ['linear', 'rbf']}
        else:
            raise ValueError(f"Unknown model type: {model_type}")

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=0)

        # Perform hyperparameter tuning using GridSearchCV
        grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy')
        grid_search.fit(X_train, y_train)
        best_model = grid_search.best_estimator_

        # Generate predictions on the testing data
        predictions = best_model.predict(X_test)
        return predictions, y_test
