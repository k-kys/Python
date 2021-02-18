from gtts import gTTS
# import os
from playsound import playsound

# Thư viện gtts (Google Text To Speed có sẵn tiếng Việt, nhưng sẽ tạo ra 1 file
# mp3 xong rồi mới đọc. Pyttsx3 thì không tạo file mp3 mà đọc luôn)
tts = gTTS('Xin chào các bạn. Tôi tên là FRIDAY', tld='com.vn', lang='vi')


tts.save("hello.mp3")
playsound("hello.mp3")
