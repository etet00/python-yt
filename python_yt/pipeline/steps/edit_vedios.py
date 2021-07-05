from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips
from python_yt.pipeline.steps.step import Steps


class EditVideos(Steps):
    def process(self, data, inputs, utils):
        video_list = []
        for found in data:
            start_time, end_time = self.parse_time(found.time)
            video = VideoFileClip(found.yt.video_filepath).subclip(start_time, end_time)
            video_list.append(video)
            if len(video_list) >= int(inputs["limit"]):
                break
        result = concatenate_videoclips(video_list)   # CompositeVideoClip(video_list)  # Overlay text on video
        output_filepath = utils.get_output_filepath(inputs["channel_id"], inputs["limit"])
        result.write_videofile(output_filepath, fps=30)
        return data

    def parse_time(self, subtitle_time):
        start, end = subtitle_time.split(" --> ")
        return self.parse_sec(start), self.parse_sec(end)

    def parse_sec(self, sec):
        h, m, s = sec.split(":")
        s, ms = s.split(",")
        return int(h), int(m), int(s) + int(ms) / 1000
