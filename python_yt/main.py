from python_yt.pipeline.pipeline import Pipeline
from python_yt.utils import Utils
from python_yt.pipeline.steps.mk_dir import DirCreate
from python_yt.pipeline.steps.get_video_list import GetVideoClass
from python_yt.pipeline.steps.yt_instance import TYInstance
from python_yt.pipeline.steps.get_subtitles import GetSubtitles
from python_yt.pipeline.steps.read_subtitles import ReadSubtitles

CHANNEL_ID = "UCqTVfT9JQqhA6_Hi_h_h97Q"  # 全域變數通常以全大寫命名
# inputs


def main():
    inputs = {
        "channel_id": CHANNEL_ID
    }
    steps = [
        DirCreate(),
        GetVideoClass(),
        TYInstance(),
        GetSubtitles(),
        ReadSubtitles(),
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == "__main__":
    main()

# video_list = get_all_video_in_channel(CHANNEL_ID)
# print(len(video_list))
