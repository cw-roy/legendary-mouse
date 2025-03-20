## TODO: correct permissions for pynput regarding permissions on mac

import time
import pyautogui
from pynput import mouse, keyboard
# import logging

# Configuration
IDLE_INTERVAL = 30  # Seconds between mouse movements
MOVE_DISTANCE = 1  # Minimal movement distance

# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


class IdlePreventer:
    def __init__(self, idle_interval, move_distance):
        self.idle_interval = idle_interval
        self.move_distance = move_distance
        self.user_activity_detected = False

    def on_activity(self, *args):
        """Callback function to detect user activity."""
        self.user_activity_detected = True

    def start(self):
        # Set up listeners for user activity
        mouse_listener = mouse.Listener(
            on_move=self.on_activity,
            on_click=self.on_activity,
            on_scroll=self.on_activity,
        )
        keyboard_listener = keyboard.Listener(on_press=self.on_activity)

        # Start listeners
        mouse_listener.start()
        keyboard_listener.start()

        print("Running... Move the mouse or press a key to stop.")

        try:
            while not self.user_activity_detected:
                x, y = pyautogui.position()
                pyautogui.moveTo(x + self.move_distance, y)
                pyautogui.moveTo(x, y)
                time.sleep(self.idle_interval)
        except KeyboardInterrupt:
            print("Exiting...")
        finally:
            mouse_listener.stop()
            keyboard_listener.stop()


if __name__ == "__main__":
    preventer = IdlePreventer(IDLE_INTERVAL, MOVE_DISTANCE)
    preventer.start()


# import time
# import pyautogui
# from pynput import mouse, keyboard

# # Configuration
# IDLE_INTERVAL = 30  # Seconds between mouse movements
# MOVE_DISTANCE = 1  # Minimal movement distance

# user_activity_detected = False  # Flag to stop the script on user input


# def on_activity(*args):
#     """Callback function to detect user activity."""
#     global user_activity_detected
#     user_activity_detected = True


# def main():
#     global user_activity_detected

#     # Set up listeners for user activity
#     mouse_listener = mouse.Listener(on_move=on_activity, on_click=on_activity, on_scroll=on_activity)
#     keyboard_listener = keyboard.Listener(on_press=on_activity)

#     # Start listeners
#     mouse_listener.start()
#     keyboard_listener.start()

#     print("Running... Move the mouse or press a key to stop.")

#     try:
#         while not user_activity_detected:
#             x, y = pyautogui.position()
#             pyautogui.moveTo(x + MOVE_DISTANCE, y)
#             pyautogui.moveTo(x, y)
#             time.sleep(IDLE_INTERVAL)
#     except KeyboardInterrupt:
#         print("Exiting...")
#     finally:
#         mouse_listener.stop()
#         keyboard_listener.stop()


# if __name__ == "__main__":
#     main()
