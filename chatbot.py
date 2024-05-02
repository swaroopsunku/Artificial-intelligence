pairs = [
    [ "My name is (.*)",   ["Hello %1, How are you today ?"]  ],
    [ "(.*) help",  ["Yes, I can help you",]  ],
    [ "(.*) your name ?",   ["My name is Robo. I'm a chatbot.",]  ],
    [ "how are you (.*) ?", ["i am great!"]  ],
    [ "sorry (.*)",   ["Its OK, never mind that",]  ],
    [ "(hi|hey|hello|hola|holla)(.*)",  ["Hello", "Hey there","Hi" ] ],
    [ "(.*) not feeling (.*)", ["Ok. Tell me your problem",] ],
    [ "(.*)created(.*)", ["Mmvc created me using Python's NLTK library ","top secret ;)",] ],
    [ "(.*)cough(.*)",   ["Take Ginger tea and take cough syrup",] ],
    [ "(.*)(headache|fever)(.*)", ["please take paracetamol tablet after food",] ],
    [ "(.*)stomach(.*)", ["please take lightweight food",] ],
    [ "i am (good|ok)",  ["Ok good. Happy to hear from you",]  ],
    [ "quit", ["Bye for now. See you soon. It was nice talking to you.. :)"] ], 
]

from nltk.chat.util import Chat, reflections
print("Hi, I am Robo and I am a chatbot \nPlease type lowercase English language to start a conversation. \n Type quit to leave ")
#Create Chat Bot
chat = Chat(pairs, reflections)
#Start conversation
chat.converse()
