#!/usr/bin/env python3
"""
Wavelength Calculator
Calculates wavelength given frequency.
Formula: λ = c / f
Where:
  λ = wavelength (meters)
  c = speed of light (~299,792,458 m/s)
  f = frequency (Hz)
"""

# Speed of light in vacuum (meters per second)
SPEED_OF_LIGHT = 299_792_458

def calculate_wavelength(frequency_hz):
    """
    Calculate wavelength from frequency.
    
    Args:
        frequency_hz: Frequency in Hertz (Hz)
    
    Returns:
        Wavelength in meters
    """
    if frequency_hz <= 0:
        raise ValueError("Frequency must be positive")
    
    wavelength = SPEED_OF_LIGHT / frequency_hz
    return wavelength

def main():
    """Main function to calculate wavelength."""
    try:
        # Get user input
        freq_input = input("Enter frequency in Hz: ")
        frequency = float(freq_input)
        
        # Calculate wavelength
        wavelength = calculate_wavelength(frequency)
        
        # Display result with appropriate formatting
        print(f"\nFrequency: {frequency:.2e} Hz")
        print(f"Wavelength: {wavelength:.6f} meters")
        
        # Also show in more convenient units if applicable
        if wavelength < 1:
            print(f"Wavelength: {wavelength * 1000:.3f} millimeters")
        elif wavelength > 1000:
            print(f"Wavelength: {wavelength / 1000:.3f} kilometers")
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()