# src/api/pydantic_models.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TransactionCreate(BaseModel):
    # ... (as previously defined) ...
    BatchId: str = Field(..., description="Identifier for the batch the transaction belongs to")
    AccountId: str = Field(..., description="Identifier for the account involved in the transaction")
    SubscriptionId: str = Field(..., description="Identifier for the subscription related to the transaction")
    CustomerId: str = Field(..., description="Identifier for the customer making the transaction")
    CurrencyCode: str = Field(..., min_length=3, max_length=3, description="3-letter ISO currency code (e.g., 'KES', 'USD')")
    CountryCode: int = Field(..., description="Numerical country code")
    ProviderId: str = Field(..., description="Identifier for the transaction provider")
    ProductId: str = Field(..., description="Identifier for the product involved in the transaction")
    ProductCategory: str = Field(..., description="Category of the product")
    ChannelId: str = Field(..., description="Identifier for the transaction channel")
    Amount: float = Field(..., gt=0, description="Monetary amount of the transaction, must be greater than 0")
    Value: int = Field(..., ge=0, description="Numerical value associated with the transaction, non-negative")
    TransactionStartTime: datetime = Field(..., description="Timestamp when the transaction started")
    PricingStrategy: int = Field(..., description="Strategy used for pricing the transaction")

    class Config:
        json_schema_extra = {
            "example": {
                "BatchId": "Batch_XYZ_20230115",
                "AccountId": "ACC_12345",
                "SubscriptionId": "SUB_67890",
                "CustomerId": "CUST_ABCDE",
                "CurrencyCode": "KES",
                "CountryCode": 254,
                "ProviderId": "PROV_A",
                "ProductId": "PROD_001",
                "ProductCategory": "Airtime",
                "ChannelId": "WEB",
                "Amount": 500.75,
                "Value": 500,
                "TransactionStartTime": "2023-01-15T14:30:00",
                "PricingStrategy": 1
            }
        }

class TransactionResponse(BaseModel):
    # ... (as previously defined) ...
    TransactionId: str = Field(..., description="Unique identifier for the transaction")
    BatchId: str
    AccountId: str
    SubscriptionId: str
    CustomerId: str
    CurrencyCode: str
    CountryCode: int
    ProviderId: str
    ProductId: str
    ProductCategory: str
    ChannelId: str
    Amount: float
    Value: int
    TransactionStartTime: datetime
    PricingStrategy: int
    FraudResult: int = Field(..., description="Result of fraud detection (e.g., 0 for not fraud, 1 for fraud)")

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "TransactionId": "TRANS_UUID_12345",
                "BatchId": "Batch_XYZ_20230115",
                "AccountId": "ACC_12345",
                "SubscriptionId": "SUB_67890",
                "CustomerId": "CUST_ABCDE",
                "CurrencyCode": "KES",
                "CountryCode": 254,
                "ProviderId": "PROV_A",
                "ProductId": "PROD_001",
                "ProductCategory": "Airtime",
                "ChannelId": "WEB",
                "Amount": 500.75,
                "Value": 500,
                "TransactionStartTime": "2023-01-15T14:30:00",
                "PricingStrategy": 1,
                "FraudResult": 0
            }
        }