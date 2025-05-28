# dzen-private-video-downloader
This utility automates downloads of private videos (e.g. Premium content) from [Dzen](https://dzen.ru/).

The tool uses in-browser authentication in order to access a user's content that is not publicly available.

## Requirements
- Python 3+
- Install deps from `requirements.txt`

## Usage
1. Run the `main.py`
2. When a browser opens the Dzen, authenticate via your user
3. When prompted in the CLI - paste a video URL to download (it's either a video link or shared link)
4. Hit <enter>
5. The script will open the video and will start its download (in-browser)
6. You may add another videos for download
7. Enter `exit` whenever you want to exit the program
