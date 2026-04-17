


from google import genai
from dotenv import load_dotenv
import os,io
from gtts import gTTS


#loading environment variable
load_dotenv()

my_api_key= os.getenv("GEMINI_API_KEY")

client= genai.Client(api_key=my_api_key)

#note generator:

def bangla_note_generator(images):

     prompt="""Summarize the picture in note format in language Bangla at max 100 words
     make sure to add necessary markdown to differentiate different section"""

     response= client.models.generate_content(
         model= "gemini-2.5-flash",
         contents=[images,prompt]
     )

     return response.text


def note_generator(images):

    prompt="""Summarize the picture in note format at max 100 words
    make sure to add necessary markdown to differentiate different section"""

    response= client.models.generate_content(
        model= "gemini-2.5-flash",
        contents=[images,prompt]
    )

    return response.text




def english_audio_generator(text):

    speech= gTTS(text,lang='en',slow=False)
    audio_buffer= io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer


def quiz_generator(image,difficulty):

    prompt=f"generate 3 quizzes based on the {difficulty}.make sure to add down markdown to differentiate the options. Add correct answer too apter the quiz"

    response= client.models.generate_content(
        model= "gemini-2.5-flash",
        contents=[image,prompt]
    )

    return response.text





# def bangla_audio_generator(text):
#      speech = gTTS(text=text, lang='bn', slow=False)
#      audio_buffer = io.BytesIO()
#      speech.write_to_fp(audio_buffer)
#      audio_buffer.seek(0)
#      return audio_buffer
