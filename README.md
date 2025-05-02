#  AFK Automation Script – `dscdotggslash143x.py`

A Python script that automates in-game activities like movement, mouse rotation, and chat messages to simulate activity, preventing AFK detection in games like **Call of Duty: Black Ops 6**. The script mimics human behavior by generating random key presses, mouse movements, and chat interactions, making it appear as though you're actively playing even when you're away.

---

##  File Requirement

> **IMPORTANT:**  
> The script **must be named exactly**:
> ```plaintext
> dscdotggslash143x.py
> ```
> If the file is renamed, the script will **not run** and will immediately exit.

---

## 🛠️ Requirements

Before using the script, make sure you have Python installed and the necessary libraries. You can install the required libraries by running:

```bash
pip install pyautogui pydirectinput pynput
```

Important:
You might need to run the script as Administrator on Windows to allow it to control your mouse and keyboard inputs.

▶How to Use
Download or clone the script to your local machine.
Rename the script to dscdotggslash143143x.py (exactly).
Open a terminal or command prompt.
Run the script with Python:

```bash
python dscdotggslash143x.py
```

⌨️ Controls
The script features a couple of simple controls for pausing and stopping the automation:

Key	Action
Right Shift	Pause / Resume
Escape	Kill Switch (Exit)

Pause/Resume: Press Right Shift to toggle between pausing and resuming the script.

Kill Switch: Press Escape to immediately stop the script.

 Features
 Simulated Actions:
The script will simulate human-like activity in-game, including:

Random keyboard inputs: Keys like W, A, S, D, Q, E, Space, and Ctrl are randomly pressed for various durations to simulate movement.
Mouse movements: The mouse moves in circular or zigzag patterns to avoid idle detection.
Mouse clicks: Left and right mouse buttons are clicked randomly.
Random chat messages: The script sends chat messages at random intervals, such as:

"My goldfish is playing for me rn 🐠"
"Keyboard on fire 🔥"
"Beep boop I'm a bot"
"I’m here but spiritually gone"
"Haven’t blinked in 2 hours 👁️👁️"
"Running on 3 FPS and dreams"
"My cat is farming XP"
"This is totally not a bot"

 How It Works
Key Components:
Mouse Movement: The script uses pyautogui to simulate smooth mouse movements. The mouse follows a circular path, moving to random points on the screen at a set interval to prevent the game from detecting inactivity.
Keyboard Inputs: The script simulates key presses for game controls (like movement, crouch, jump, etc.) using pydirectinput. The key actions are randomized to look natural.
Chat Messages: The script sends random messages to simulate in-game communication. This helps further reduce the likelihood of being detected as AFK.
Pausing and Stopping: You can pause and resume the script with Right Shift and stop it entirely with the Escape key.

Flow:
Initialization: The script waits for you to start it and enters a loop where it simulates actions.
AFK Simulation: The script continuously sends random key presses, mouse movements, and chat messages.
Pause/Resume: You can pause the automation by pressing Right Shift, and resume it by pressing the same key again.
Kill Switch: Press Escape to immediately exit the script.

 Customization
Feel free to modify the script to suit your needs. You can:

Customize chat messages: Add or remove phrases in the messages[] list to change the chat output.

Adjust timing: Modify the durations of key presses, mouse movements, and message sending intervals to make the script more or less aggressive.

Add more keys or actions: Modify the key actions in the perform_sequence() function to suit the game controls of your choice.

🛑 Safety Warning
This script is meant for educational purposes and entertainment. Use it responsibly, and ensure that it doesn’t violate the terms of service of the game you are using it with. Running automated scripts in some online games may lead to account bans or other penalties. Always double-check with the game’s policy before using such scripts.
