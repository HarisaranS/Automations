import moviepy.editor as mp 


path = input("Enter the path for the video file:")

videoclip = mp.VideoFileClip(path)
audioclip = videoclip.audio
audioclip.write_audiofile("extracted_audio.mp3")
audioclip.close()
videoclip.close()   

print("Audio extracted and saved as extracted_audio.mp3")

