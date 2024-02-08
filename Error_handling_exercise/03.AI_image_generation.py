import json
import tkinter as tk
import urllib.request
from io import BytesIO

import requests
from PIL import ImageTk, Image


def display_image(image_url):
    with urllib.request.urlopen(image_url) as url:
        image_data = url.read()  # download the image

    image_stream = BytesIO(image_data)
    image = ImageTk.PhotoImage(Image.open(image_stream))

    image_label.config(image=image)
    image_label.image = image  # keeps reference to the image


def get_image_url():
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMmUwNTUyOTItODAxNy00ZGU1LTg2ZDctZWQ4NDM1ZDFiNzZlIiwidHlwZSI6ImFwaV90b2tlbiJ9.vCDIV_Tt-o_RHcxO-JVDQLnxOq0nOF2RetqoXB9oOvM"}

    url = "https://api.edenai.run/v2/image/generation"
    payload = {
        "providers": "openai",
        "text": input_field.get(),
        "resolution": "256x256",
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    return result['openai']['items'][0]["image_resource_url"]


def render_image():
    print("Clicked")
    try:
        error_label.place_forget()
        image_url = get_image_url()
    except KeyError:
        error_label.place(x=175, y=50)
    else:
        display_image(image_url)


window = tk.Tk()
window.title("AI Image Generator")
window.geometry("500x350")

error_label = tk.Label(window, text="Prompt cannot be empty!", fg="red")

input_field = tk.Entry(window, width=14)
input_field.place(x=120, y=20)

image_label = tk.Label(window)
image_label.place(x=150, y=50)

generate_button = tk.Button(window, text="Create", height=1, command=render_image)
generate_button.place(x=300, y=18)

window.mainloop()
