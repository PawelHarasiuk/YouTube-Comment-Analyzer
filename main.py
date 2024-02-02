from yt_scraper import YTScraper

yt_scraper = YTScraper()

video_id = 'NRZGhYrpmKI'
print(yt_scraper.get_comments(video_id))