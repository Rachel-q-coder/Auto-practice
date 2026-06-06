from config import BASE_URL
import requests
import allure
from common.logger_utils import logger
def login(account,pwd):
    url = BASE_URL
    logger.info("请求的url：%s", url)
    allure.attach(url,"请求地址")
    querry_params = {
        "s": "api/user/login",
        "application": "app",
        "application_client_type": "weixin"
    }
    logger.info("请求参数：%s", querry_params)
    allure.attach(url, "请求地址")
    datas = {
        "accounts":account,
        "pwd": pwd,
        "type": "username"
    }
    logger.info("请求体：%s", datas)
    allure.attach(str(datas), "请求")
    response = requests.post(url,data=datas,params=querry_params)
    return response

