import xgboost as xgb

class Classifiers:

    def XGB_classifier(X, y):
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