import time
import pyautogui

def get_click_location():
    print("Move the mouse to the desired location for the click.")
    print("I will capture the location in 3 seconds.")

    # Countdown before capturing mouse position
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)

    x, y = pyautogui.position()
    print(f"Click location: ({x}, {y})")
    return x, y

def type_text(phrase):
    pyautogui.typewrite(phrase, interval=0.1)  # Adjust the interval for typing speed

def main():
    # Get click location for typing
    x, y = get_click_location()

    # Ask the user what to type
    phrase = input("What phrase do you want to type? ")

    # Move the mouse to the specified location and click
    pyautogui.click(x, y)

    # Type the specified phrase with human-like typing speed
    type_text(phrase)

if __name__ == "__main__":
    main()
