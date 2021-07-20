import logging
from pytube import YouTube
from python_yt.pipeline.steps.step import Steps
from python_yt.setting import VIDEOS_DIR


class DownloadVideo(Steps):
    def process(self, data, inputs, utils):
        logger = logging.getLogger(__name__)
        yt_set = set(found.yt for found in data)
        # print(yt_set)
        for yt in yt_set:
            if utils.check_video_exist(yt.video_filepath):
                logger.info("video files exist")  # print("video files exist")
                continue
            logger.info(f"download video from {yt.url}")  # print(f"download video from {yt.url}")
            YouTube(yt.url).streams.get_highest_resolution().download(output_path=VIDEOS_DIR, filename=yt.id)
            logger.info(f"download finnish")  # print(f"download finnish")
        return data
