import time
from src.capture.record import record_sound
from src.analyze.analyze import analyze_sound
from src.generate.generate import generate_sound
import yaml

def main():
    with open('config/settings.yaml', 'r') as file:
        config = yaml.safe_load(file)
    
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
