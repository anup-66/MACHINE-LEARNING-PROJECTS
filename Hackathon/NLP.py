# import speech_recognition as sr
#
# # Initialize recognizer class (for recognizing the speech) and store in the object called speech
# # speech = sr.Recognizer()
#
# # Reading Audio file as source
# # listening the audio file and store in text variable
# # Give your file name with path
# rec = sr.Recognizer()
# data = sr.Microphone()
# with data as source:
#     rec.adjust_for_ambient_noise(source, duration=1)
#     print("Listening....")
#     rec.pause_threshold = 0.5
#     audio_voice = rec.listen(source)
# try:
#     print("Analysing....")
#     Speech = rec.recognize_google(audio_voice, language="te-IN")
#     print(Speech)
# except:
#     print('Sorry')
#
# # with sr.AudioFile('Telugu.wav') as source:
# #     text = sr.listen(source)
# #
# #     # recoginize_() method will throw a request error if the API is unreachable or unable to
# #     # recogonize or match the words, hence using exception handling
# #     try:
# #
# #         # using google speech recognition
# #         text_output = speech.recognize_google(text,
# #                                               language="ml-IN")  # By default, it converts the speech into english
# #         print('Converting speech into text ...')
# #         print(text_output)
# #         # Adding french langauge option



from transformers import MBartForConditionalGeneration, MBart50TokenizerFast


model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt")

tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt", src_lang="en_XX")


article_en ="how are you."

model_inputs = tokenizer(article_en, return_tensors="pt")



generated_tokens = model.generate(
    **model_inputs,
    forced_bos_token_id=tokenizer.lang_code_to_id["hi_IN"]
)

translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

print(translation)



