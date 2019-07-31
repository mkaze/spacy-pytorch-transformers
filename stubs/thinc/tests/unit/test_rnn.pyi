# Stubs for thinc.tests.unit.test_rnn (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ...neural._classes.rnn import LSTM
from ...neural.ops import NumpyOps
from ...neural.util import minibatch

def test_square_sequences() -> None: ...
def test_LSTM_init() -> None: ...
def test_LSTM_fwd_bwd_shapes() -> None: ...
def test_LSTM_learns() -> None: ...
def test_benchmark_RNN_fwd() -> None: ...