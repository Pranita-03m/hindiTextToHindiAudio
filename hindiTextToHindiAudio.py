import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pyttsx3
from pydub import AudioSegment
from pydub.playback import play


def hindi_text_to_audio(text, voice_id, output_filename="output.wav"):
    try:
        # Initialize pyttsx3 engine
        engine = pyttsx3.init()

        # Set the selected Hindi voice
        engine.setProperty('voice', voice_id)

        # Save the Hindi text as an audio file
        engine.save_to_file(text, output_filename)
        engine.runAndWait()
        return output_filename
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        return None


def convert_text_to_audio():
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input Required", "Please enter Hindi text.")
        return

    selected_voice = voice_selector.get()
    if selected_voice == "Kalpana":
        voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\MSTTS_V110_hiIN_KalpanaM"
    elif selected_voice == "Hemant":
        voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\MSTTS_V110_hiIN_HemantM"
    else:
        messagebox.showerror("Error", "Please select a valid voice.")
        return

    output_filename = "output.wav"
    output_file = hindi_text_to_audio(text, voice_id, output_filename)

    if output_file:
        messagebox.showinfo("Success", f"Audio saved as '{output_filename}'")
        play_audio(output_file)


def save_audio_file():
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input Required", "Please enter Hindi text.")
        return

    selected_voice = voice_selector.get()
    if selected_voice == "Kalpana":
        voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\MSTTS_V110_hiIN_KalpanaM"
    elif selected_voice == "Hemant":
        voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\MSTTS_V110_hiIN_HemantM"
    else:
        messagebox.showerror("Error", "Please select a valid voice.")
        return

    # Ask user for the save location
    output_file = filedialog.asksaveasfilename(defaultextension=".wav",
                                               filetypes=[("WAV files", "*.wav")],
                                               title="Save Audio File")
    if output_file:
        hindi_text_to_audio(text, voice_id, output_file)
        messagebox.showinfo("Success", f"Audio saved as '{output_file}'")


def play_audio(file_path):
    try:
        audio = AudioSegment.from_file(file_path, format="wav")
        play(audio)
    except Exception as e:
        messagebox.showerror("Error", f"Unable to play audio: {str(e)}")


# GUI Setup
def setup_gui():
    window = tk.Tk()
    window.title("Hindi Text-to-Speech with Voice Selection")
    window.geometry("500x450")

    # Instruction Label
    instruction_label = tk.Label(window, text="Enter Hindi Text Below:", font=("Arial", 14))
    instruction_label.pack(pady=10)

    # Text Input Box
    global text_input
    text_input = tk.Text(window, height=10, width=50, font=("Arial", 12))
    text_input.pack(pady=10)

    # Voice Selection Label and Dropdown
    voice_label = tk.Label(window, text="Select Voice:", font=("Arial", 12))
    voice_label.pack(pady=5)

    global voice_selector
    voice_selector = ttk.Combobox(window, values=["Kalpana", "Hemant"], state="readonly", font=("Arial", 12))
    voice_selector.set("Kalpana")  # Default voice
    voice_selector.pack(pady=5)

    # Convert Button
    convert_button = tk.Button(window, text="Convert to Audio", command=convert_text_to_audio, font=("Arial", 12), bg="green", fg="white")
    convert_button.pack(pady=5)

    # Save Button
    save_button = tk.Button(window, text="Save as File", command=save_audio_file, font=("Arial", 12), bg="blue", fg="white")
    save_button.pack(pady=5)

    # Exit Button
    exit_button = tk.Button(window, text="Exit", command=window.quit, font=("Arial", 12), bg="red", fg="white")
    exit_button.pack(pady=5)

    window.mainloop()


if __name__ == "__main__":
    setup_gui()
