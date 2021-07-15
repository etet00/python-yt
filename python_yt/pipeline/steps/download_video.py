from pytube import YouTube
from python_yt.pipeline.steps.step import Steps
from python_yt.setting import VIDEOS_DIR


class DownloadVideo(Steps):
    def process(self, data, inputs, utils):
        yt_set = set(found.yt for found in data)
        # print(yt_set)
        for yt in yt_set:
            if utils.check_video_exist(yt.video_filepath):
                print("video files exist")
                continue
            print(f"download video from {yt.url}")
            YouTube(yt.url).streams.get_highest_resolution().download(output_path=VIDEOS_DIR, filename=yt.id)
            print(f"download finnish")
        return data
