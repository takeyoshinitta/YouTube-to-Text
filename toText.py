from youtube_transcript_api import YouTubeTranscriptApi

def main():
    url = input('URL: ')
    v_id = url[-11:]
    transcript(v_id)

def transcript(v_id):
    transcript_list = YouTubeTranscriptApi.list_transcripts(v_id)

    file = open(v_id + '.txt', mode='w', encoding='utf_8')
    for t in transcript_list.find_generated_transcript(['en']).fetch():
        text = t['text']
        file.write(text + ' ')

    # reference for transcript
    # youtube_transcript_api: https://pypi.org/project/youtube-transcript-api/ 
    # the source code: https://github.com/jdepoix/youtube-transcript-api/blob/master/setup.py

if __name__ == "__main__":
    main()