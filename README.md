# JSON Beautifier Tool  

📂 **Tool for formatting JSON files** with proper indentation and structure.  
✅ User-friendly (GUI file selection) | Custom output path  

---

## 🛠 Features  
- **Formats JSON files** with 4-space indentation.  
- **Preserves Unicode characters** (no `ensure_ascii` corruption).  
- **Interactive file selection** (no manual path typing).  
- **Flexible output**:  
  - Save to a custom location.  
  - Default: Creates `beautified_<original_name>.json` in the input file's folder.  
- **Error handling** (clear messages if JSON is invalid).  

---

## ⚙️ Installation  
1. **Requirements**:  
   - Python 3.6+  
   - `tkinter` (usually included with Python).  

2. **Install dependencies** (if needed):  
   ```bash  
   pip install tk

---

## 🚀 Usage

### **GUI Method (Recommended)**
1. Run the script:
   ```bash
   python json_beautifier.py
2. Follow the prompts:
- Select input JSON file  
- Choose output location (or press Cancel for default)  

---

Drag & Drop:  
- Simply drag a `.json` file onto `json_beautifier.py`  
- Automatically creates `beautified_<input_name>.json` in the same folder

### **Command Line Usage**
```bash
python json_beautifier.py input.json [output.json] 
```

---

## 📝 Example
### **Before (`compact.json`):**
```json
{"name":"Alice","skills":["Python","JSON"],"meta":{"version":1.2}}
```
### **After (`beautified_compact.json`):**
```json
{
    "name": "Alice",
    "skills": [
        "Python",
        "JSON"
    ],
    "meta": {
        "version": 1.2
    }
}
```
---

## 🐛Troubleshooting
- "Invalid JSON" error: Ensure your input file is valid JSON.
- "No file selected": Cancel was pressed during file selection.
- Encoding issues: Script forces UTF-8; override if needed (e.g., encoding="latin1").

