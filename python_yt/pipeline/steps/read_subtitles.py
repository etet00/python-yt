import os
from pprint import pprint
from python_yt.setting import SUBTITLES_DIR
from python_yt.pipeline.steps.step import Steps


class ReadSubtitles(Steps):
    def process(self, data, inputs, utils):
        all_subtitle_dics = {}
        for subtitle_file in os.listdir(SUBTITLES_DIR):
            subtitles_dic = {}
            with open(os.path.join(SUBTITLES_DIR, subtitle_file), "r") as f:
                timeline = False
                # time = None
                # subtitles = None
                for line in f:
                    if "-->" in line:
                        timeline = True
                        time = line.strip()
                        continue
                    if timeline:  # 未寫判斷內容，預設為判斷變數是否為True
                        timeline = False
                        subtitles = line.strip()
                        subtitles_dic[subtitles] = time  # 以字幕當作字典的key，以後面方便進行關鍵字搜索比對
                all_subtitle_dics[subtitle_file] = subtitles_dic
            pprint(all_subtitle_dics)
        return all_subtitle_dics
