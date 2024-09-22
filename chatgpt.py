import os
import openai #pip install openai
import tkinter as tk

def generate():
    prompt= ent_qst.get()

    openai.api_key = os.getenv("OPENAI_API_KEY")

    response= openai.ChatCompletion.create(
        model= "gpt-4-turbo",
        messages=[
            {"role":"user", "content": prompt}
        ]
    )

def clear():
    txt_result.delete(1.0, tk.END)

root = tk.Tk()
root.title("AI Chatbot")
root.geometry("400x600")
root.config(background="black")

lbl_head = tk.Label(root, text= "ChatGPT", font=("arial", 27), bg="black", fg="white")
lbl_head.pack(fill="x", pady=10,)

frm_result=tk.Frame(root)
scroll_bar= tk.Scrollbar(frm_result)
scroll_bar.pack(side="right", fill="y")


txt_result = tk.Text(root, font=("geogio", 12), yscrollcommand=scroll_bar.set)
txt_result.pack(fill="x")

frm_result.pack(padx=10, pady=5, fill="x")



ent_qst = tk.Entry(root, font=("geogio, 15"))
ent_qst.pack(padx=10, pady=5, fill="x" )

btn_gen = tk.Button(root, font=("geogio", 15), text="Generate", command=generate)
btn_gen.pack(padx=10, fill="x")

scroll_bar.config(command=txt_result.yview)


btn_clear = tk.Button(root, font=("georio", 15), text="Clear", command=clear)
btn_clear.pack(padx=10,pady=2, fill="x")



root.mainloop()

