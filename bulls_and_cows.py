# Secret code / Game conditions
import random
digit_length = 4
guess_length = 6

# Banner for game
print(''' 
                                                                                                                                                        
                                                                                                                                                        
    ,---,.                 ,--,    ,--,                                                                    ,----..                                      
  ,'  .'  \              ,--.'|  ,--.'|                                                     ,---,         /   /   \                                     
,---.' .' |         ,--, |  | :  |  | :                                         ,---,     ,---.'|        |   :     :  ,---.           .---.             
|   |  |: |       ,'_ /| :  : '  :  : '    .--.--.                          ,-+-. /  |    |   | :        .   |  ;. / '   ,'\         /. ./|  .--.--.    
:   :  :  /  .--. |  | : |  ' |  |  ' |   /  /    '             ,--.--.    ,--.'|'   |    |   | |        .   ; /--` /   /   |     .-'-. ' | /  /    '   
:   |    ; ,'_ /| :  . | '  | |  '  | |  |  :  /`./            /       \  |   |  ,"' |  ,--.__| |        ;   | ;   .   ; ,. :    /___/ \: ||  :  /`./   
|   :     \|  ' | |  . . |  | :  |  | :  |  :  ;_             .--.  .-. | |   | /  | | /   ,'   |        |   : |   '   | |: : .-'.. '   ' .|  :  ;_     
|   |   . ||  | ' |  | | '  : |__'  : |__ \  \    `.           \__\/: . . |   | |  | |.   '  /  |        .   | '___'   | .; :/___/ \:     ' \  \    `.  
'   :  '; |:  | : ;  ; | |  | '.'|  | '.'| `----.   \          ," .--.; | |   | |  |/ '   ; |:  |        '   ; : .'|   :    |.   \  ' .\     `----.   \ 
|   |  | ; '  :  `--'   \;  :    ;  :    ;/  /`--'  /         /  /  ,.  | |   | |--'  |   | '/  '        '   | '/  :\   \  /  \   \   ' \ | /  /`--'  / 
|   :   /  :  ,      .-./|  ,   /|  ,   /'--'.     /         ;  :   .'   \|   |/      |   :    :|        |   :    /  `----'    \   \  |--" '--'.     /  
|   | ,'    `--`----'     ---`-'  ---`-'   `--'---'          |  ,     .-./'---'        \   \  /           \   \ .'              \   \ |      `--'---'   
`----'                                                        `--`---'                  `----'             `---`                 '---"                  
                                                                                                                                                     
''')

def get_secret(digit_length):
    return random.sample(range(1, 10), digit_length)
def pretty(number_list):
    return "".join([str(digit) for digit in number_list])
secret = get_secret(digit_length)
example = pretty(get_secret(digit_length))
print(secret)

try:
    guess_number = 1
    while True:

        guess = input(f"What is guess no. {guess_number}?\n")
        try:
            guess_list = [int(char_digit) for char_digit in list(guess)]
        except ValueError:
            print(f"You need to provide a number, e.g. {example}.")
            continue
        if len(guess_list) != digit_length:
            print(f"You need to provide a {digit_length} digit guess, e.g. {example}.")
            continue
        bull_count = 0
        cow_count = 0
        for i in range(digit_length):
            secret_digit = secret[i]
            guess_digit = guess_list[i]
            if secret_digit == guess_digit:
                bull_count += 1
                continue
            if guess_digit in secret:
                cow_count += 1
                continue
        if bull_count == digit_length:
            print("You have won the game!")
            break
        else:
            print(f"Bulls: {bull_count} | Cows: {cow_count}")
        if guess_number == guess_length:
            print(f"You reached the maximum guesses of {guess_length}\nThe answer was {pretty(secret)}")
            break
        guess_number += 1


except KeyboardInterrupt: 
    print("Bye")






