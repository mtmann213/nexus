"""
Hyperparameter configuration for the adaptive neural equalizer.
"""

import os
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Hyperparameters:
    """
    Training and inference hyperparameters for the ANE system.
    
    Attributes:
        learning_rate: Base learning rate for optimization
        batch_size: Mini-batch size for training
        num_epochs: Total training epochs
        patience: Early stopping patience
        lms_step_size: LMS algorithm step size (μ)
        rls_forgetting_factor: RLS forgetting factor (λ)
        regularization_lambda: L2 regularization strength
    """
    
    # Training hyperparameters
    learning_rate: float = 0.001
    batch_size: int = 64
    num_epochs: int = 100
    patience: int = 10
    
    # Model architecture
    hidden_size: int = 128
    num_subcarriers: int = 64
    cnn_filters: tuple = (64, 128, 256)
    cnn_kernel_sizes: tuple = (5, 7, 9)
    lstm_units: tuple = (128, 64)
    attention_heads: int = 8
    
    # Adaptation algorithm parameters
    lms_step_size: float = 0.005
    rls_forgetting_factor: float = 0.99
    regularization_lambda: float = 1e-4
    
    # Convergence criteria
    mse_threshold: float = 0.01
    gradient_threshold: float = 1e-5
    min_batch_size: int = 32
    
    # Optimization settings
    optimizer_momentum: float = 0.9
    weight_decay: float = 1e-5
    clip_grad_norm: Optional[float] = 1.0
    
    # Data augmentation
    augmentation_prob: float = 0.3
    noise_std: float = 0.01
    
    def __post_init__(self):
        """Validate hyperparameters."""
        assert self.learning_rate > 0, "Learning rate must be positive"
        assert self.batch_size > 0, "Batch size must be positive"
        assert 0 < self.lms_step_size < 1, "LMS step size must be in (0, 1)"
        assert 0 < self.rls_forgetting_factor < 1, "RLS forgetting factor must be in (0, 1)"
        assert len(self.cnn_filters) == len(self.cnn_kernel_sizes), \
            "CNN filters and kernel sizes must have same length"
        assert len(self.lstm_units) == 2, "LSTM units must be a tuple of 2 values"


def get_hyperparameters(mode: str = 'training') -> Hyperparameters:
    """
    Get hyperparameters for the specified mode.
    
    Args:
        mode: 'training' or 'inference'
        
    Returns:
        Configured Hyperparameters instance
    """
    if mode == 'inference':
        return Hyperparameters(
            learning_rate=0.0,  # Disable gradient updates
            batch_size=1,       # Single sample inference
            num_epochs=0,       # No training
            patience=0,
            lms_step_size=0.005,
            rls_forgetting_factor=0.99,
            regularization_lambda=0.0,
            mse_threshold=0.01,
            gradient_threshold=1e-5,
            min_batch_size=1,
            augmentation_prob=0.0,
            noise_std=0.0
        )
    return Hyperparameters()
