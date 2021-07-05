import os
from python_yt.setting import SUBTITLES_DIR
from python_yt.setting import VIDEOS_DIR


class YT:
    def __init__(self, url):
        self.url = url
        self.id = self.get_id_from_url(url)
        self.sub_filepath = self.get_subtitle_files_path()
        self.video_filepath = self.get_video_files_path()
        self.subtitle = None

    @staticmethod
    def get_id_from_url(url):
        return url.split("watch?v=")[-1]

    def get_subtitle_files_path(self):
        return os.path.join(SUBTITLES_DIR, self.id + ".txt")

    def get_video_files_path(self):
        return os.path.join(VIDEOS_DIR, self.id + ".mp4")

    def __str__(self):
        return "<YT(" + str(self.id) + ")>"

    def __repr__(self):
        contain=":".join([
            "url=" + str(self.url),
            "id=" + str(self.id),
            "subtitle_filepath=" + str(self.sub_filepath),
            "video_filepath=" + str(self.video_filepath),
        ])
        return "<Found" + contain + ")>"