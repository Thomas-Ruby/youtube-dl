# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor


class NestIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?video\.nest\.com/clip/(?P<id>\d+)'
    _TEST = {
        'url': 'https://video.nest.com/clip/73ddb6bd57c4485597a76e154a4429ea.mp4',
        'md5': '7ab4eb6d4c2480be1740cc014a76ee96',
        'info_dict': {
            'id': '73ddb6bd57c4485597a76e154a4429ea',
            'ext': 'mp4',
            'title': 'Nest Cam',
            # TODO more properties, either as:
            # * A value
            # * MD5 checksum; start the string with md5:
            # * A regular expression; start the string with re:
            # * Any Python type (for example int or float)
        }
    }

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)
        print("TEST TWO")

        # TODO more code goes here, for example ...
        title = 'Nest Cam'
        video_id = url[28:-4:1]
        print(url)
        print(video_id)
        url_2 = 'https://clips.dropcam.com/' + video_id + '.mp4'
        print(url_2)

        return {
            'id': video_id,
            'title': title,
            'ext': 'mp4',
            'url': url_2
            # TODO more properties (see youtube_dl/extractor/common.py)
        }