# Five9 Automation Script

This project automates interactions with the Five9 contact center platform using Python and PyAutoGUI. The script is designed to simulate outbound call handling, voicemail selection, and other workflow actions.

## Features
- Automates clicking through Five9's interface.
- Handles tasks like selecting "Not Ready," "Ready (Voice)," and "Voicemail-NoAnswer."
- Configurable coordinates via a `config.yaml` file for flexible UI changes.
- Designed for repeated use until manually stopped.

## Requirements

To run the automation script, you'll need the following:
- Python 3.x
- Required Python libraries:
  - `pyautogui`
  - `pyyaml`
  
You can install these libraries using pip:
```bash
pip install pyautogui pyyaml

Setup

	1.	Clone the Repository:
git clone https://github.com/roninazure/five9-automation.git
cd five9-automation

	2.	Set Up Your Virtual Environment (Optional but Recommended):
python3 -m venv venv
source venv/bin/activate

	3.	Install Dependencies:
pip install -r requirements.txt

	4.	Configure the config.yaml File:
	•	The config.yaml file contains all the screen coordinates for the Five9 UI. Edit this file as necessary to match your current screen resolution and Five9 interface.
	•	Example config.yaml:

coordinates:
  not_ready_coords: [2009, 177]
  ready_voice_coords: [2002, 208]
  call_button_coords: [1997, 934]
  voicemail_noanswer_coords: [2349, 760]
  end_call_coords: [2066, 876]
  set_disposition_coords: [2064, 935]
  call_back_coords: [1940, 375]
  end_interaction_coords: [2067, 934]
  confirm_coords: [2057, 767]
  cancel_coords_0: [2049, 619]
  cancel_coords_1: [2055, 618]
  cancel_coords_2: [2056, 652]
  cancel_coords_3: [2066, 612]
  save_end_call_coords: [2351, 198]
  dropdown_coords: [2439, 724]
  voicemail_option_coords: [2429, 774]

Running the Script

	1.	Start the Script:
Once your environment is set up and config.yaml is configured, run the script:
python3 nitro6.py


2.	Workflow:
	•	The script will simulate mouse clicks through the Five9 interface, making outbound calls, selecting voicemail options, and handling the end of the call.
	•	The script runs continuously until manually stopped.
	3.	Manual Inputs:
	•	The script will ask if the call was answered or if it went to voicemail.
	•	You’ll need to confirm when the voicemail message is complete before the script proceeds.

Customization

	•	Adjusting Coordinates: If your UI changes or you switch screens, you can update the coordinates in the config.yaml file.
	•	Adding New Actions: Feel free to add new functionality to the script by modifying the nitro6.py file.

Troubleshooting

	•	Timing Issues: If the script is running too slowly or too quickly, adjust the time.sleep() values in the nitro6.py script.
	•	Coordinate Issues: Ensure your config.yaml coordinates are accurate and match your screen resolution and UI elements.

Contributions

Feel free to fork this project and submit pull requests for improvements or additional features.

License

This project is licensed under the MIT License.












