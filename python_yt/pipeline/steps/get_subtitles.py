import time
import logging
from multiprocessing import Process
from pytube import YouTube
from python_yt.pipeline.steps.step import Steps


class GetSubtitles(Steps):
    def process(self, data, inputs, utils):
        logger = logging.getLogger(__name__)
        processes = []
        start = time.time()
        for i in range(4):
            processes.append(Process(target=self.download_subtitles(data[i::4], utils, logger)))
        for process in processes:
            process.start()
        for process in processes:
            process.join()
        logger.info(f"Took {time.time() - start} seconds.")  # print(f"Took {time.time() - start} seconds.")
        return data

    def download_subtitles(self, data, utils, logger):
        for yt in data:
            # if utils.check_subtitle_file_exist(yt.url):
            if utils.check_subtitle_file_exist(yt.sub_filepath):
                logger.info("subtitle files exist!")  # print("subtitle files exist!")
                continue

            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
                logger.info(f"downloading subtitle from {yt.url}")  # print("downloading subtitle from\n" + yt.url)
            except AttributeError:
                logger.warning("skips AttributeError")  # print("skips AttributeError")
                continue

            text_file = open(yt.get_subtitle_files_path(), "w", encoding="utf-8")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
