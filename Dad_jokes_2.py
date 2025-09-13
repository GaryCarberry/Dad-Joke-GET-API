import requests
import random
import colorama
import termcolor
import pyfiglet
colorama.init()
 
result= pyfiglet.figlet_format('Dad Jokes Software',font = "slant")
result=termcolor.colored(result,color='magenta')
print(result)
answer=input("Gimme a topic for a joke")

if answer:
    url = "https://icanhazdadjoke.com/search"
    response = requests.get(
        url,
        headers= {"Accept":"application/json"},
        params={"term":answer}
    )
    data=response.json() # gives dictionary
    amount=len(data["results"])

    print(f"I have {amount} jokes about that topic heres one") 
    joke=random.choice(data["results"])
    print(joke["joke"])
    #print(data["joke"])
else:
    print("You didnt type nuffin")
