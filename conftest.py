import pytest
import requests
from config import BASE_URL,ADMIN,PWD
from api.login_api import login
from common.logger_utils import logger
# ====================== ficture ======================
#获取token
@pytest.fixture(scope="session")
def access_token(login):
    resp = login(ADMIN,PWD)
    token = resp.json().get("data",{}).get("token"," ")
    logger.info("获取的token为: %s",token)
    yield token



