from python_yt.command_line_argu_fun import command_fun
from python_yt.pipeline.pipeline import Pipeline
from python_yt.utils import Utils
from python_yt.pipeline.steps.mk_dir import DirCreate
from python_yt.pipeline.steps.get_video_list import GetVideoClass
from python_yt.pipeline.steps.yt_instance import TYInstance
from python_yt.pipeline.steps.get_subtitles import GetSubtitles
from python_yt.pipeline.steps.read_subtitles import ReadSubtitles
from python_yt.pipeline.steps.search import Search
from python_yt.pipeline.steps.download_video import DownloadVideo
from python_yt.pipeline.steps.edit_vedios import EditVideos

CHANNEL_ID = "UCqTVfT9JQqhA6_Hi_h_h97Q"  # 全域變數通常以全大寫命名


def main():
    inputs = {
        "channel_id": CHANNEL_ID,
        "search_word": "sexy move",
        "limit": "20",
        "cleanup": False,
    }
    steps = [
        DirCreate(),
        GetVideoClass(),
        TYInstance(),
        GetSubtitles(),
        ReadSubtitles(),
        Search(),
        DownloadVideo(),
        EditVideos(),
    ]

    inputs = command_fun(inputs)
    # print(inputs)
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == "__main__":
    main()
