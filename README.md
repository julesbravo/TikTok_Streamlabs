# TikTok_Streamlabs
A python script to write TikTok Live Stream events to a file to be used for Streamlabs labels.

Currently, this only works for recent subscribers and followers, but can easily be updated in the future to include other event types.

## Requirements
* [Python](https://www.python.org/downloads/)
* [TikTokLive](https://github.com/isaackogan/TikTokLive)

## Getting Started
1. Install Python by going to https://www.python.org/downloads/ and downloading and installing the latest version available.
2. From a terminal/command prompt install the [TikTokLive python library](https://github.com/isaackogan/TikTokLive) by entering `pip install TikTokLive`. Note: On Mac OS you may need to use `pip3 install TikTokLive` 
3. [Download](https://github.com/julesbravo/TikTok_Streamlabs/archive/refs/heads/main.zip) this repository and unzip it.
4. Open the start.py file in a code/text editor.
5. Edit the `subscribersLog` value to be the location of the file of your recent subscribers file for Streamlabs labels.
6. Edit the `followersLog` value to be the location of the file of your recent followers file for Streamlabs labels.
7. Edit the `streamerId` value to be your TikTok username including the `@`.
8. Start your TikTok live stream.
9. Go to the location of this repository in the terminal/command prompt and run `python start.py`.

