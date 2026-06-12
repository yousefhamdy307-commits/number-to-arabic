from num2words import num2words
import arabic_reshaper
from bidi.algorithm import get_display
def number_Arabic() :
    print("converting numbers to words")
    while True :
        user = input("type your namber ")
        
        if user.lower() == 'exit' :
            print(" Good Zoksh")
            break 

        try :
            number = int(user)
            result = num2words(number,lang='ar')

            reshaped_text = arabic_reshaper.reshape(result)
            bidi_text = get_display(reshaped_text)

            print(f" result :{bidi_text}")

        except ValueError :
            print("please enter a valid number")


number_Arabic()