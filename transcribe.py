#!/usr/bin/env python
#coding: utf-8

import argparse
import io
import codecs
import emoji
from termcolor import colored
from google.cloud import speech
from google.cloud.speech import types, enums

def transcribe(args):
    client = speech.SpeechClient()

    # Extract filename
    filename = args.path.split('/')[-1]

    # Configuration
    print '[*] Reading',
    print colored(filename, 'cyan'), 
    if args.path.startswith('gs://'):
        print 'from Google Cloud Storage.'
        audio = types.RecognitionAudio(uri=args.path)
    else:
        print 'from local strage.'
        with io.open(args.path, 'rb') as audio_file:
            content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        language_code=args.lang)

    # Asynchronous recognition
    print emoji.emojize('[*] Transcribing ... this takes a while. Have a :coffee: break. ;)', use_aliases=True)
    operation = client.long_running_recognize(config, audio)
    response = operation.result()

    # Save into file
    print '[*] Saving ...',
    f = codecs.open('.'.join(filename.split('.')[0:-1]) + '.txt', 'a', 'utf-8')
    for result in response.results:
        for alternative in result.alternatives:
            f.write(u'{}\n'.format(alternative.transcript))
    f.close()
    print 'Done.'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='path_to_audio')
    parser.add_argument('--lang', default='ja-JP', help='language_code')
    args = parser.parse_args()
    transcribe(args)

if __name__ == '__main__':
    main()
 
