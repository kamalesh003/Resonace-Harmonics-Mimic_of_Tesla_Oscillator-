import time
import yaml
from src.capture.record import record_sound
from src.analyze.analyze import analyze_sound
from src.generate.generate import generate_sound
import numpy as np

def load_config(config_path='config/settings.yaml'):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def main():
    config = load_config()
    
    rate = config['recording']['rate']
    duration = config['recording']['duration']
    amplitude = config['sound']['amplitude']
    
    while True:
        # Step 1: Record sound
        signal = record_sound(duration, rate)
        
        # Step 2: Analyze sound to find dominant frequency
        dominant_frequency = analyze_sound(signal, rate)
        print(f"Dominant Frequency: {dominant_frequency} Hz")
        
        # Step 3: Generate resonant sound
        generate_sound(dominant_frequency, duration, rate, amplitude)
        
        # Small delay to avoid overwhelming the system
        time.sleep(0.5)

if __name__ == "__main__":
    main()
