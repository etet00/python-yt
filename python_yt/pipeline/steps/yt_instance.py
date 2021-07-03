from python_yt.pipeline.steps.step import Steps
from python_yt.model.yt import YT


class TYInstance(Steps):
    def process(self, data, inputs, utils):
        return [YT(url) for url in data]
