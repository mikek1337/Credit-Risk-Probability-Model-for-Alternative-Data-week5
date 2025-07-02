import pandas as pd
import mlflow.sklearn
import os
import joblib
current_dir = os.path.dirname(os.path.abspath(__file__))
model_artifacts_dir = os.path.join(current_dir, '../full_feat_pipeline/full_feature_pipeline.joblib')
PIPELINE_PATH = model_artifacts_dir 
class PredictModel:
    def __init__(self):
        mlflow.set_tracking_uri(uri='http://127.0.0.1:8080')
        self.model_name = 'tracking-linear_credit'
        self.model_version = 'latest'
        self.model_uri = f'models:/{self.model_name}/{self.model_version}'
        self.model = mlflow.sklearn.load_model(self.model_uri)
        self.pipeline = None
        self.load_pipeline()

    def load_pipeline(self):
        try:
            self.pipeline = joblib.load(PIPELINE_PATH)
        except FileNotFoundError:
            print(f"File not {PIPELINE_PATH}")
        
    def predict(self,data:pd.DataFrame):
        featured_data = self.pipeline.transform(data)
        result = self.model.predict(featured_data)
        return result

