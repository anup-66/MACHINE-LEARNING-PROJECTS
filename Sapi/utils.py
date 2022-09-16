greet_n = (
    "i am assuming that u are going to bed good night sir",
    "It was nice spending time with you sir ba bye good night",
    "You look tired nice decision to take some rest go get it i am here whenever you want me good night ! ")

greet_m = ("It's morning now sir wishing u a great day ahead",
           "hey sir u worked late night are u ok pls take some rest")
Normal_greet=("Thankyou for talking to me bye take care. Talk to you later")
# start_conv = (
#     "Cool, I'm on it sir.",
#     "Okay sir, I'm working on it.",
#     "Just a second sir.", "just wait a second", "please give me some time to do, I am working on it"
#              )
start_conv =("Fine sir nenu a pani medhe unna","Cool, I'm on it sir.")
hello = ("hello sir how are you ?", "hey sir hope you are  doing well",
         "hello sir i am here to help you ")
name = ("what is my name ", "my name", "can u remember my name", "my name is ")
Help = ("help", "what can u do for me ", "can do", "what you do", "you job", "job")
Last_words = ("stop", "bye", "tata", "good bye", "exit", "Time to go ", "i have to go now", "i will take a leave now ",
              "leave","bye bye","Talk to you later")

a = []
def rem_name(name):
    a.append(name)


help = """######### THE List of work i can do is ###############\n1. i can talk to you for all day\n 2. I can track your I.P address\n 
3.i can open camera,notepad\n4. i can search for u on google\n5. i can search contents on wikipedia\n
5. i can send whats app msg to any one in your contact list\n6.i can play video on youtube\n
7. i can say jokes and even give you some advice
8. i can send email too😘😘😘😘"""


def say_name():
    return a[0]


def what_do():
    print(help)
