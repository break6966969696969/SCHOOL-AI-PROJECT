import pyttsx3
from youtube_search_python import SearchVideos
from pytube import YouTube
import subprocess
import datetime

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main loop
while True:
    # Get user input
    command = input("Enter a command: ")

    # Process commands
    if command == "quit":
        break
    elif command == "hello":
        speak("Hello! How can I assist you?")
    elif command == "play music":
        speak("Sure! Which song would you like me to play?")
        song = input("Enter the song name: ")
        speak(f"Searching for {song} on YouTube.")

        # Search for the song on YouTube
        search = SearchVideos(song, offset=1, mode="dict", max_results=1)
        results = search.result()

        if len(results["search_result"]) > 0:
            video_id = results["search_result"][0]["id"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            video_title = results["search_result"][0]["title"]
            speak(f"Now playing {video_title}.")

            # Open the video URL in the web browser
            subprocess.run(["start", "", video_url], shell=True)

            speak("Song played successfully.")
        else:
            speak("Sorry, I couldn't find the requested song.")
    elif command == "tell time":
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}.")
    else:
        # Perform the desired action
        # ...

        # Speak the response
        speak("Command executed successfully.")

# Cleanup
engine.stop()
