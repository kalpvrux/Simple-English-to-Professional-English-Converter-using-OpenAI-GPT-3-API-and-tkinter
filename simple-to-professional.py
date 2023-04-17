import openai
import tkinter as tk

# Set up OpenAI API credentials
openai.api_key = "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"

# Define a function to convert simple English to professional English
def convert_to_professional(input_text):
    response = openai.Completion.create(
        engine="davinci",
        prompt=(f"Convert the following sentence to professional English: {input_text}\n"
                "Professional English:"),
        temperature=0.7,
        max_tokens=60,
        n=1,
        stop=None,
        )
    return response.choices[0].text.strip()

# Define a function to handle the conversion when the button is clicked
def convert_button_click():
    input_text = input_textbox.get("1.0", tk.END).strip()
    if input_text:
        output_textbox.delete("1.0", tk.END)
        output_text = convert_to_professional(input_text)
        output_textbox.insert("1.0", output_text)

# Create a tkinter window
window = tk.Tk()
window.title("Simple English to Professional English Converter")

# Create a label and textbox for input
input_label = tk.Label(window, text="Enter a simple English sentence:")
input_label.pack()
input_textbox = tk.Text(window, height=1)
input_textbox.pack()

# Create a label and textbox for output
output_label = tk.Label(window, text="Professional English:")
output_label.pack()
output_textbox = tk.Text(window, height=1)
output_textbox.pack()

# Create a button to convert the text
convert_button = tk.Button(window, text="Convert", command=convert_button_click)
convert_button.pack()

# Run the tkinter event loop
window.mainloop()
