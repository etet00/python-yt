import urllib.request
import json

from python_yt.pipeline.steps.step import Steps
from python_yt.setting import API_KEY


class GetVideoClass(Steps):     # 物件取名通常不會家底線，以開頭第一個大寫作為不同單字的區隔
    def process(self, data, inputs, utils):  # 因為抽象類別的關係，其子物件必須繼承父物件的類別方法
        channel_id = inputs["channel_id"]
        if utils.check_video_link_list_exist(channel_id):
            return self.read_video_list(utils.get_video_link_list_path(channel_id))

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(API_KEY, channel_id)

        video_links = []
        url = first_url
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except KeyError:
                break
            # print(video_links)
        self.write_video_list(video_links, utils.get_video_link_list_path(channel_id))
        return video_links

    def write_video_list(self, video_links, filepath):
        with open(filepath, "w") as f:
            for url in video_links:
                f.write(url + "\n")

    def read_video_list(self, filepath):
        video_links = []
        with open(filepath, "r") as f:
            for url in f:
                video_links.append(url.strip())  # .strip()是用來將url前後的空格去掉
        return video_links
