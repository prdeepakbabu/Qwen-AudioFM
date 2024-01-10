#import packages
import utils
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig
import torch
torch.manual_seed(1234)

#import model and tok
tokenizer = AutoTokenizer.from_pretrained("audio_models/Qwen-Audio-Chat", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("audio_models/Qwen-Audio-Chat", trust_remote_code=True).eval()

#define the input audio file and text prompt
query = tokenizer.from_list_format([
    {'audio': 'data/happy_speech.wav'}, # Either a local path or an url
    {'text': 'can you describe the scene ?'},
])
global history

#initiate first turn
response, history = model.chat(tokenizer, query=query, history=None)
print(response)

#continue the dialog (2+ turns). type "end" to end the dialog.
dialog()


