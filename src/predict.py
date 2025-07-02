from data_processed import feature_engineering_pipeline
import pandas as pd
import mlflow.sklearn

class PredictModel:
    def __init__(self):
        mlflow.set_tracking_uri(uri='http://127.0.0.1:8080')
        self.model_name = 'linear_credit'
        self.model_version = 'latest'
        self.model_uri = f'models:/{self.model_name}/{self.model_version}'
        self.model = mlflow.sklearn.load_model(self.model_uri)
    def predict(self,data:pd.DataFrame):
        featured_data = feature_engineering_pipeline(data)
        result = self.model.predict(featured_data['processed_data'])
        return result

