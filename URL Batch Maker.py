print(""" ______                   _        _     _ ______  _          _______       _                 
(____  \         _       | |      (_)   (_|_____ \(_)        (_______)     | |                
 ____)  )_____ _| |_ ____| |__     _     _ _____) )_          _  _  _ _____| |  _ _____  ____ 
|  __  ((____ (_   _) ___)  _ \   | |   | |  __  /| |        | ||_|| (____ | |_/ ) ___ |/ ___)
| |__)  ) ___ | | |( (___| | | |  | |___| | |  \ \| |_____   | |   | / ___ |  _ (| ____| |    
|______/\_____|  \__)____)_| |_|   \_____/|_|   |_|_______)  |_|   |_\_____|_| \_)_____)_|    
                                                                                              
 ______           _______ _             _     ___   ___   ___   ______                        
(____  \         (_______|_)           | |   (___) (___) (___) (_____ \                       
 ____)  )_   _    _  _  _ _ ____   ____| |__    _     _     _    ____) )                      
|  __  (| | | |  | ||_|| | |  _ \ / _  |  _ \  | |   | |   | |  / ____/                       
| |__)  ) |_| |  | |   | | | | | ( (_| | | | |_| |_ _| |_ _| |_| (_____                       
|______/ \__  |  |_|   |_|_|_| |_|\___ |_| |_(_____|_____|_____)_______)                      
        (____/                   (_____|                                                    """)

print("""ReadME : 
> It's possible to add a group of sequential file names 
> like img001.jpg, img002.jpg, img002.jpg, etc., img100.jpg
> to Batch Maker queue. 
> Use the asterisk(*) wildcard for the file name pattern. 
> For example:
> https://www.anydownload.com/pictures/*.jpg
> Here :
> Wildcard size = 1 >> 1, 2, 3, 4, 5, ....99, 100
> Wildcard size = 2 >> 01, 02, 03, 04,....99, 100
> Wildcard size = 3 >> 001, 002, 003, 004...010, 011...099, 100\n""")
print("Replace number with asterisk(*)")
print(r"https://www.any.com/picture/001.jpg >>> https://www.any.com/picture/*.jpg"+"\n" )

site = input("Paste your link here After changed:")
num = int(input("Series Start From : "))
num2 = int(input("To :"))
wildcard = int(input("WildCard Size : "))

with open("URL.txt","+w") as file:
    for i in range(num,num2+1):
        point = site.split("*")
        file.write(f"{point[0]}{i:0{wildcard}}{point[1]}\n")

print("Task Finished. URLs Saved in URL.txt")
