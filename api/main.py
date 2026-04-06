from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from api.inference import evaluate_risk
from api.rate_limiter import is_rate_limited

app = FastAPI(title="Transaction Risk API")

class Transaction(BaseModel):
    user_id: str
    amount: float
    user_age_days: int

@app.post("/api/evaluate")
async def evaluate_transaction(tx: Transaction):
    # 1. Check Redis Rate Limiter (Sub-5ms)
    if is_rate_limited(tx.user_id):
        raise HTTPException(status_code=429, detail="Too Many Requests. Suspicious activity blocked.")
    
    # 2. Run ML Inference
    risk_status = evaluate_risk(tx.amount, tx.user_age_days)
    
    # 3. (Mock) Save to PostgreSQL audit log here
    # database.log_transaction(tx.user_id, tx.amount, risk_status)
    
    return {
        "transaction_id": "tx_12345",
        "risk_assessment": risk_status
    }