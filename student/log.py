import logging
def log():
  logger = logging.getLogger("nick")
  logger.setLevel(logging.DEBUG)

  if not logger.handlers:
    # 创建handler
    fh = logging.FileHandler("test.log", encoding="utf-8")
    ch = logging.StreamHandler()
    # 设置输出的日志格式
    formatter = logging.Formatter(fmt="%(asctime)s %(name)s %(filename)s %(message)s", datefmt="%Y/%m/%d %x")
    # 为handler指定输出格式
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # 为logger添加日志处理器
    logger.addHandler(fh)
    logger.addHandler(ch)

  return logger

logger = log()
logger.warning("警告")
logger.info("信息提示")
logger.error("错误提示")
logger.debug("查错信息")