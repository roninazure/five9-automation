Five9 Automation Script

This project automates interactions with the Five9 contact center platform using Python and PyAutoGUI. The script simulates outbound call handling, voicemail selection, and other workflow actions within the Five9 interface.

Features

	•	Automates mouse clicks through the Five9 interface.
	•	Handles actions such as selecting “Not Ready,” “Ready (Voice),” and “Voicemail-NoAnswer.”
	•	Configurable screen coordinates via the config.yaml file for flexible UI adaptation.
	•	Designed for repeated execution until manually stopped.

Requirements

To run the automation script, you’ll need:

	•	Python 3.x
	•	Required Python libraries:
	•	pyautogui
	•	pyyaml

You can install the necessary libraries with:

pip install pyautogui pyyaml

Setup
1. Clone the Repository:
 	git clone https://github.com/roninazure/five9-automation.git
	cd five9-automation
2. Set Up a Virtual Environment (optional but recommended):
	python3 -m venv venv
	source venv/bin/activate
3. Install Dependencies:
   	pip install -r requirements.txt
4.	Configure the config.yaml File:
   	The config.yaml file contains all the screen coordinates required to interact with the Five9 UI. Modify these coordinates as necessary 		to match your screen resolution and the current layout of the Five9 interface.
	
Example config.yaml:

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

1. Start the Script:
Once your environment is set up and config.yaml is configured, you can start the script by running:

python3 nitro6.py

2. Script Workflow:
	The script simulates mouse clicks in the Five9 interface, handling tasks like making outbound calls, selecting voicemail options, and 		ending calls.
	The script runs continuously until manually stopped.
3. Manual Inputs:
   	After each call, the script will ask whether the call was answered or if it went to voicemail.
   	You’ll need to confirm when the voicemail is complete before the script proceeds to the next call.

Customization
	•	Adjusting Coordinates: If your UI changes or you switch screens, you can easily update the coordinates in the config.yaml file.
	•	Adding New Actions: You can expand the script by adding more functionality to the nitro6.py file.


Troubleshooting
	•	Timing Issues: If the script is running too slowly or too quickly, adjust the time.sleep() values in the nitro6.py script.
	•	Coordinate Issues: Ensure the config.yaml coordinates are accurate and match your current screen resolution and UI elements.

Contributions

Feel free to fork this repository and submit pull requests for improvements or additional features.

License

This project is licensed under the MIT License.




