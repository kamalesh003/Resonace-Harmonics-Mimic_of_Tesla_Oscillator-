# Resonace-Harmonics-Mimic_of_Tesla_Oscillator-

Resonant Harmonics is a Python-based project inspired by Nikola Tesla's mechanical oscillator, designed to capture ambient sound, analyze dominant frequencies, and generate resonant sounds based on that analysis.
It simulates the concept of resonance digitally, offering insights into the principles of mechanical vibration and potential applications in various domains.

**Features:**

**Sound Capture:** Utilizes the microphone input to capture ambient sound in real-time.

**Frequency Analysis:** Analyzes the captured sound to identify dominant frequencies using signal processing techniques.

**Resonant Sound Generation:** Generates resonant sounds based on the analyzed frequencies, simulating the phenomenon of mechanical resonance.

**Configurability:** Allows for customization of recording duration, sampling rate, and amplitude of generated sounds via configuration files.

To start, run, and enjoy your project, follow these steps:

**Step 1: Set Up the Environment**

Install Dependencies:Ensure you have Python installed (preferably Python 3.6 or higher).

Navigate to the project directory in your terminal.

Install the required dependencies using the requirements.txt file:


pip install -r requirements.txt

**Step 2: Run the Main Script**

Running the Project: Execute the main script to start capturing, analyzing, and generating resonant sound:


python main.py

**Step 3: Test the Project**

Run Unit Tests:It's a good practice to run unit tests to ensure everything is working correctly. Run the tests using:


python -m unittest discover -s tests
