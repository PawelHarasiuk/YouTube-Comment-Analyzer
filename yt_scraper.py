import googleapiclient.discovery


class YTScraper:
    def __init__(self):
        self.API_KEY = 'AIzaSyDzm6Wz7T-KaV2tS2p79-jRMRTh2P2nJy4'
        self.youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=self.API_KEY)

    def get_comments(self, video_id):
        comments = []
        request = self.youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            textFormat='plainText',
            maxResults=100
        )

        while request:
            response = request.execute()
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                comments.append(comment)

            request = self.youtube.commentThreads().list_next(request, response)

        return comments
