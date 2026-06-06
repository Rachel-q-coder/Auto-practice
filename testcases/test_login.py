from threading import active_count

import pytest
import requests
import pandas as pd
from api.login_api import login
from common.assert_utils import assert_msg,assert_code,assert_state_code
from common.logger_utils import logger
import allure

@allure.feature("登录模块")
#将读取的excel转换为字典
@allure.story("获取excel测试用例")
def access_excel():
    datas_form = pd.read_excel(r"C:\Users\30493\OneDrive\文档\工作簿1.xlsx", sheet_name="import_excel")
    datas = datas_form.to_dict(orient="records")
    return datas
datas = access_excel()

# ====================== 多个参数进行传值 ======================

@pytest.mark.parametrize("data",datas)
def test_login(data):
    allure.dynamic.title(f"登录用例：{data['account']}")
    account = data["account"]
    pwd = data["pwd"]
    msg = data["msg"]
    allure.attach(str(data).encode("utf-8"), "测试用例")
    logger.info("开始进行登录测试")
    with allure.step("开始登录测试"):
        response = login(account,pwd)
    logger.info("登录测试结束")
    logger.info(f"登录的状态码为：{response.json().get('code')}")
    with allure.step("进行断言阶段"):
        assert_msg(response,msg)
        assert_state_code(response,200)



