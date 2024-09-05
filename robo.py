import os

if __name__ =='__main__':
    print("welcome to robospeaker")
    print("it is devloped by kushagra")
    while True:
        x=input("Enter what you wanted to speak:")
        if x=="q":
            os.system("bye bye to all")
            break
    command=f"say {x}"
    os.system(command)
