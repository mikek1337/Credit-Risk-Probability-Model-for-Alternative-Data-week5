from fastapi import FastAPI, status, HTTPException
from predict import PredictModel
import pandas as pd
from src.api.pydantic_models import TransactionCreate, TransactionResponse
app = FastAPI(
    title="Transaction API",
    description="API for managing and predicting transaction fraud.",
    version="1.0.0")
model = PredictModel()
@app.post('/predict', response_model=TransactionResponse, status_code=status.HTTP_200_OK)
def predict(transaction:TransactionCreate):
    transaction_dict = transaction.model_dump()
    input_df = pd.DataFrame([transaction_dict])
    return model.predict(input_df)

