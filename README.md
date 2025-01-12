# J.A.R.V.I.S Virtual Assistant

A Python-based virtual assistant created by **ChiragPatankar** that performs various tasks like weather updates, currency conversion, opening websites, fetching news, and interacting with OpenAI's ChatGPT, among other functionalities.

---

## Features

- **Text-to-Speech:** Converts text responses to speech using `pyttsx3`.
- **Voice Commands:** Listens and processes voice commands with `speech_recognition`.
- **Weather Updates:** Fetches real-time weather information using the OpenWeatherMap API.
- **News Headlines:** Retrieves the latest top 5 headlines from NewsAPI.
- **Currency Conversion:** Converts currencies in real-time using `forex_python`.
- **Website Navigation:** Opens popular websites like YouTube, Google, and Wikipedia.
- **Search Engine Integration:** Performs Google and YouTube searches via voice commands.
- **Volume Control:** Adjusts the system's volume.
- **Timer Functionality:** Sets a timer and notifies when the time is up.
- **ChatGPT Integration:** Answers queries using OpenAI's GPT-3.5-turbo model.

---

## Installation

### Prerequisites
Ensure you have the following installed:

- Python 3.7 or higher
- Pip (Python package manager)

### Required Libraries

Install the required Python libraries by running:
```bash
pip install opencv-python speechrecognition pyttsx3 pywhatkit pytz forex-python openai requests pyautogui
```

### APIs Used

1. **OpenWeatherMap API**
   - Sign up at [OpenWeatherMap](https://openweathermap.org/) to get your API key.
   - Replace the placeholder `api_key` in the `get_weather` function.

2. **NewsAPI**
   - Sign up at [NewsAPI](https://newsapi.org/) to get your API key.
   - Replace the placeholder `api_key` in the `get_news` function.

3. **OpenAI API**
   - Sign up at [OpenAI](https://openai.com/) to get your API key.
   - Replace the placeholder `openai.api_key` with your API key.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/ChiragPatankar/jarvis-virtual-assistant.git
   ```

2. Navigate to the project directory:
   ```bash
   cd jarvis-virtual-assistant
   ```

3. Run the script:
   ```bash
   python jarvis.py
   ```

---

## Usage

- Launch the script and speak your commands.
- Example commands:
  - "What's the weather in New York?"
  - "Get the news."
  - "Convert 100 USD to INR."
  - "Open YouTube."
  - "Search YouTube for Python tutorials."
  - "Ask ChatGPT, what is AI?"

---

## Contributing

Feel free to fork this repository and contribute by submitting pull requests. Suggestions and improvements are always welcome!

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Author

**ChiragPatankar**
