import os

if __name__=='__main__':
    print("welcome to robokspeaker 1.1 created by kartik")
    while True:
    
        x=input("Enter what you want me to speak: ")
        if x=="k":
            os.system("say 'by by budddy'")
            break
        command = f" say {x} "
        os.system(command)