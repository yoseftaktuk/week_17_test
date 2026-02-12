
from fastapi import FastAPI, HTTPException, APIRouter
import  qury
app = FastAPI()
router = APIRouter()
my_qury = qury.Mysql_Service()

@router.get('/analytics/top-customers')
def get_top():
    try:
        return my_qury.get_top_10()
    except HTTPException as e:
        return str(e)
@router.get('/analytics/customers-without-orders')
def customers_without_orders():
    try:
        return my_qury.get_customers_without_orders()
    except HTTPException as e:
        return str(e)
@router.get('/analytics/zero-credit-active-customers')
def get_zero_credit_active_customers():
    try:
        return my_qury.zero_credit_active_customers()
    except HTTPException as e:
        return str(e)