import logging
from shutil import rmtree
from python_yt.pipeline.steps.step import Steps
from python_yt.setting import DOWNLOADS_DIR
from python_yt.setting import OUTPUTS_DIR


class CleanOutput(Steps):
    def process(self, data, inputs, utils):
        logger = logging.getLogger(__name__)
        if inputs["clean_output"]:
            try:
                logger.info("clean output files")  # print("clean output files")
                rmtree(OUTPUTS_DIR)
            except OSError as e:
                logger.warning(e)  # print(e)
            else:
                logger.info("The previous output_directory is deleted successfully")


class CleanDownloadFiles(Steps):
    def process(self, data, inputs, utils):
        logger = logging.getLogger(__name__)
        if inputs["clean_downloads"]:
            try:
                logger.info("clean download files")  # print("clean download files")
                rmtree(DOWNLOADS_DIR)
            except OSError as e:
                logger.warning(e)  # print(e)
            else:
                logger.info("The download_directory is deleted successfully")
