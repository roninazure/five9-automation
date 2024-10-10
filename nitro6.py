import pyautogui
import time
import yaml

# Load the YAML configuration file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Extract the coordinates from the YAML configuration
coords = config['coordinates']

# Function to move and click (for single and double clicks)
def move_and_click(x, y, description, clicks=1):
    """Move the mouse to the given coordinates and click."""
    print(f"Moving to '{description}' at ({x}, {y}) and clicking {clicks} time(s)...")
    pyautogui.moveTo(x, y)
    time.sleep(0.2)  # Short delay for proper mouse movement
    pyautogui.click(clicks=clicks)
    print(f"Clicked on '{description}'.")

# Function to move and double-click
def move_and_double_click(x, y, description):
    """Move the mouse to the given coordinates and double-click."""
    print(f"Moving to '{description}' at ({x}, {y}) and double-clicking...")
    pyautogui.moveTo(x, y)
    time.sleep(0.2)  # Short delay before double-clicking
    pyautogui.doubleClick()
    print(f"Double-clicked on '{description}'.")

# Retry function for "Not Ready" click
def retry_not_ready_click(x, y, description, max_attempts=3):
    """Retry clicking on 'Not Ready' with multiple attempts."""
    for attempt in range(max_attempts):
        print(f"Attempt {attempt + 1} to click '{description}'...")
        pyautogui.moveTo(x, y)
        time.sleep(0.3)  # Allow mouse movement to complete
        pyautogui.click()
        time.sleep(1)  # Give time for the system to process the click
        print(f"Attempt {attempt + 1} to click '{description}' completed.")
        return True
    
    print(f"Failed to click '{description}' after {max_attempts} attempts.")
    return False

# Function to simulate outbound dialing and initiating a call
def make_call():
    """Simulate making a call by performing the steps in sequence."""
    move_and_double_click(*coords['not_ready_coords'], "Not Ready dropdown")
    time.sleep(0.5)  # Increased delay for better handling of the dropdown

    move_and_double_click(*coords['ready_voice_coords'], "Ready (Voice) option")
    time.sleep(0.5)  # Wait for system to process

    move_and_double_click(*coords['call_button_coords'], "Call button")
    time.sleep(0.5)  # Allow time for call to initiate

    print("Call sequence completed.")

# Function to select 'Voicemail-NoAnswer'
def select_voicemail_noanswer():
    """Select 'Voicemail-NoAnswer' from the dropdown."""
    move_and_click(*coords['dropdown_coords'], "Dropdown", clicks=2)
    time.sleep(0.5)  # Allow time for the dropdown to fully open

    move_and_click(*coords['voicemail_option_coords'], "Voicemail-NoAnswer option")
    time.sleep(0.5)  # Short pause to ensure the option registers

# Function to complete the remaining steps (ending call, disposition, etc.)
def leave_voicemail_and_complete():
    """Simulate the process of leaving a voicemail and completing all steps."""
    move_and_double_click(*coords['end_call_coords'], "End Call")
    time.sleep(0.5)

    move_and_click(*coords['set_disposition_coords'], "Set Disposition")
    time.sleep(0.5)

    move_and_click(*coords['call_back_coords'], "Call Back")
    time.sleep(0.5)

    move_and_click(*coords['end_interaction_coords'], "End Interaction")
    time.sleep(0.5)

    move_and_click(*coords['confirm_coords'], "Confirm")
    time.sleep(0.5)

    # Try all 'Cancel' button locations
    cancel_coords_list = [coords['cancel_coords_0'], coords['cancel_coords_1'], coords['cancel_coords_2'], coords['cancel_coords_3']]
    for i, cancel_coords in enumerate(cancel_coords_list):
        move_and_click(*cancel_coords, f"Cancel (location {i + 1})")
        time.sleep(0.2)

    move_and_click(*coords['save_end_call_coords'], "Save & End Call")
    time.sleep(1)

# Main workflow to handle the complete process
def call_workflow():
    """Main workflow to handle call interaction."""
    make_call()

    # Ask if the call was answered or went to voicemail
    call_status = input("Call answered (a) or Voicemail (v)? ").strip().lower()
    
    if call_status == "a":
        print("Call was answered. Ending the script.")
        return False
    elif call_status == "v":
        select_voicemail_noanswer()
        input("Leave the voicemail and press Enter when done.")

        leave_voicemail_and_complete()

        # Retry clicking 'Not Ready' after voicemail completion
        retry_not_ready_click(*coords['not_ready_coords'], "Not Ready")
        return True
    else:
        print("Invalid input.")
        return False

# Main loop for repeating the process
while True:
    if not call_workflow():
        break
    
    print("Proceeding to the next call...")
    time.sleep(1)

print("All voicemail sequences completed.")
