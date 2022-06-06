from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
import os

def main():
    url = input('URL: ')
    option = input('1 or 2: ')
    if option == '1':
        transcript1(url)
    if option == '2':
        transcript2(url)

def transcript1(url):
    yt = YouTube(url)
    v_id = YouTube.video_id(url)

    transcript_list = YouTubeTranscriptApi.list_transcripts(v_id)
    transcript = transcript_list.find_generated_transcript(['en'])

    file = open(yt.title + '.txt', mode = 'w', encoding='utf_8')

    for d in transcript.fetch():
        text = d['text']
        file.write(text + ' ')

    print(yt.title + " has been successfully downloaded.")

    # reference for transcript1
    # youtube_transcript_api: https://pypi.org/project/youtube-transcript-api/ 
    # the source code: https://github.com/jdepoix/youtube-transcript-api/blob/master/setup.py
    # pytube: https://github.com/pytube/pytube 
    # the source code: https://pytube.io/en/latest/

def transcript2(url):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download()
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print(yt.title + " has been successfully downloaded.")

    # reference for transcript2
    # https://www.geeksforgeeks.org/download-video-in-mp3-format-using-pytube/

if __name__ == "__main__":
    main()