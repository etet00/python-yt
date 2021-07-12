import time
# from multiprocessing import Process
from threading import Thread
from pytube import YouTube
from python_yt.pipeline.steps.step import Steps


class GetSubtitles(Steps):
    def process(self, data, inputs, utils):
        # processes = []
        threads = []
        start = time.time()
        for yt in data:
            # if utils.check_subtitle_file_exist(yt.url):
            if utils.check_subtitle_file_exist(yt.sub_filepath):
                print("subtitle files exist!")
                continue
            # processes.append(Process(target=self.download_subtitles(yt)))
            threads.append(Thread(target=self.download_subtitles(yt)))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        print(f"Took {time.time() - start} seconds.")
        return data

    def download_subtitles(self, yt):
        try:
            source = YouTube(yt.url)
            en_caption = source.captions.get_by_language_code('a.en')
            en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            print("downloading subtitle from\n" + yt.url)
        except AttributeError:
            print("skips AttributeError")
            return
        # print(en_caption_convert_to_srt)
        text_file = open(yt.get_subtitle_files_path(), "w", encoding="utf-8")
        text_file.write(en_caption_convert_to_srt)
        text_file.close()
