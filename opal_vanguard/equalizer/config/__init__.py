"""
Configuration file for Adaptive Neural Equalizer (5G Signals)
Production-ready settings with proper error handling
"""

import os
from dataclasses import dataclass, field
from typing import Optional, Dict, Any
from pathlib import Path


@dataclass
class ModelConfig:
    """Neural Network Architecture Configuration"""
    
    # CNN-LSTM Hybrid Model Settings
    cnn_filters: int = 64
    cnn_kernel_size: tuple = (3, 3)
    lstm_units: int = 128
    attention_heads: int = 4
    attention_dim: int = 64
    
    # Model Depth
    cnn_layers: int = 3
    lstm_layers: int = 2
    
    # Dropout and Regularization
    dropout_rate: float = 0.3
    l2_regularization: float = 1e-4
    
    # Optimization
    learning_rate: float = 0.001
    weight_decay: float = 1e-5
    
    # Training Settings
    batch_size: int = 64
    epochs: int = 100
    patience: int = 10
    validation_split: float = 0.2
    
    # Hardware Acceleration
    use_gpu: bool = True
    gpu_memory_fraction: float = 0.85


@dataclass
class AdaptationConfig:
    """LMS/RLS Hybrid Algorithm Configuration"""
    
    # LMS Parameters
    lms_step_size: float = 0.01
    lms_normalization: bool = True
    
    # RLS Parameters
    rls_forgetting_factor: float = 0.9995
    rls_initial_inverse_correlation: Optional[Dict[str, Any]] = None
    
    # Hybrid Switching
    hybrid_switch_threshold: float = 0.001
    adaptation_window: int = 100
    
    # Convergence Criteria
    convergence_threshold: float = 1e-6
    max_iterations: int = 500


@dataclass
class PreprocessingConfig:
    """Signal Processing Pipeline Configuration"""
    
    # ADC Sampling
    sample_rate_mhz: float = 30.0
    adc_bits: int = 12
    
    # FFT Settings
    fft_size: int = 256
    window_type: str = "hann"
    overlap_factor: float = 0.75
    
    # Feature Extraction
    feature_window_length: int = 256
    feature_extraction_method: str = "spectral"  # spectral, temporal, hybrid
    
    # Normalization
    normalization_method: str = "zscore"  # zscore, minmax, robust


@dataclass
class EvaluationConfig:
    """Evaluation Metrics Configuration"""
    
    # BER Testing
    ber_target: float = 1e-3
    ber_tolerance: float = 1e-2
    
    # MSE Calculation
    mse_window_size: int = 64
    
    # SINR Measurement
    sinr_measurement_interval: int = 100
    
    # Reporting
    report_frequency: int = 50
    save_results: bool = True
    result_directory: str = "results"


@dataclass
class DataConfig:
    """Data Generation and Management Configuration"""
    
    # Synthetic Channel Generator
    channel_type: str = "rayleigh"  # rayleigh, rician, tdl
    max_delay_tap: int = 10
    delay_spread_us: float = 5.0
    
    # Training Data
    training_samples: int = 100000
    validation_samples: int = 20000
    test_samples: int = 20000
    
    # Signal Parameters
    modulation_scheme: str = "qam64"  # qpsk, qam16, qam64, qam256
    symbol_rate_ms: float = 30.0
    esm_ratio: float = 0.1  # ESM/E ratio
    
    # Data Management
    data_cache_size: int = 10000
    shuffle_data: bool = True


@dataclass
class TrainingConfig:
    """Training Pipeline Configuration"""
    
    # Early Stopping
    early_stopping_monitor: str = "val_loss"
    early_stopping_patience: int = 10
    
    # Checkpointing
    checkpoint_path: str = "checkpoints"
    save_best_only: bool = True
    
    # Callbacks
    enable_tensorboard: bool = True
    tensorboard_log_dir: str = "logs/tensorboard"
    
    # Mixed Precision
    use_mixed_precision: bool = True


@dataclass
class ProductionConfig:
    """Production Deployment Configuration"""
    
    # Inference Settings
    inference_batch_size: int = 32
    inference_latency_ms: float = 10.0
    
    # Monitoring
    health_check_interval: int = 60
    metrics_collection_interval: int = 10
    
    # Error Handling
    max_retries: int = 3
    retry_delay_seconds: float = 1.0
    circuit_breaker_threshold: float = 0.5
    
    # Logging
    log_level: str = "INFO"
    log_file: Optional[str] = None


class ConfigManager:
    """Centralized Configuration Manager with Error Handling"""
    
    def __init__(self):
        self.model_config = ModelConfig()
        self.adaptation_config = AdaptationConfig()
        self.preprocessing_config = PreprocessingConfig()
        self.evaluation_config = EvaluationConfig()
        self.data_config = DataConfig()
        self.training_config = TrainingConfig()
        self.production_config = ProductionConfig()
        
        self._validate_all_configs()
    
    def _validate_all_configs(self):
        """Validate all configuration parameters"""
        try:
            # Model validation
            assert 0 < self.model_config.cnn_filters <= 512, "CNN filters must be between 1 and 512"
            assert 0 < self.model_config.lstm_units <= 512, "LSTM units must be between 1 and 512"
            assert 0.0 < self.model_config.dropout_rate <= 0.9, "Dropout rate must be between 0 and 0.9"
            
            # Adaptation validation
            assert 0.0 < self.adaptation_config.lms_step_size <= 0.1, "LMS step size out of range"
            assert 0.5 < self.adaptation_config.rls_forgetting_factor <= 1.0, "RLS forgetting factor out of range"
            
            # Preprocessing validation
            assert self.preprocessing_config.fft_size > 0 and (self.preprocessing_config.fft_size & (self.preprocessing_config.fft_size - 1)) == 0, \
                "FFT size must be a power of 2"
            
            # Data validation
            assert self.data_config.training_samples > 0, "Training samples must be positive"
            assert self.data_config.modulation_scheme in ["qpsk", "qam16", "qam64", "qam256"], \
                "Invalid modulation scheme"
            
            # Training validation
            assert self.training_config.batch_size > 0, "Batch size must be positive"
            
            print("✓ All configuration validations passed")
            
        except AssertionError as e:
            raise ValueError(f"Configuration Error: {str(e)}")
    
    def update(self, **kwargs):
        """Update configuration with new values"""
        for attr_name, value in kwargs.items():
            if hasattr(self, attr_name):
                setattr(self, attr_name, value)
            else:
                raise AttributeError(f"Invalid config attribute: {attr_name}")
    
    def to_dict(self) -> Dict[str, Any]:
        """Export all configurations as dictionary"""
        return {
            "model": vars(self.model_config),
            "adaptation": vars(self.adaptation_config),
            "preprocessing": vars(self.preprocessing_config),
            "evaluation": vars(self.evaluation_config),
            "data": vars(self.data_config),
            "training": vars(self.training_config),
            "production": vars(self.production_config)
        }


# Global configuration instance
config = ConfigManager()
