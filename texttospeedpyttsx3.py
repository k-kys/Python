import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")

# láy thông tin giọng đọc trong windows
# for voice in voices:
#     print("Voice:")
#     print("- ID: %s" % voice.id)
#     print("- Name: %s" % voice.name)
#     print("- Languages: %s" % voice.languages)
#     print("- Gender: %s" % voice.gender)
#     print("- Age: %s" % voice.age)

vi_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An";

engine.setProperty("voice", voices[2].id)
engine.setProperty("voice", vi_voice_id)
engine.say("Xin chào các bạn. Tôi tên là Ngô Văn Bắp")
engine.runAndWait()
