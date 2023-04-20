#G-Brain by Richard Vaalotu
#Code by Richard Vaalotu
#Copyright (c) 2023 Richard Vaalotu

import openai
import tkinter as tk
import time
import pyttsx3
import threading

# Initialize the OpenAI API client
openai.api_key = "YOUR API KEY"

# Set up the tkinter window and widgets
root = tk.Tk()

# Set the window icon
root.iconbitmap("test.ico")

# Set the window title
root.title("G-Brain By Richard Vaalotu")

root.geometry("800x500")
root.configure(bg="black")

# Center the text in the code input box
code_label = tk.Label(root, text="Ask me anything here:", bg="black", fg="white")
code_label.pack()

code_box = tk.Text(root, height=15, bg="black", fg="white", insertbackground="white")
code_box.pack(fill="both", expand=True)
code_box.tag_configure("center", justify="center")
code_box.insert("end", "Enter here...", "center")

def generate_response():
    # Get the user's code input
    code = code_box.get("1.0", tk.END)

    # Generate a response from ChatGPT
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=code,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Get the relevant answer from the response
    answer = response.choices[0].text

    # Display the answer in the response box with a typing effect
    response_box.delete("1.0", tk.END)

    # Define a function that speaks the answer using TTS
    def speak_answer():
        engine = pyttsx3.init()
        engine.say(answer)
        engine.runAndWait()

    # Run the TTS engine in a separate thread
    threading.Thread(target=speak_answer).start()

    # Add the answer to the response box one character at a time
    for char in answer:
        response_box.insert(tk.END, char)
        root.update()
        time.sleep(0.045)
        response_box.see(tk.END)

response_button = tk.Button(root, text="Answer me", command=generate_response, bg="white", fg="black")
response_button.pack()

# Center the text in the ChatGPT response box and add a placeholder
response_label = tk.Label(root, text="G-Brain Response:", bg="black", fg="white")
response_label.pack()

response_box = tk.Text(root, height=15, bg="black", fg="green", insertbackground="white")
response_box.pack(fill="both", expand=True)
response_box.tag_configure("center", justify="center")
response_box.insert("end", "G-Brain will respond here...", "center")

# Add a button to clear the GPT response box
def clear_response():
    response_box.delete("1.0", tk.END)

clear_button = tk.Button(root, text="Clear Response", command=clear_response, bg="white", fg="black")
clear_button.pack()

# Set the foreground color of the ChatGPT response text to green
response_box.config(fg="green")

root.mainloop()
