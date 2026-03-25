"""
WaveformEngine.py - Professional RF Signal Generation Library for TechniqueMaker

This module provides 15 advanced waveform templates for electronic warfare,
SIGINT operations, and reactive interdiction systems. Designed for Ettus USRP platforms.

Author: Opal Vanguard Engineering Team
License: Proprietary - For Authorized Use Only
"""

import numpy as np
from typing import Tuple, Optional, Callable, Dict, List, Any
from dataclasses import dataclass
from enum import Enum
import warnings
import time


class WaveformType(Enum):
    """Enumeration of supported waveform types."""
    LFM_CHIRP = "LFM_CHIRP"  # Linear Frequency Modulated Chirp
    OFDM_NOISE = "OFDM_NOISE"  # Orthogonal Frequency Division Multiplexing Noise
    DIFFERENTIAL_COMB = "DIFFERENTIAL_COMB"  # Differential Comb Pattern
    STEPPED_FREQ = "STEPPED_FREQ"  # Stepped Frequency Waveform
    PHASE_CODED = "PHASE_CODED"  # BPSK/Barker Code Phase Coded
    FREQUENCY_HOPPING = "FREQUENCY_HOPPING"  # FHSS Pattern Generator
    CONTINUOUS_WAVE = "CONTINUOUS_WAVE"  # Pure CW Tone
    NOISE_BURST = "NOISE_BURST"  # Random Noise Burst
    LOG_CHIRP = "LOG_CHIRP"  # Logarithmic Frequency Chirp
    EXPONENTIAL_CHIRP = "EXPONENTIAL_CHIRP"  # Exponential Sweep
    COMPOSITE_PULSE = "COMPOSITE_PULSE"  # Multi-Pulse Train
    FREQUENCY_MODULATED = "FREQUENCY_MODULATED"  # FM Modulated Carrier
    PHASE_REVERSED = "PHASE_REVERSED"  # Phase Reversal Keying
    QUADRATURE_AMPLITUDE = "QUADRATURE_AMPLITUDE"  # QAM Constellation Based
    HYBRID_WAVEFORM = "HYBRID_WAVEFORM"  # Multi-Mode Composite


@dataclass
class WaveformParameters:
    """Container for waveform generation parameters."""
    sample_rate: float
    duration: float
    carrier_freq: float
    bandwidth: float
    amplitude: float = 1.0
    phase_offset: float = 0.0
    snr_db: Optional[float] = None


@dataclass
class GeneratedWaveform:
    """Container for generated waveform data and metadata."""
    signal: np.ndarray
    params: WaveformParameters
    waveform_type: WaveformType
    timestamp: float
    metadata: Dict[str, Any]


