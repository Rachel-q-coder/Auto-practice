import logging

# ====================== 日志编辑 ======================
#创建日志器
logger = logging.getLogger("test_api")
logger.setLevel(logging.INFO)
#创建控制器和模式器
console_handler = logging.StreamHandler()
#file_handler = logging.FileHandler("test.log",encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s -%(message)s")

#进行绑定
console_handler.setFormatter(formatter)
#file_handler.setFormatter(formatter)
logger.addHandler(console_handler)
#logger.addHandler(file_handler)