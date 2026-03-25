"""
Model architecture configuration for the adaptive neural equalizer.
"""

from dataclasses import dataclass


@dataclass
class ModelConfig:
    """
    Architecture configuration for the CNN-LSTM-Attention model.
    
    Attributes:
        input_channels: Number of input feature channels (I/Q real/imag)
        num_subcarriers: Number of OFDM subcarriers
        hidden_size: Hidden dimension for LSTM layers
        cnn_filters: Tuple of filter counts per CNN stage
        cnn_kernel_sizes: Tuple of kernel sizes per CNN stage
        lstm_units: Tuple of LSTM unit counts (bidirectional)
        attention_heads: Number of attention heads
        dropout_rate: Dropout probability
        use_batch_norm: Whether to use batch normalization
    """
    
    # Input/output dimensions
    input_channels: int = 4  # I, Q, magnitude, phase
    num_subcarriers: int = 64
    
    # CNN backbone configuration
    cnn_filters: tuple = (64, 128, 256)
    cnn_kernel_sizes: tuple = (5, 7, 9)
    cnn_strides: tuple = (2, 2, 2)
    
    # LSTM temporal modeling
    lstm_units: tuple = (128, 64)
    lstm_dropout: float = 0.3
    
    # Attention mechanism
    attention_heads: int = 8
    attention_dropout: float = 0.2
    
    # Normalization and activation
    use_batch_norm: bool = True
    batch_norm_momentum: float = 0.1
    leaky_relu_alpha: float = 0.1
    
    # Output configuration
    output_activation: str = 'tanh'  # tanh for bounded coefficients
    
    def get_total_filters(self) -> int:
        """Calculate total number of CNN filters."""
        return sum(self.cnn_filters)
    
    def get_lstm_output_size(self) -> int:
        """Calculate final LSTM output dimension."""
        return self.lstm_units[-1] * 2  # Bidirectional doubles the units
    
    def __repr__(self) -> str:
        return (
            f"ModelConfig("
            f"input_channels={self.input_channels}, "
            f"num_subcarriers={self.num_subcarriers}, "
            f"cnn_filters={self.cnn_filters}, "
            f"lstm_units={self.lstm_units})"
        )
