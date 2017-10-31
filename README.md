# transcribe
A script to transcribe audio files with Google Cloud Speech API.

## Requirements
* Python 2.x.x
* ffmpeg

## Quick Start
1. [Set up new Google Cloud Platform project](https://console.cloud.google.com/).
2. [Enable Google Cloud Speech API](https://console.developers.google.com/apis/api/speech.googleapis.com/overview).
3. [Set up a service account](https://cloud.google.com/speech/docs/common/auth#set_up_a_service_account).
4. Save `credential.json`.
5.  Run commands below:

```sh
export GOOGLE_APPLICATION_CREDENTIALS=credential.json
git clone https://github.com/ntddk/transcribe
cd transcribe
pip install -r requirements.txt
python transcribe.py audio.flac
```

## Note
* Audio file must be encoded to FLAC format.

```sh
ffmpeg -i audio.mp3 audio.flac
```

* You can also transcibe audio file on `bucket` of [Google Cloud Storage](https://cloud.google.com/storage/docs/quickstart-console).

```sh
python transcribe.py gs://bucket/audio.flac
```

* We highly recommend the use of Google Cloud Shell.

## Reference
* [GoogleCloudPlatform/python-docs-samples](https://github.com/GoogleCloudPlatform/python-docs-samples)

