from data_processed import feature_engineering_pipeline
import mlflow
import 
from mlflow.models import infer_signature
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
class TrainModel:
    def __init__(self):
        mlflow.set_tracking_uri(uri='http://127.0.0.1:8080')
        self.feat_data = feature_engineering_pipeline()
        self.data = self.feat_data['processed_data']
        if self.data is pd.