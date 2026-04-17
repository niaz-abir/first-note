import streamlit as st
from api_calling import note_generator,english_audio_generator,bangla_note_generator,quiz_generator
from PIL import Image


st.title("More summary and quiz generator")
st.markdown("Upload upto 3 images to generate note summary and quizzes")
st.divider()

with st.sidebar:
    st.header("controls")

    #images work
    images = st.file_uploader("upload your image",type=["jpg","jpeg","png"],accept_multiple_files=True)
    
    pil_images=[]

    for img in images:
        pil_img= Image.open(img)
        pil_images.append(pil_img)

  
    if images:
        if len(images)>3:
            st.error("upload three image")
        else:
            col = st.columns(len(images))
            st.subheader("uploaded images")

            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)

    #category

    selected_option= st.selectbox("Enter the difficulty of your quiz",("Easy","Medium","Hard"),index=None)


    pressed=st.button("click the button to initiate AI",type="primary")

    #sidebar finished

if pressed:
    if not images:
        st.error("upload your image")

    if not selected_option:
        st.error("please select your option")

    if images and selected_option:
      
         #note for bangla

         with st.container(border=True):
           st.subheader("Your note in bangla")

         with st.spinner("Note is writing for you"):
             generated_notes= bangla_note_generator(pil_images)
             st.markdown(generated_notes)

               #note for english:
         with st.container(border=True):
          st.subheader("Your note in english")

         with st.spinner("Note is writing for you"):
            generated_notes= note_generator(pil_images)
            st.markdown(generated_notes)
        
          
        
      

        #audio in english

    with  st.container(border=True):

        st.subheader("Audio note in english")

        with st.spinner("Note is generating for you"):
           generated_notes= generated_notes.replace("#","")
           generated_notes= generated_notes.replace("*","")
           generated_notes= generated_notes.replace("-","")
           generated_notes= generated_notes.replace("`","")
           eng_audio_Transcript= english_audio_generator(generated_notes)
           st.audio(eng_audio_Transcript)
      
      # ✅ Audio (Bangla)

        # with st.container(border=True):
        #  st.subheader("Audio note in bangla")

        # with st.spinner("Generating audio..."):
        #  generated_notes= generated_notes.replace("#","")
        #  generated_notes= generated_notes.replace("*","")
        #  generated_notes= generated_notes.replace("-","")
        #  generated_notes= generated_notes.replace("`","")
          
        #  bn_audio_transcript = bangla_audio_generator(generated_notes)
        #  st.audio(bn_audio_transcript)

        

        #quiz
    with  st.container(border=True):
        st.subheader(f"your quiz level {selected_option} Difficulty")

        with st.spinner("Quiz is writing for you"):
            quizzes= quiz_generator(pil_images,selected_option)
            st.markdown(quizzes)

        

