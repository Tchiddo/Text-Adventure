from termcolor import colored
import sys
import time

# Changes up speed of text
def typewriter(text, default_delay=0.05):
    delay = default_delay
    color = None
    i = 0

    while i < len(text):
        
        if text[i] == "{":
            end = text.find("}", i)
            tag = text[i+1:end]

            if tag == "fast":
                delay = 0.01
            elif tag == "slow":
                delay = 0.1
            elif tag == "superslow":
                delay = 0.15
            elif tag.startswith("color:"):
                color = tag.split(":")[1].strip()
            elif tag == "end":
                delay = default_delay
                color = None

            elif tag == "endcolor":
                color = None  # Only reset color
            
            elif tag == "endspeed" :
                delay = default_delay


            i = end + 1
            continue

        
        if color:
            sys.stdout.write(colored(text[i], color))
        else:
            sys.stdout.write(text[i])
        sys.stdout.flush()
        time.sleep(delay)
        i += 1

        
    print()  

# --- Act 1 - Breakout ---
typewriter("\nThis is a decision-based simulation. Your actions {color: red}WILL{endcolor} have consequences.")
print(colored("-------------------------------------------------------------", "yellow"))

# Start input
begin = input("Type " + colored("START ", "green") + "to begin your Journey of Revenge: ").upper().strip()

if begin != "START":
    print("Conditions not met, TERMINATING SIMULATION")
    print("-------------------------------------------------------------------")
    sys.exit()

print("-----------------------------------------------------------------------")
print("                Act 1   BREAKOUT                            ")

# Location info
typewriter("\n{superslow}{color: blue}Location:{endcolor} {slow} Chronoview Prison {endspeed}")
typewriter("{superslow}{color: blue}Time:{endspeed}{endcolor} {slow} 10:42 PM")
typewriter("{superslow}{color: blue}Weather condition:{endspeed}{endcolor} {slow} HARSH RAIN and THUNDERSTORMS {endspeed}")
typewriter("{superslow}{color: blue}Health condition:{endspeed}{endcolor} {slow} POOR {endspeed}")

# Dialogue
typewriter("\n{superslow}{color: red}GUARD 1:{endspeed}{endcolor}{slow} Did you not hear me scumbag? I said lights out. Get in your bed you swine.{endspeed}")

typewriter('\n{superslow}{color: red}GUARD 2:{endspeed}{endcolor}{slow} Hmph, maybe shes deaf. Anything in that thick skull of yours anyways{color: yellow} prisoner 041?{endcolor}{endspeed}')

typewriter ("\n{superslow}{color: cyan}Unbelieveable.{endspeed}{slow} Is this the price I have to pay for a crime I didn't even commit? {endspeed}{color: magenta} Zahra thought to herself{endcolor}")

input ("\nENTER to continue: ")


