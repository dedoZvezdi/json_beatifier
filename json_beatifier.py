import json
import os
import tkinter as tk
from tkinter import filedialog

def select_file(title="Select a JSON file"):
    root = tk.Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename(
        title=title,
        filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
    )
    return file_path

def select_output_file(default_name="output.json", title="Save as..."):
    root = tk.Tk()
    root.withdraw()
    output_path = filedialog.asksaveasfilename(
        title=title,
        defaultextension=".json",
        initialfile=default_name,
        filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
    )
    return output_path if output_path else None

def beautify_json(input_path, output_path=None):
    try:
        with open(input_path, "r", encoding="utf-8") as infile:
            data = json.load(infile)
        
        if not output_path:
            dir_name = os.path.dirname(input_path)
            output_path = os.path.join(dir_name, "beautified_" + os.path.basename(input_path))
        
        with open(output_path, "w", encoding="utf-8") as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii=False)
        
        print(f"Formatting successful! Recorded in: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("1. Select an input JSON file:")
    input_path = select_file()
    
    if not input_path:
        print("No file selected. Exiting...")
        exit()
    
    print("2. Select an output file (or press Cancel to save to the same folder):")
    output_path = select_output_file(default_name="beautified_" + os.path.basename(input_path))
    
    beautify_json(input_path, output_path)