from termcolor import colored
import sys
import time
import os

# Enable ANSI on some Windows terminals
if os.name == 'nt':
    os.system('')

def shake_text(text, shakes=8, delay=0.04, color=None):
    """
    Shake `text` in-place a few times then leave the text in its final position
    (does not print a newline).
    """
    if color:
        try:
            text_to_draw = colored(text, color)
        except Exception:
            text_to_draw = text
    else:
        text_to_draw = text

    for i in range(shakes):
        offset = " " * (i % 2)  # alternate 0/1 spaces
        sys.stdout.write("\r" + offset + text_to_draw)
        sys.stdout.flush()
        time.sleep(delay)

    # finally draw normal (no offset)
    sys.stdout.write("\r" + text_to_draw)
    sys.stdout.flush()
    # do NOT add newline here (typewriter will continue on same line if needed)


def input_clear(prompt=""):
    """
    Reads user input with input(prompt) then erases the whole prompt+response line
    from the terminal and returns the string entered.
    """
    val = input(prompt)
    # Move cursor up one line and clear it
    sys.stdout.write("\033[A\033[K")
    sys.stdout.flush()
    return val


# Changes up speed of text
def typewriter(text, default_delay=0.05):
    delay = default_delay
    color = None
    i = 0

    while i < len(text):

        if text[i] == "{":
            end = text.find("}", i)
            if end == -1:
                # malformed tag — print the rest and break
                sys.stdout.write(text[i:])
                break
            tag = text[i+1:end]

            # speed tags
            if tag == "fast":
                delay = 0.01
            elif tag == "slow":
                delay = 0.08
            elif tag == "superslow":
                delay = 0.15
            elif tag == "endspeed":
                delay = default_delay

            # color tags
            elif tag.startswith("color:"):
                color = tag.split(":", 1)[1].strip()
            elif tag == "endcolor":
                color = None

            # combined end (for e.g. {shake}...{end}) - note: {end} resets speed/color
            elif tag == "end":
                delay = default_delay
                color = None

            # custom shake: {shake}TEXT{end}
            elif tag == "shake":
                # find the closing {end}
                end_marker = text.find("{end}", end + 1)
                if end_marker == -1:
                    # nothing to shake; skip tag
                    i = end + 1
                    continue
                content = text[end + 1:end_marker]
                shake_text(content, color=color)
                # advance i past the "{end}"
                i = end_marker + len("{end}")
                continue

            # advance past tag
            i = end + 1
            continue

        # normal character printing
        ch = text[i]
        if color:
            sys.stdout.write(colored(ch, color))
        else:
            sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
        i += 1

    print()  # default newline at end of the whole typewriter call


# --- Act 1 - Breakout ---
typewriter("\nThis is a decision-based simulation. Your actions {color: red}WILL{endcolor} have consequences.")
print(colored("-------------------------------------------------------------", "yellow"))

# Start input (cleared after)
begin = input_clear("Type " + colored("START ", "green") + "to begin your Journey of Revenge: ")
begin = begin.upper().strip()

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

input_clear("\nENTER to continue...")
# Dialogue
typewriter("\n{superslow}{color: red}GUARD 1:{endspeed}{endcolor}{slow} Did you not hear me scumbag? I said lights out. Get in your bed you swine.{endspeed}")

input_clear("\nENTER to continue...")
typewriter('\n{superslow}{color: red}GUARD 2:{endspeed}{endcolor}{slow} Hmph, maybe shes deaf. Anything in that thick skull of yours anyways{color: yellow} prisoner 041?{endcolor}{endspeed}')

input_clear("\nENTER to continue...")
typewriter("\n{superslow}{color: cyan}Unbelieveable.{endspeed}{slow} Is this the price I have to pay for a crime I didn't even commit? {endspeed}{color: magenta} Zahra thought to herself{endcolor}")

input_clear("\nENTER to continue...")
# Narrate
typewriter("\n{color: magenta}By the time she's finished questioning her sanity, the guards have already entered her cell, sneering, waving their batons around, as if threatening a disobedient dog with a roll of newspaper")

input_clear("\nENTER to continue...")
# Dialogue
typewriter("\n{color: red}{superslow}Guard 1:{endcolor}{endspeed}{slow} Look mutt, I won't tell you again.{endspeed}{superslow} Get. In. Your. Bed.{endspeed}")

typewriter("\n{color: cyan}Alright. Sitting here and playing hard to get probably wont get me anywhere. Guess I should do something...")

input_clear("\nENTER to continue...")


# Choice time
typewriter("\n{color: yellow}{slow}What will Zahra do?{endcolor}{endspeed}")
typewriter("\n{color: green} 1.{endcolor}{color: blue} Obey and get in her bed{endcolor}")
typewriter("\n{color: green} 2.{endcolor}{color: blue} Take her chances, try to take them both on{endcolor}")

choice = input_clear("\nChoose 1, or 2: ").strip()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Choice 1:
if choice == "1":
    typewriter("\n{color: magenta}Zahra swallows her already broken pride, and climbs into bed...{endcolor}")

    input_clear("\nENTER to continue...")
    typewriter("\n{color: red}{superslow}Guard 1:{endcolor}{endspeed}{superslow} Good little dog.{endspeed}{slow} Act up again, and we won't give you a second chance..{endspeed}")
    
    input_clear("\nENTER to continue...")

    typewriter("\n{color: magenta}{slow}The guards exit the cell as the spoken threat looms in the air like a still fog.{endcolor}{endspeed}")


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Choice 2:
if choice == "2":
    typewriter("\n{color: cyan}You leap at the guards with a weak attempt, placing all your bets on a minisucle chance...{endcolor}")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------



