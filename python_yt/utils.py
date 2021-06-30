import os

from python_yt.setting import DOWNLOADS_DIR
from python_yt.setting import VIDEOS_DIR
from python_yt.setting import SUBTITLES_DIR


class Utils:
    def __init__(self):
        pass

    def create_dirs(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(SUBTITLES_DIR, exist_ok=True)

    def get_video_link_list_path(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + ".txt")

    def video_link_list_exist(self, channel_id):
        path = self.get_video_link_list_path(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0
