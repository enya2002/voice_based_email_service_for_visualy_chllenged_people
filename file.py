import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_mail(receiver,subject, message):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('testingemail967@gmail.com','qwertyistyping')
    email= EmailMessage()
    email['From'] = 'testingemail967@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)




email_list = {
     'ayush': 'ayujudo22@gmail.com',
     'adamay': 'adamaysingh18@gmail.com',
     'dishant': 'dishantnbd@gmail.com'
     }

def get_email_info():
    talk('To Whom you want to send email?')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    print('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email?')
    message = get_info()
    send_mail(receiver, subject, message)
    talk('Your email is sent.')
    print('Your email is sent')



get_email_info()
