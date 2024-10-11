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

 Voice Playback Functionality

The voice2.py script plays random voice memo recordings from a specified folder on your system. It uses the pydub library to handle and play .m4a audio files. The script selects a random voice recording each time and allows the user to decide whether to play another recording or exit.

How It Works

	•	The script searches for .m4a files in the Voice Memos folder located at:
/Users/scottsteele/Library/Group Containers/group.com.apple.VoiceMemos.shared/Recordings
	•	It picks a random .m4a file and plays it using the pydub library.
	•	After playing the file, it prompts the user whether they would like to play another recording (y for yes, n for no).

Requirements

To use the voice2.py script, you’ll need the following:

	1.	Install pydub:

 pip install pydub

 	2.	Install an Audio Playback Backend:
	3.	For macOS, you’ll need to install ffmpeg or libav to support .m4a audio playback.
Example (using Homebrew):

brew install ffmpeg

Running the Script

	1.	Run the voice2.py script:
 python3 voice2.py

 	1.	Interact with the Script:
	2.	Once it plays a recording, you will be prompted to play another (y/n).
	3.	The script will exit when you choose not to play another recording.

Customization

	1.	Folder Path: If your recordings are stored in a different location, you can modify the recordings_folder variable to point to the correct folder.
	2.	Supported Formats: While the script is designed for .m4a files, pydub supports various audio formats, such as .mp3 and .wav. You can modify the script to handle 			different file types by changing the file extension in the recordings filter.

This will provide clear documentation about how the voice2.py script works, the requirements for running it, and how it can be customized.


Contributions

Feel free to fork this repository and submit pull requests for improvements or additional features.

License

This project is licensed under the MIT License.




