import pyttsx3

def get_voices(engine):
    #Get available voices on the system.
    voices = engine.getProperty('voices')
    return voices

def set_voice(engine, voice_id):
    #Set the voice based on the given voice ID.
    engine.setProperty('voice', voice_id)

def text_to_speech(text, voice_id=None):
    #Convert text to speech with an optional specified voice.
    ##Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    #Get available voices
    voices = get_voices(engine)

    if voice_id is not None:
        #Set the voice to the one selected by the user
        set_voice(engine, voices[voice_id].id)
    else:
        """Set to the default voice"""
        set_voice(engine, voices[0].id)

    #Speak the provided text
    engine.say(text)
    engine.runAndWait()

def list_available_voices():
    #List the available voices.
    engine = pyttsx3.init()
    voices = get_voices(engine)
    print("Available Voices:")
    for idx, voice in enumerate(voices):
        print(f"{idx}: {voice.name}")

#Defining the conversation
s=input('enter a conversation')
l=s.split(':')
conversation=[]
for i in range(0,len(l),2):
    #splitting the conversation into sentences and assigning the
    #key as character name and value as sentence
    d={}
    d['text']=l[i+1]
    d['char']=l[i].strip().lower()
    conversation.append(d)
    
list_available_voices()

Voice_list={}
for i in range(3):
    a=input(f"enter the name of character for voice_id {i}").lower()
    Voice_list[a]=i
for line in conversation:
    char_name=line['char']
    selected_voice_id=Voice_list[char_name]
    text_to_speech(line['text'],selected_voice_id)
        

   
