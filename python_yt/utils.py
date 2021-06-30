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

    def check_video_link_list_exist(self, channel_id):
        path = self.get_video_link_list_path(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    @staticmethod
    def get_id_from_url(url):
        return url.split("watch?v=")[-1]

    def get_subtitle_files_path(self, url):
        return os.path.join(SUBTITLES_DIR, self.get_id_from_url(url) + ".txt")

    def check_subtitle_file_exist(self, url):
        path = self.get_subtitle_files_path(url)
        return os.path.exists(path) and os.path.getsize(path) > 0
