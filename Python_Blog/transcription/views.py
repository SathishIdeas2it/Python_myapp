from django.shortcuts import render
from django.http import HttpResponse
import logging
import openai
import config_reader.config as config

# Create your views here.

def audio_to_text(request):
    try:
        
        api_key = config.read_config('Audio_Convertion_API','audio_to_text_API_Key')        
        model_type =config.read_config('Audio_Convertion_API','model_type')        
        output_format =config.read_config('Audio_Convertion_API','output_format') 
        output_language = config.read_config('Audio_Convertion_API','output_langanguage')
        
        audio_file= open("audio/song.mp3", "rb")        
        transcript = openai.Audio.transcribe(api_key=api_key,model=model_type,file= audio_file,response_format=output_format,language=output_language)
        return HttpResponse(transcript)
    
    except Exception as e:
        error_message = 'user:' + str(request.user) + ', error:'+ str(e)     
        logging.getLogger("error_logger").error(error_message)