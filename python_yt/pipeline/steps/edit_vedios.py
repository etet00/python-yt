from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips
from moviepy.editor import CompositeVideoClip
from moviepy.editor import TextClip
from moviepy.video.tools.subtitles import SubtitlesClip
from python_yt.pipeline.steps.step import Steps


class EditVideos(Steps):
    def process(self, data, inputs, utils):
        video_list = []
        sub_list = []
        sub_time = 0
        for found in data:
            start_time, end_time = self.parse_time(found.time)
            sub, time_length = self.add_subtitles(found.subtitle, start_time, end_time, sub_time)
            sub_list.append(sub)
            sub_time = time_length
            video = VideoFileClip(found.yt.video_filepath).subclip(start_time, end_time)
            video_list.append(video)
            if len(video_list) >= int(inputs["limit"]):
                break
        generator = lambda txt: TextClip(txt, font="Arial", fontsize=60, color="black")
        subtitles = SubtitlesClip(sub_list, generator).set_position(("center", "bottom"))
        # result = concatenate_videoclips([video_list, subtitles])   # CompositeVideoClip(video_list)
        result = concatenate_videoclips(video_list)
        result = CompositeVideoClip([result, subtitles])
        output_filepath = utils.get_output_filepath(inputs["channel_id"], inputs["search_word"])
        result.write_videofile(output_filepath, fps=30)

        # close video files
        for video in video_list:
            video.close()

        return data

    def parse_time(self, subtitle_time):
        start, end = subtitle_time.split(" --> ")
        return self.parse_sec(start), self.parse_sec(end)

    def parse_sec(self, sec):
        h, m, s = sec.split(":")
        s, ms = s.split(",")
        return int(h), int(m), int(s) + int(ms) / 1000

    def add_subtitles(self, subtitle, start_time, end_time, sub_start_time):
        t1 = self.hms2s(start_time)
        t2 = self.hms2s(end_time)
        duration = t2 - t1
        sub_end_time = sub_start_time + duration
        temp = (sub_start_time, sub_end_time)
        return (temp, subtitle), sub_end_time

    def hms2s(self, tuple_time):
        new_time = tuple_time[0] * 3600 + tuple_time[1] * 60 + tuple_time[2]
        return new_time
