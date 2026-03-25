import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# Phase 9: Neural Equalizer Implementation
# Objective: Equalize 16-QAM signals in a Rayleigh Fading Channel

def generate_rayleigh_data(num_samples=10000, snr_db=20):
    """Generates synthetic 16-QAM symbols affected by Rayleigh fading."""
    # 1. Generate random bits and map to 16-QAM
    bits = np.random.randint(0, 2, (num_samples, 4))
    # Simple mapping for demonstration
    symbols = (2 * bits[:, 0] - 1) + 1j * (2 * bits[:, 1] - 1)
    
    # 2. Channel: Rayleigh Fading (Complex Gaussian)
    h = (np.random.randn(num_samples) + 1j * np.random.randn(num_samples)) / np.sqrt(2)
    received = symbols * h
    
    # 3. Add AWGN
    snr_linear = 10**(snr_db / 10)
    noise_std = np.sqrt(1 / (2 * snr_linear))
    noise = noise_std * (np.random.randn(num_samples) + 1j * np.random.randn(num_samples))
    received_noisy = received + noise
    
    # Preprocess for Neural Net (Separate I/Q components)
    X = np.stack([received_noisy.real, received_noisy.imag], axis=-1)
    y = np.stack([symbols.real, symbols.imag], axis=-1)
    
    return X, y

def build_equalizer_model():
    """Builds a Bidirectional GRU model for adaptive equalization."""
    model = models.Sequential([
        layers.Input(shape=(1, 2)), # Single symbol observation
        layers.Bidirectional(layers.GRU(64, return_sequences=False)),
        layers.Dense(32, activation='relu'),
        layers.Dense(2) # Output I and Q estimates
    ])
    
    model.compile(optimizer='adam', loss='mse')
    return model

def run_simulation():
    print("🚀 Initializing 5G Neural Equalizer Simulation...")
    
    # 1. Data Prep
    X, y = generate_rayleigh_data()
    X = X.reshape(-1, 1, 2) # [Batch, Time, Features]
    
    # 2. Build and Train
    print("🧠 Training Neural Equalizer (Bi-GRU)...")
    model = build_equalizer_model()
    history = model.fit(X, y, epochs=10, batch_size=32, verbose=0, validation_split=0.2)
    
    print("✅ Training Complete.")
    print(f"📉 Final Loss: {history.history['loss'][-1]:.4f}")
    
    # 3. Verification Plot
    plt.figure(figsize=(10, 5))
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title('Neural Equalizer Convergence (MSE)')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)
    plt.savefig('LABS/equalizer_convergence.png')
    print("📊 Convergence plot saved to LABS/equalizer_convergence.png")

if __name__ == "__main__":
    run_simulation()