class WaveformEngine:
    """
    Professional RF Signal Generation Engine
    
    This engine provides 15 distinct waveform templates optimized for:
    - Radar cross-section analysis
    - Electronic countermeasures (ECM)
    - SIGINT signal characterization
    - Reactive jamming operations
    - Channel probing and mapping
    """
    
    def __init__(self, default_sample_rate: float = 10e6):
        """
        Initialize the waveform engine.
        
        Args:
            default_sample_rate: Default sampling rate in Hz (default: 10 MHz)
        """
        self.default_sample_rate = default_sample_rate
        self._generated_signals: List[GeneratedWaveform] = []
        self._seed: int = int(np.random.randint(0, 2**32))
        
    def set_seed(self, seed: int):
        """Set random seed for reproducible signal generation."""
        self._seed = seed
        np.random.seed(seed)
        
    def generate_waveform(
        self,
        waveform_type: WaveformType,
        params: WaveformParameters,
        custom_params: Optional[Dict] = None
    ) -> GeneratedWaveform:
        """
        Generate a specific waveform type with given parameters.
        
        Args:
            waveform_type: Type of waveform to generate
            params: Waveform generation parameters
            custom_params: Additional customization dictionary
            
        Returns:
            GeneratedWaveform object containing signal and metadata
        """
        np.random.seed(self._seed)
        
        t = np.linspace(0, params.duration, 
                       int(params.sample_rate * params.duration), 
                       endpoint=False)
        
        signal = self._generate_by_type(waveform_type, t, params, custom_params)
        
        # Add noise if SNR specified
        if params.snr_db is not None:
            signal = self._add_noise(signal, params.snr_db)
        
        # Apply phase offset
        signal = np.exp(1j * params.phase_offset) * signal
        
        # Scale amplitude
        signal = params.amplitude * signal / (np.max(np.abs(signal)) + 1e-12)
        
        generated = GeneratedWaveform(
            signal=signal,
            params=params,
            waveform_type=waveform_type,
            timestamp=time.time(),
            metadata={
                'duration': params.duration,
                'bandwidth': params.bandwidth,
                'carrier_freq': params.carrier_freq,
                'custom_params': custom_params or {}
            }
        )
        
        self._generated_signals.append(generated)
        return generated
    
    def _add_noise(self, signal: np.ndarray, snr_db: float) -> np.ndarray:
        """Add controlled Gaussian noise at specified SNR."""
        signal_power = np.mean(np.abs(signal) ** 2)
        noise_power = signal_power / (10 ** (snr_db / 10))
        noise = np.sqrt(noise_power / 2) * (np.random.randn(len(signal)) + 
                                              1j * np.random.randn(len(signal)))
        return signal + noise
    
    def _lfm_chirp(self, t: np.ndarray, params: WaveformParameters) -> np.ndarray:
        """Generate Linear Frequency Modulated Chirp - Wideband sweep."""
        f_start = params.carrier_freq - params.bandwidth / 2
        f_end = params.carrier_freq + params.bandwidth / 2
        
        k = (f_end - f_start) / params.duration  # Chirp rate
        
        phi = 2 * np.pi * (f_start * t + 0.5 * k * t ** 2)
        return np.exp(1j * phi)
    
    def _ofdm_noise(self, t: np.ndarray, params: WaveformParameters) -> np.ndarray:
        """Generate OFDM-like noise with frequency diversity."""
        n_subcarriers = int(params.bandwidth / (1000))  # ~1kHz subcarrier spacing
        
        # Generate random phases for each subcarrier
        frequencies = np.linspace(
            params.carrier_freq - params.bandwidth/2,
            params.carrier_freq + params.bandwidth/2,
            n_subcarriers
        )
        
        signal = np.zeros(len(t), dtype=complex)
        for freq in frequencies:
            phase = 2 * np.pi * np.random.rand()
            signal += np.exp(1j * (2 * np.pi * freq * t + phase))
        
        return signal / np.sqrt(n_subcarriers)
    
    def _differential_comb(self, t: np.ndarray, params: WaveformParameters) -> np.ndarray:
        """Generate differential comb pattern for spectral analysis."""
        n_teeth = int(params.bandwidth / 5000)  # ~5kHz tooth spacing
        
        signal = np.zeros(len(t), dtype=complex)
        center_freq = params.carrier_freq
        
        for i in range(n_teeth):
            offset = (i - n_teeth // 2) * 5000  # Tooth spacing
            tooth_width = 1000  # Each tooth is ~1kHz wide
            
            if np.abs(offset) < params.bandwidth / 2:
                freq_component = center_freq + offset
                
                # Create tooth shape (raised cosine window)
                tooth_duration = int(tooth_width * params.duration / params.bandwidth)
                for j in range(len(t)):
                    if np.abs((j - len(t)//2) * params.duration / len(t)) < tooth_width / 2:
                        envelope = 0.5 * (1 + np.cos(2 * np.pi * 
                                    ((j - len(t)//2) * params.duration / len(t)) / tooth_duration))
                        signal[j] += envelope * np.exp(1j * 2 * np.pi * freq_component * t[j])
        
        return signal
    
    def _stepped_freq(self, t: np.ndarray, params: WaveformParameters) -> np.ndarray:
        """Generate stepped frequency waveform for high-resolution range."""
        n_steps = int(params.bandwidth / 10e3)  # ~10kHz steps
        
        signal = np.zeros(len(t), dtype=complex)
        step_duration = params.duration / n_steps
        
        for i in range(n_steps):
            freq_offset = (i - n_steps//2) * 10e3
            current_freq = params.carrier_freq + freq_offset
            
            # Apply to appropriate time segment
            start_idx = int(i * step_duration * params.sample_rate)
            end_idx = int((i + 1) * step_duration * params.sample_rate)
            signal[start_idx:end_idx] += np.exp(1j * 2 * np.pi * current_freq * 
                                               t[start_idx:end_idx])
        
        return signal
    
    def _phase_coded(self, t: np.ndarray, params: WaveformParameters) -> np.ndarray:
        """Generate phase-coded waveform using Barker codes."""
        barker_codes = [
            [1, 1, 1, 1, 1],           # Barker-5
            [1, 1, 1, -1, -1],         # Barker-7
            [1, 1, 1, -1, -1, 1, -1],  # Barker-13
        ]
        
        code = barker_codes[min(len(barker_codes)-1, int(params.bandwidth/1e6))]
        n_replications = max(1, len(t) // (len(code) * params.sample_rate / params.bandwidth))
        
        full_code = np.repeat(code, int(params.sample_rate / params.bandwidth))[:len(t)]
        
        signal = np.ones(len(t), dtype=complex)
        for i in range(len(full_code)):
            if full_code[i] < 0:
                signal[i] = -1
        
        carrier = np.exp(1j * 2 * np.pi * params.carrier_freq * t)
        return signal * carrier
    
    def _frequency_hopping(self, t: np.ndarray, params: WaveformParameters) -> np.ndarray:
        """Generate frequency-hopping spread spectrum pattern."""
        n_hops = int(params.duration * params.bandwidth / 1000)  # Hop rate ~1kHz
        
        signal = np.zeros(len(t), dtype=complex)
        hop_duration = t[-1] / n_hops if n_hops > 0 else t[-1]
        
for i in range(min(n_hops, len(t))):
            hop_freq_offset = (np.random.randint(0, int(2*params.bandwidth//500)) - 
                              int(params.bandwidth/500)) * 500
            
            start_idx = int(i * hop_duration * params.sample_rate)
            end_idx = min(start_idx + int(hop_duration * params.sample_rate), len(t))
            
            current_freq = params.carrier_freq + hop_freq_offset
            signal[start_idx:end_idx] = np.exp(1j * 2 * np.pi * 
                                             current_freq * t[start_idx:end_idx])
        
        return signal
    
    def _continuous_wave(self, t: np.ndarray, params: WaveformParameters) -> np.ndarray:
        """Generate pure continuous wave tone."""
        return np.exp(1j * 2 * np.pi * params.carrier_freq * t)
    
    def _noise_burst(self, t: np.ndarray, params: WaveformParameters) -> np.ndarray:
        """Generate random noise burst with controlled bandwidth."""
        noise = np.random.randn(len(t)) + 1j * np.random.randn(len(t))
        
        # Apply bandpass filter in frequency domain
        fft_signal = np.fft.fft(noise)
        freqs = np.fft.fftfreq(len(t), 1/params.sample_rate)
        
        mask = (np.abs(freqs - params.carrier_freq) < params.bandwidth / 2) | \
               (np.abs(freqs + params.carrier_freq) < params.bandwidth / 2)
        fft_signal[~mask] = 0
        
        return np.fft.ifft(fft_signal)
    
    def _log_chirp(self, t: np.ndarray, params: WaveformParameters) -> np.ndarray:
        """Generate logarithmic frequency chirp."""
        f_start = max(params.carrier_freq * 0.5, 
                     params.carrier_freq - params.bandwidth/2)
        f_end = params.carrier_freq * 1.5
        
        # Logarithmic sweep: f(t) = f_start * (f_end/f_start)^(t/T)
        def instantaneous_freq(t_val):
            return f_start * (f_end / f_start) ** (t_val / params.duration)
        
        phi = 2 * np.pi * f_start * params.duration / np.log(f_end/f_start) * \
              (np.exp(np.log(f_end/f_start) * t / params.duration) - 1)
        return np.exp(1j * phi)
    
    def _exponential_chirp(self, t: np.ndarray, params: WaveformParameters) -> np.ndarray:
        """Generate exponential frequency sweep."""
        f_start = params.carrier_freq - params.bandwidth/2
        f_end = params.carrier_freq + params.bandwidth/2
        
        # Exponential sweep with quadratic phase
        k = (f_end - f_start) / (params.duration ** 2)
        phi = 2 * np.pi * (f_start * t + (1/3) * k * t ** 3)
        return np.exp(1j * phi)
    
    def _composite_pulse(self, t: np.ndarray, params: WaveformParameters) -> np.ndarray:
        """Generate multi-pulse train waveform."""
        n_pulses = int(params.duration / (2e-3))  # ~2ms pulse width
        pulse_width = 1e-3  # 1ms pulses
        
        signal = np.zeros(len(t), dtype=complex)
        
        for i in range(n_pulses):
            pulse_start = i * (params.duration / n_pulses)
            pulse_end = pulse_start + pulse_width
            
            if pulse_start < params.duration:
                mask = (t >= pulse_start) & (t < pulse_end)
                signal[mask] = np.exp(1j * 2 * np.pi * 
                                    params.carrier_freq * t[mask])
        
        return signal
    
    def _frequency_modulated(self, t: np.ndarray, params: WaveformParameters) -> np.ndarray:
        """Generate FM modulated carrier with sinusoidal modulation."""
        mod_freq = 1000  # 1kHz modulation frequency
        mod_index = 0.5 * params.bandwidth / mod_freq
        
        instantaneous_freq = params.carrier_freq + \
                            mod_index * mod_freq * np.sin(2 * np.pi * mod_freq * t)
        
        phi = 2 * np.pi * (params.carrier_freq * t + 
                          (mod_index / (2 * np.pi)) * np.cos(2 * np.pi * mod_freq * t))
        return np.exp(1j * phi)
    
    def _phase_reversed(self, t: np.ndarray, params: WaveformParameters) -> np.ndarray:
        """Generate phase reversal keying waveform."""
        symbol_duration = 0.5e-3  # 0.5ms symbols
        
        signal = np.ones(len(t), dtype=complex)
        current_phase = 0
        
        for i in range(len(t)):
            symbol_idx = int(i * params.duration / (symbol_duration * len(t)))
            
            if symbol_idx % 2 == 1:
                current_phase = np.pi
            
            signal[i] = np.exp(1j * (2 * np.pi * params.carrier_freq * t[i] + 
                                    current_phase))
        
        return signal
    
    def _quadrature_amplitude(self, t: np.ndarray, params: WaveformParameters) -> np.ndarray:
        """Generate QAM-based waveform with constellation shaping."""
        symbol_rate = 10e3  # 10k symbols/sec
        n_symbols = int(params.duration * symbol_rate)
        
        # Generate random QPSK symbols
        symbols = (2 * np.random.randint(0, 2, n_symbols*2).reshape(-1, 2) - 1)
        constellations = symbols[:, 0] + 1j * symbols[:, 1]
        
        signal = np.zeros(len(t), dtype=complex)
        symbol_duration = params.duration / n_symbols
        
        for i in range(min(n_symbols, len(constellations))):
            start_idx = int(i * symbol_duration * params.sample_rate)
            end_idx = min(start_idx + int(symbol_duration * params.sample_rate), len(t))
            
            if start_idx < len(t):
                signal[start_idx:end_idx] += \
                    constellations[i] * np.exp(1j * 2 * np.pi * 
                                              params.carrier_freq * t[start_idx:end_idx])
        
        return signal
    
    def _hybrid_waveform(self, t: np.ndarray, params: WaveformParameters) -> np.ndarray:
        """Generate multi-mode composite waveform combining multiple techniques."""
        # Combine LFM chirp with phase coding and noise overlay
        
        # Component 1: LFM Chirp (50% weight)
        chirp = self._lfm_chirp(t, params) * 0.5
        
        # Component 2: Phase code (30% weight)
        phase_code = np.sign(np.cos(2 * np.pi * 1000 * t))
        phase_component = phase_code * np.exp(1j * 2 * np.pi * params.carrier_freq * t) * 0.3
        
        # Component 3: Noise overlay (20% weight)
        noise_component = self._noise_burst(t, params) * 0.2
        
        return chirp + phase_component + noise_component
    
    def _generate_by_type(
        self, 
        waveform_type: WaveformType,
        t: np.ndarray,
        params: WaveformParameters,
        custom_params: Optional[Dict]
    ) -> np.ndarray:
        """Route to appropriate waveform generator."""
        
        generators = {
            WaveformType.LFM_CHIRP: self._lfm_chirp,
            WaveformType.OFDM_NOISE: self._ofdm_noise,
            WaveformType.DIFFERENTIAL_COMB: self._differential_comb,
            WaveformType.STEPPED_FREQ: self._stepped_freq,
            WaveformType.PHASE_CODED: self._phase_coded,
            WaveformType.FREQUENCY_HOPPING: self._frequency_hopping,
            WaveformType.CONTINUOUS_WAVE: self._continuous_wave,
            WaveformType.NOISE_BURST: self._noise_burst,
            WaveformType.LOG_CHIRP: self._log_chirp,
            WaveformType.EXPONENTIAL_CHIRP: self._exponential_chirp,
            WaveformType.COMPOSITE_PULSE: self._composite_pulse,
            WaveformType.FREQUENCY_MODULATED: self._frequency_modulated,
            WaveformType.PHASE_REVERSED: self._phase_reversed,
            WaveformType.QUADRATURE_AMPLITUDE: self._quadrature_amplitude,
            WaveformType.HYBRID_WAVEFORM: self._hybrid_waveform,
        }
        
        generator = generators.get(waveform_type)
        if not generator:
            raise ValueError(f"Unknown waveform type: {waveform_type}")
        
        return generator(t, params)
    
    def get_available_waveforms(self) -> List[WaveformType]:
        """Return list of all available waveform types."""
        return list(WaveformType)
    
    def generate_preset(
        self, 
        preset_name: str,
        sample_rate: float = None,
        duration: float = 1.0
    ) -> GeneratedWaveform:
        """Generate a predefined tactical waveform based on preset name."""
        
        presets = {
            'radar_probe': {
                'type': WaveformType.LFM_CHIRP,
                'bandwidth': 5e6,
                'duration': 0.1
            },
            'comms_interference': {
                'type': WaveformType.OFDM_NOISE,
                'bandwidth': 2e6,
                'duration': 0.5
            },
            'frequency_scan': {
                'type': WaveformType.STEPPED_FREQ,
                'bandwidth': 10e6,
                'duration': 2.0
            },
            'spoofing_tone': {
                'type': WaveformType.CONTINUOUS_WAVE,
                'bandwidth': 1000,
                'duration': 5.0
            },
            'spread_spectrum': {
                'type': WaveformType.FREQUENCY_HOPPING,
                'bandwidth': 5e6,
                'duration': 1.0
            }
        }
        
        if preset_name not in presets:
            raise ValueError(f"Unknown preset: {preset_name}")
        
        preset = presets[preset_name]
        
        params = WaveformParameters(
            sample_rate=sample_rate or self.default_sample_rate,
            duration=preset['duration'] or duration,
            carrier_freq=2.4e9,  # Default to 2.4 GHz ISM band
            bandwidth=preset['bandwidth'],
            snr_db=None
        )
        
        return self.generate_waveform(preset['type'], params)


def main():
    """Demonstration of waveform engine capabilities."""
    
    print("=" * 60)
    print("TechniqueMaker Waveform Engine - Demonstration")
    print("=" * 60)
    
    engine = WaveformEngine(default_sample_rate=10e6)
    engine.set_seed(42)
    
    # Generate sample waveforms
    presets_to_demo = ['radar_probe', 'comms_interference', 'frequency_scan']
    
    for preset in presets_to_demo:
        try:
            result = engine.generate_preset(preset, duration=0.5)
            print(f"\n{preset.upper()}:")
            print(f"  Type: {result.waveform_type.value}")
            print(f"  Duration: {result.params.duration:.3f}s")
            print(f"  Bandwidth: {result.params.bandwidth/1e6:.1f} MHz")
            print(f"  Signal length: {len(result.signal)} samples")
            print(f"  Peak amplitude: {np.max(np.abs(result.signal)):.4f}")
        except Exception as e:
            print(f"Error generating {preset}: {e}")
    
    print("\n" + "=" * 60)
    print("Available waveform types:")
    for wtype in engine.get_available_waveforms():
        print(f"  - {wtype.value}")
    print("=" * 60)


if __name__ == "__main__":
    main()
