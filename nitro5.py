import pyautogui
import time

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
        
        # Optional: Add a verification step to check if the UI state has changed to 'Not Ready'
        # You could check for a visual or state change in the system here
        
        print(f"Attempt {attempt + 1} to click '{description}' completed.")
        return True
    
    print(f"Failed to click '{description}' after {max_attempts} attempts.")
    return False

# Coordinates for the outbound dialing and voicemail handling
not_ready_coords = (2009, 177)
ready_voice_coords = (2002, 208)
call_button_coords = (1997, 934)

voicemail_noanswer_coords = (2349, 760)
end_call_coords = (2066, 876)
set_disposition_coords = (2064, 935)
call_back_coords = (1940, 375)  # This is a radio button
end_interaction_coords = (2067, 934)
confirm_coords = (2057, 767)

cancel_coords_0 = (2049, 619)
cancel_coords_1 = (2055, 618)
cancel_coords_2 = (2056, 652)
cancel_coords_3 = (2066, 612)

save_end_call_coords = (2351, 198)
dropdown_coords = (2439, 724)
voicemail_option_coords = (2429, 774)

# Function to simulate outbound dialing and initiating a call
def make_call():
    """Simulate making a call by performing the steps in sequence."""
    move_and_double_click(*not_ready_coords, "Not Ready dropdown")
    time.sleep(0.5)  # Increased delay for better handling of the dropdown

    move_and_double_click(*ready_voice_coords, "Ready (Voice) option")
    time.sleep(0.5)  # Wait for system to process

    move_and_double_click(*call_button_coords, "Call button")
    time.sleep(0.5)  # Allow time for call to initiate

    print("Call sequence completed.")

# Function to select 'Voicemail-NoAnswer'
def select_voicemail_noanswer():
    """Select 'Voicemail-NoAnswer' from the dropdown."""
    move_and_click(*dropdown_coords, "Dropdown", clicks=2)
    time.sleep(.5)  # Allow time for the dropdown to fully open

    move_and_click(*voicemail_option_coords, "Voicemail-NoAnswer option")
    time.sleep(.5)  # Short pause to ensure the option registers

# Function to complete the remaining steps (ending call, disposition, etc.)
def leave_voicemail_and_complete():
    """Simulate the process of leaving a voicemail and completing all steps."""
    move_and_double_click(*end_call_coords, "End Call")
    time.sleep(.5)

    move_and_click(*set_disposition_coords, "Set Disposition")
    time.sleep(.5)

    move_and_click(*call_back_coords, "Call Back")
    time.sleep(.5)

    move_and_click(*end_interaction_coords, "End Interaction")
    time.sleep(.5)

    move_and_click(*confirm_coords, "Confirm")
    time.sleep(0.5)

    # Try all 'Cancel' button locations
    cancel_coords_list = [cancel_coords_0, cancel_coords_1, cancel_coords_2, cancel_coords_3]
    for i, cancel_coords in enumerate(cancel_coords_list):
        move_and_click(*cancel_coords, f"Cancel (location {i + 1})")
        time.sleep(0.2)

    move_and_click(*save_end_call_coords, "Save & End Call")
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
        retry_not_ready_click(*not_ready_coords, "Not Ready")
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
