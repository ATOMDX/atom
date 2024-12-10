import time

def animate_text(text, speed=0.1):
    for char in text:
        print(char, end='', flush=True)  # Print each character without a newline
        time.sleep(speed)  # Pause for the specified speed
    print()  # Move to the next line after the text is fully written

# Example usage
text = "TOOLS OFF"
animate_text(text, 0.1)  # Adjust the speed (in seconds)
