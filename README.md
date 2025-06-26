# 📁 File Manager GUI

A user-friendly, PyQt5-based graphical interface for performing basic file management operations — such as browsing directories, editing text files, finding file types, and creating or deleting files — all within a modern, dark-themed interface.

---

## 📑 Index

- [🚀 Features](#-features)
- [🛠️ Requirements](#️-requirements)
- [🧪 Create and Use a Virtual Environment](#-create-and-use-a-virtual-environment)
  - [📥 Step 1: Create the Virtual Environment](#-step-1-create-the-virtual-environment)
  - [⚙️ Step 2: Activate the Virtual Environment](#-step-2-activate-the-virtual-environment)
  - [📦 Step 3: Install All Required Packages](#-step-3-install-all-required-packages)
- [🔧 Convert to .exe with PyInstaller](#-convert-to-exe-with-pyinstaller)
  - [Step 1: Install PyInstaller](#step-1-install-pyinstaller)
  - [Step 2: Create the Executable](#step-2-create-the-executable)
  - [Step 3: Locate the Executable](#step-3-locate-the-executable)
- [📦 How to Run](#-how-to-run)
- [📸 Interface Preview](#-interface-preview)
- [📄 Copyright](#-copyright)

---

## 🚀 Features
&nbsp;
- 📍 **Current Directory Viewer** — Displays your current working directory
- 📁 **Change Directory** — Choose and switch to another folder
- 🔍 **Find File Types** — Search for specific file extensions (e.g., `.txt`, `.py`)
- 📄 **Show All Files** — List all files and folders in the current directory
- ✏️ **Edit Text File** — Edit or append text to `.txt` files directly
- ➕➖ **Add / Remove File** — Create or delete a file by name
- 🧹 **Clear Console** — Clear the output area
- ❌ **Exit** — Close the application

---

## 🛠️ Requirements

&nbsp;
Make sure you have Python 3.x and the following library installed:

- PyQt5
- PyInstaller
- Venv ( Virtual Enviroment )

---
&nbsp;
&nbsp;
## 🧪 Create and Use a Virtual Environment

Using a virtual environment helps isolate dependencies and keep your project clean.

### 📥 Step 1: Create the Virtual Environment

Run the following command in your project directory:

```bash
python -m venv venv
```
### ⚙️ Step 2: Activate the Virtual Environment

#### 🪟 In Dedicated Terminal On Windows:

```bash
venv\Scripts\activate
```
or

#### 🪟 In Dedicated Terminal On (Linux / macOS):

```bash
source venv/bin/activate
```
---


### 📦 Step 3: Install All Required Packages

Once your virtual environment is activated, install the dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```
&nbsp;
&nbsp;
---
## 🔧 Convert to .exe with PyInstaller

To turn the application into a Windows executable, follow these steps:

### Step 1: Install PyInstaller

First, install **PyInstaller** by running:

``` bash
pip install PyInstaller
```

---


### Step 2: Create the Executable

1. Open a terminal (or Command Prompt on Windows) and navigate to the directory where the main Python file (`main_GUI.py`) is located.
2. Run the following command:

``` bash
pyinstaller --onefile -w '.\main_GUI.py'
```
or 

``` bash
python -m PyInstaller --onefile -w .\main_GUI.py
```



#### Explanation of options:
- `--onefile`: Bundles the entire application into a single executable file.
- `--windowed`: Prevents a terminal window from opening when running the GUI (recommended for GUI applications).

---
### Step 3: Locate the Executable

Once PyInstaller finishes, the `.exe` file will be found in the `dist` folder:


&nbsp;
&nbsp;

## 📦 How to Run

1. Clone or download the repository.

    ```bash
    git clone https://github.com/TaleeBarbieri/Python_File_Explorer.git
    ```

2. Navigate into the project directory.
    ```bash
    cd .\Python_File_Explorer\
    ```
3. Run the main Python file.
    ```bash
    python3 main_GUI.py
    ```
4. Enjoy 😀 !!!
---


## 📸 Interface Preview  

![alt text](<media/Screenshot 2025-05-13 105352.png>) ![alt text](<media/Screenshot 2025-05-13 105437.png>) ![alt text](<media/Screenshot 2025-05-13 105457.png>) ![alt text](<media/Screenshot 2025-05-13 105519.png>) ![alt text](<media/Screenshot 2025-05-13 105539.png>)
---

## 📄 Copyright

This project was made by Talee Barbieri and John Beresford 