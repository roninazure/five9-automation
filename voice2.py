from pydub import AudioSegment
from pydub.playback import play
import os
import random

def play_random_recording():
    recordings_folder = "/Users/scottsteele/Library/Group Containers/group.com.apple.VoiceMemos.shared/Recordings"
    recordings = [f for f in os.listdir(recordings_folder) if f.endswith('.m4a')]
    
    if recordings:
        random_recording = random.choice(recordings)
        recording_path = os.path.join(recordings_folder, random_recording)
        print(f"Playing: {random_recording}")

        # Load and play the .m4a file
        audio = AudioSegment.from_file(recording_path, format="m4a")
        play(audio)
    else:
        print("No recordings found.")

while True:
    play_random_recording()
    
    # Prompt to run again
    user_input = input("Do you want to play another recording? (y/n): ").strip().lower()
    
    if user_input != 'y':
        print("Exiting.")
        break
