import os
import json
import youtube_dl

def extract_format_data(format_data):
    extension = format_data["ext"]
    format_name = format_data["format"]
    url = format_data["url"]
    return {
        "extension": extension,
        "format_name": format_name,
        "url": url
    } 
def extract_video_data_from_url(url):
    command = f'youtube-dl "{url}" -j'
    output = os.popen(command).read()
    video_data = json.loads(output)
    title = video_data['title']
    formats = video_data['formats']
    thumbnail = video_data["thumbnails"]
    formats = [extract_format_data(format_data) for format_data in formats]
    return {
        "title":title,
        "formats":formats,
        "thumbnail":thumbnail
    }

extract_video_data_from_url("https://www.dailymotion.com/video/x938sqm")