import xgboost as xgb

class Classifiers:

    def XGB_classifier(X, y):
        """
        Fit a XGBoost Classifier and return the fitted model
        and parameters.
        
        Parameters
        ----------
        X : pd.DataFrame()
            Dataframe that contains X data.
        
        y: pd.Series()
            Series that contains the target columns.
        """

        model = xgb.XGBClassifier()
        
        model.fit(X, y)

        pred = model.predict(X)
        params = model.get_params()
        feature_importance = model.feature_importances_

        results =   {
                        'predictions': pred,
                        'parameters': params,
                        'feature_importance': feature_importance
                    }

        return model, results