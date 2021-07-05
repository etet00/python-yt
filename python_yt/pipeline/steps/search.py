from python_yt.pipeline.steps.step import Steps
from python_yt.model.found_key_word import FoundKeyWord


class Search(Steps):
    def process(self, data, inputs, utils):
        found_results = []
        key_word = inputs["search_word"]
        for yt in data:
            subtitles = yt.subtitle
            if not subtitles:
                continue
            for word in subtitles:
                if key_word in word:
                    time = subtitles[word]
                    f = FoundKeyWord(yt, word, time)
                    found_results.append(f)
        # print(len(found_results))
        return found_results

