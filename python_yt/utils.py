import os

from python_yt.setting import DOWNLOADS_DIR
from python_yt.setting import VIDEOS_DIR
from python_yt.setting import SUBTITLES_DIR
from python_yt.setting import OUTPUTS_DIR

class Utils:
    def __init__(self):
        pass

    def create_dirs(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(SUBTITLES_DIR, exist_ok=True)
        os.makedirs(OUTPUTS_DIR, exist_ok=True)

    def get_video_link_list_path(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + ".txt")

    def check_video_link_list_exist(self, channel_id):
        path = self.get_video_link_list_path(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    def check_subtitle_file_exist(self, path):
        # path = self.get_subtitle_files_path(url)
        return os.path.exists(path) and os.path.getsize(path) > 0

    def check_video_exist(self, path):
        # path = yt.video_filepath()
        return os.path.exists(path) and os.path.getsize(path) > 0

    def get_output_filepath(self, channel_id, search_word):
        filename = channel_id + "_" + search_word + ".mp4"
        return os.path.join(OUTPUTS_DIR, filename)
