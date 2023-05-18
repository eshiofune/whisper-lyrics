# whisper-lyrics
This tool automatically gets lyrics of songs from audio files using the OpenAI Whisper model or API.

## Setup
1. Switch to either the `model` or `api` folder:
    ```
    cd model
    ```

1. Copy the config file:
    ```
    cp config_dist.py config.py
    ```
    Make sure to modify the config values as appropriate.

1. Create a virtual environment using [venv](https://docs.python.org/3/library/venv.html) for example:
    ```
    python -m venv .env
    ```

1. Install requirements:
    ```
    source .env/bin/activate
    pip install -r requirements.txt
    ```

## Running
Change the file path 
Run:
```
python transcribe.py
```

## Help with issues
- If you get the error:
    ```
    urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1002)
    ```
    See: https://stackoverflow.com/questions/52805115/certificate-verify-failed-unable-to-get-local-issuer-certificate
- If you get the error:
    ```
    RuntimeError: Model has been downloaded but the SHA256 checksum does not not match. Please retry loading the model.
    ```
    See: https://github.com/openai/whisper/discussions/1027

## Contributing
Please fork this repo and make a pull request to either the `transcribe` or `test` branch.
