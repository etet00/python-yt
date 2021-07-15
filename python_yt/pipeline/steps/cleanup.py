from shutil import rmtree
from python_yt.pipeline.steps.step import Steps
from python_yt.setting import DOWNLOADS_DIR
from python_yt.setting import OUTPUTS_DIR


class CleanOutput(Steps):
    def process(self, data, inputs, utils):
        if inputs["clean_output"]:
            try:
                print("clean output files")
                rmtree(OUTPUTS_DIR)
            except OSError as e:
                print(e)
            else:
                print("The previous output_directory is deleted successfully")


class CleanDownloadFiles(Steps):
    def process(self, data, inputs, utils):
        if inputs["clean_downloads"]:
            try:
                print("clean download files")
                rmtree(DOWNLOADS_DIR)
            except OSError as e:
                print(e)
            else:
                print("The download_directory is deleted successfully")
