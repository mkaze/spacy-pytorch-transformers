# Stubs for torch.autograd._functions.utils (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def maybe_view(tensor: Any, size: Any, check_same_size: bool = ...): ...
def maybe_unexpand(tensor: Any, old_size: Any, check_same_size: bool = ...): ...
def prepare_onnx_paddings(dim: Any, pad: Any): ...
def check_onnx_broadcast(dims1: Any, dims2: Any): ...