
# windows command line console input
#>set GOOGLE_APPLICATION_CREDENTIALS=c:\Documents\chrome-empire-250103-52d834a45056.json
#>set http_proxy=http://127.0.0.1:10809
#>set https_proxy=http://127.0.0.1:10809
# Imports the Google Cloud client library
#from google.cloud import speech
from google.cloud import speech_v1p1beta1 as speech

import os
def transcribe_file_with_multilanguage(files_path = r'D:/dirname'):
    client = speech.SpeechClient()

    first_lang = "fr-FR"
    #second_lang = "cmn-Hans-CN"
        
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        #language_code='fr-FR',
        model='command_and_search',
        enable_automatic_punctuation=True,
        sample_rate_hertz=16000,
        #audio_channel_count=2,
        #enable_speaker_diarization=True,
        language_code=first_lang,
        #alternative_language_codes=[second_lang],
        #model="video",
    )

    for f in os.listdir(files_path):
        speech_file = os.path.join(files_path, f)
        outputfile = os.path.splitext(f)[0] + '.txt'
        outputfile = os.path.join(files_path, outputfile)
        if os.path.splitext(speech_file)[-1] != '.mp3':
            continue
        
        if os.path.exists(outputfile):
            print(speech_file + ' already transcribed in ' + outputfile)
            continue

        print(speech_file)
        with open(speech_file, "rb") as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        #gcs_uri = "gs://pathname.mp3"
        #audio = speech.RecognitionAudio(uri=gcs_uri)

        
        #operation = client.long_running_recognize(config=config, audio=audio)
        operation = client.recognize(config=config, audio=audio)
        print("Waiting for operation to complete...")
        #response = operation.result(timeout=30)
        response = operation
        #print(response.results)
        
        print('saving to ' + outputfile)
        with open(outputfile, 'w', encoding='utf-8') as f:
            for i, result in enumerate(response.results):
                alternative = result.alternatives[0]
                
                print("-" * 20)
                print(u"First alternative of result {}: {}".format(i, alternative))
                print(u"Transcript: {}".format(alternative.transcript))
                f.write(alternative.transcript)
                f.write('\n')
        #break
transcribe_file_with_multilanguage()
