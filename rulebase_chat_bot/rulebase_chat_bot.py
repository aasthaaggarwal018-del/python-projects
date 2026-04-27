# extract time in hours

import datetime
import time

presenthour= datetime.datetime.now().hour
# greeting according to time
if 5 <=presenthour <=11:
    print('good morning')
elif 11 <=presenthour <=17:
    print('good afternoon')
elif 17 <=presenthour <=20:
    print('good evening')
else:
    print('good night')

# welcome
print('welcome to our chat bot \nyou can ask simple questions. ' \
'\npress exit to leave chat')

# dictonary
response={
    'hello':'hi i am you personal chat bot how can i help you',
    'how are you': 'i am fine .thanks',
    'who are you': 'i am a rule base chat bot you can ask me ',
    'motivate me':'i know you can do it ',
    'happy':'thats great ',
    'sad':'ohh sorry to hear that you should relax and perform meditation',
    'bye': 'take care we will meet again'

}
# function to extract the answer
def x(i):
    i=i.lower()
    for j in response:
        if j  in i:
            return response[j]
        
    return 'i cannot answer the question i am still developing'

#running chat in loop
while True:
    i=input('entre your question here:')
    print (x(i))

    if 'bye' in i.lower() :
        break
    