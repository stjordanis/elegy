import elegy
import haiku as hk
from haiku.testing import transform_and_run
import jax.numpy as jnp


# import debugpy

# print("Waiting for debugger...")
# debugpy.listen(5679)
# debugpy.wait_for_client()


@transform_and_run
def test_basic():

    accuracy = elegy.metrics.CategoricalAccuracy()

    result = accuracy(
        y_true=jnp.array([[0, 0, 1], [0, 1, 0]]),
        y_pred=jnp.array([[0.1, 0.9, 0.8], [0.05, 0.95, 0]]),
    )
    assert result == 0.5  # 1/2

    result = accuracy(
        y_true=jnp.array([[0, 1, 0], [0, 1, 0]]),
        y_pred=jnp.array([[0.1, 0.9, 0.8], [0.05, 0.95, 0]]),
    )
    assert result == 0.75  # 3/4
