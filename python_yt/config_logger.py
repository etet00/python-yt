import logging


def config_log(level):
    logger = logging.getLogger()
    logger.setLevel(logging.NOTSET)
    log_level = int(level) * 10

    # 設定輸出格式
    formatter = logging.Formatter('%(name)-8s: %(levelname)-8s: %(filename)-8s: %(asctime)-23s: %(message)s')

    # 定義 handler 輸出 log 檔案
    file_handler = logging.FileHandler('run_info.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # 定義 handler 輸出螢幕
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(log_level)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
