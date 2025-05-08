# interpreter
An attempt to implement a local interpreter.

That version uses Mac OS's 

## How to run
python3 -m venv venv
source venv/bin/activate
(.venv) pip install git+https://github.com/openai/whisper.git (the Whisper model will be downloaded!)
pip install transformers
pip install sentencepiece
(optional) pip install sacremoses

### Next
To have it working with RAM, one can proceed as follows:
pip install sounddevice numpy openai-whisper