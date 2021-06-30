from python_yt.pipeline.steps.step import Steps
from python_yt.pipeline.steps.step import StepException


class DirCreate(Steps):
    def process(self, data, inputs, utils):
        utils.create_dirs()
