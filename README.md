# Simple English to Professional English Converter using OpenAI GPT-3 API and tkinter

This is a Python script that uses the OpenAI GPT-3 API and the tkinter module to convert a simple English sentence to professional English. The user enters a simple English sentence in a tkinter window, and the script sends it to the OpenAI API for conversion. The converted professional English sentence is then displayed in the same window.

## Getting Started
To use this script, you need to install the following Python packages:

* OpenAI
* tkinter

You can install these packages using pip, the Python package manager.
```
pip install openai tkinter
```
You also need an OpenAI API key, which you can get by creating an account on the OpenAI website. The script is designed to use the Davinci engine of the OpenAI API, which is the most powerful and accurate engine. However, it requires a paid subscription to OpenAI. If you don't have a subscription, you can use the GPT-3 API's other engines like Curie, Babbage, Ada, etc.

## Usage
To use the script, simply run the Python file simple-to-professional.py. A tkinter window will appear, where you can enter a simple English sentence and click the "Convert" button to convert it to professional English. The converted sentence will appear in the same window.
```
python simple-to-professional.py
```
## Example
Here's an example of how to use the script:
```
import openai
import tkinter as tk
from tkinter import *

# Set up OpenAI API credentials
openai.api_key = "your-api-key"

# Set up tkinter window
root = tk.Tk()
root.title("Simple to Professional English Converter")

# Define function to convert simple English to professional English
def convert():
    # Get input text from tkinter window
    input_text = entry.get()

    # Use OpenAI GPT-3 API to convert input text to professional English
    response = openai.Completion.create(
        engine="davinci",
        prompt=input_text + " is written in simple English. Please convert it to professional English.",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Get converted text from OpenAI API response
    converted_text = response.choices[0].text.strip()

    # Display converted text in tkinter window
    output_label.config(text=converted_text)

# Create tkinter widgets
label = Label(root, text="Enter a simple English sentence:")
label.pack()

entry = Entry(root)
entry.pack()

button = Button(root, text="Convert", command=convert)
button.pack()

output_label = Label(root, text="")
output_label.pack()

# Run tkinter main loop
root.mainloop()
```
## Contributing
If you find any issues with the script or want to suggest new features, please feel free to submit an issue or pull request on the GitHub repository.

## License
> This project is licensed under the MIT License. See the LICENSE file for details.
