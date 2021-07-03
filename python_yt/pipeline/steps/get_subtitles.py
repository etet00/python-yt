from pytube import YouTube
from python_yt.pipeline.steps.step import Steps


class GetSubtitles(Steps):
    def process(self, data, inputs, utils):
        for yt in data:
            # if utils.check_subtitle_file_exist(yt.url):
            if utils.check_subtitle_file_exist(yt.sub_filepath):
                print("subtitle files exist!")
                continue
            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
                print("downloading subtitle from\n" + yt.url)
            except AttributeError:
                print("skips AttributeError")
                continue
            # print(en_caption_convert_to_srt)
            text_file = open(yt.get_subtitle_files_path(), "w", encoding="utf-8")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
        return data
