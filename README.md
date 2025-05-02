# Pixeldoro Timer ⏱️

![App Screenshot](/assets/screenshot.png)  
*A customizable productivity timer based on the Pomodoro Technique*

[![GitHub release](https://img.shields.io/github/v/release/yourusername/PomodoroTimer)](https://github.com/Bebok3Q/Pixeldoro-Timer/releases)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Downloads](https://img.shields.io/github/downloads/yourusername/PomodoroTimer/total)](https://github.com/Bebok3Q/Pixeldoro-Timer/releases)

## Features ✨
- 🕒 **Preset Timers**: 25-minute work / 5-minute break (customizable)
- 🔔 **Sound Notifications**: Gentle alerts when time expires
- 🎨 **Custom UI**: Clean interface with theming support
- ⚙️ **Settings Panel**: Adjust durations and auto-break toggles
- 📦 **Single EXE**: No installation needed (Windows)

## Installation 📥
### Option 1: Download Pre-built (Windows)
1. Go to [Releases](https://github.com/Bebok3Q/Pixeldoro-Timer/releases)
2. Download `PomodoroTimer.exe`
3. Double-click to run

### Option 2: Run from Source
# Clone the repository
git clone https://github.com/Bebok3Q/Pixeldoro-Timer.git

# Install dependencies
pip install tkinter playsound

# Run
python main.py

#Usage 🖱️
Start: Click "Start" to begin the work timer
Pause: Use "Stop" to pause the session
Reset: Restart with current settings
Customize: Adjust durations in Settings

#Build Your Own 🔨
To compile from source:
pip install pyinstaller
pyinstaller --onefile --windowed --icon=assets/icon.ico --name PomodoroTimer main.py


## Roadmap 🗺️
- [x] Basic timer functionality  
- [ ] Task tracking integration  
- [ ] Cross-platform builds (Mac/Linux)
