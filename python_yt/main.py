import python_yt.pipeline.steps.step
from python_yt.pipeline.pipeline import Pipeline
from python_yt.pipeline.steps.get_video_list import GetVideoClass

CHANNEL_ID = "UCqTVfT9JQqhA6_Hi_h_h97Q"  # 全域變數通常以全大寫命名
# inputs


def main():
    inputs = {
        "channel_id": CHANNEL_ID
    }
    steps = [
        GetVideoClass(),
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == "__main__":
    main()

# video_list = get_all_video_in_channel(CHANNEL_ID)
# print(len(video_list))
