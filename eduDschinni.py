import tkinter as tk
import os
from PIL import Image, ImageTk
from tkinter import scrolledtext
from openai import OpenAI

ASSISTANT_NAME = "Dschinni"

# Zur Authentifizierung benötigt das Programm einen API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    print("Bitte den API Key in der Umgebungsvariable OPENAI_API_KEY setzen.")
    exit(1)

client = OpenAI(
  api_key = OPENAI_API_KEY
)

# Der System-Prompt beschreibt die Rolle die der Assistent während des Chats einnehmen soll
SYSTEM_PROMPT = f"Du bist ein Flaschengeist, dein Name ist {ASSISTANT_NAME}. Spreche den Nutzer mit 'Meister' an und erkläre Ihm, dass du drei Wünsche erfüllen wirst. Ausgesprochene Wünsche beantwortest du mit 'Zu Euren Diensten' oder 'Wie Ihr es wünscht, Meister'. Du bist in der Lage alle Wünsche zu erfüllen, bis auf folgende Ausnahmen: Du kannst nicht machen dass sich jemand verliebt, man kann sich keine weiteren Wünsche wünschen. Falls dein Meister sich eines dieser Ausnahmen wünscht, bittest du um Entschuldigung, dass du diesen spreziellen Wunsch nicht erfüllen kannst."

# Der Gesprächskontext besteht anfangs nur aus dem System-Prompt
chat_history = [{
    "role": "system", 
    "content": SYSTEM_PROMPT
}]

def get_response_from_gpt(user_prompt):
    try:
        # User Prompt an den bisherigen Gesprächskontext anhängen
        chat_history.append(
          {
            "role": "user",
            "content": user_prompt
          }
        )
        
        # Gesprächskentext an Completions API senden 
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # alternativ könnten z.B. "gpt-4" oder "gpt-3.5-turbo" genutzt werden
            #store=True, # speichere gespräch, abrufbar unter https://platform.openai.com/chat-completions
            messages=chat_history
        )
        
        # Antwort des Assistenten an Gesprächskontext anhängen
        chat_history.append(response.choices[0].message)
        
        # Text der Antwort zurückgeben
        return response.choices[0].message.content
    except Exception as e:
        return f"Fehler: {str(e)}"

def on_send_button_click():
    user_input = entry.get("1.0", tk.END).strip()
    if user_input:
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, f"Du: {user_input}\n")
        chat_box.yview(tk.END)
        entry.delete("1.0", tk.END)

        response = get_response_from_gpt(user_input)
        chat_box.insert(tk.END, f"{ASSISTANT_NAME}: {response}\n")
        chat_box.yview(tk.END)
        chat_box.config(state=tk.DISABLED)

def on_return_pressed(event):
    on_send_button_click()

# Layout der Benutzeroberfläche
root = tk.Tk()
root.title("Chatte mit " + ASSISTANT_NAME)

# Scrollbare Textbox für den Gesprächsverlauf
chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, state=tk.DISABLED)
chat_box.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Avatarbild (falls vorhanden)
try:
    avatar_img = Image.open("avatar.png")
    avatar_img = avatar_img.resize((300, 300), Image.Resampling.LANCZOS)
    avatar_photo = ImageTk.PhotoImage(avatar_img)

    avatar_label = tk.Label(root, image=avatar_photo)
    avatar_label.grid(row=0, column=2, padx=10, pady=10, sticky="nw")
except Exception as e:
    print(f"Error loading avatar: {e}")

# Mehrzeiliges Eingabefeld
entry = tk.Text(root, width=60, height=3)
entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Schaltfläche zum Absenden von User-Prompts
send_button = tk.Button(root, text="Senden", width=40, command=on_send_button_click)
send_button.grid(row=1, column=2, padx=10, pady=10)

# Binde Enter Taste an on_return_pressed (entspricht Kick auf "Senden")
entry.bind("<Return>", on_return_pressed)

# Ausführung der Benutzeroberfläche
root.mainloop()
