# YouTube Video Downloader
## Project Description
### What it does
The main script can be used to start up a GUI for downloading YouTube videos. The currently available features include:
1. Downloading videos
2. Choosing a download directory via a file dialog window
3. Giving a specific file name for the downloaded video
4. Displaying the thumbnail and title of the video that will be downloaded

### What technologies were used
This project is built with python, including some libraries such as:
1. Pillow / PIL
2. io (specifically BytesIO)
3. urllib
4. pytube
5. tkinter

### Challenges in making this
I had a hard time setting paths for download because sometimes the backslash when copy pasting paths messes things up. Another challenge I encountered was displaying the thumbnail of the video.

### What's the plan?
After this I hope to add a progress bar or something alike to show users the download progress of longer videos, because currently when a long video is being downloaded, the GUI window just freezes.

### Credits
Credits to Kumar Shubham, Lalithnarayan C, Rishabh Bansal, and other amazing writers who have made pytube and tkinter articles on the web.

## How to Use
If you want to try this project out, you can simple copy and paste the main python script to your text editor.
