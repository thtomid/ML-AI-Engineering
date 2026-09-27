import time
import torch
import matplotlib.pyplot as plt
from IPython.display import clear_output


def _to_numpy(x):
    """Convert a tensor or array-like object to NumPy safely."""
    if isinstance(x, torch.Tensor):
        return x.detach().cpu().numpy()
    return x


def plot_points(x, y, *, normalized=False, title=None, label="Actual Data"):
    """
    Plot raw data points.

    Args:
        x: Input values (tensor or array-like).
        y: Target values (tensor or array-like).
        normalized: Whether the data is normalized.
        title: Optional custom title.
        label: Legend label for the points.
    """
    x_np = _to_numpy(x)
    y_np = _to_numpy(y)

    plt.figure(figsize=(8, 6))
    plt.scatter(x_np, y_np, color="orange", label=label)

    if normalized:
        plt.xlabel("Normalized Distance")
        plt.ylabel("Normalized Time")
        plt.title(title or "Normalized Delivery Data")
    else:
        plt.xlabel("Distance (miles)")
        plt.ylabel("Time (minutes)")
        plt.title(title or "Delivery Data")

    plt.legend()
    plt.grid(True)
    plt.show()


def plot_fit(
    x,
    y,
    predictions,
    *,
    normalized=False,
    title=None,
    data_label="Actual Data",
    pred_label="Model Predictions",
):
    """
    Plot actual data and model predictions together.

    Args:
        x: Input values (tensor or array-like).
        y: True target values (tensor or array-like).
        predictions: Model predictions (tensor or array-like).
        normalized: Whether the values are normalized.
        title: Optional custom title.
        data_label: Legend label for actual data.
        pred_label: Legend label for predictions.
    """
    x_np = _to_numpy(x).reshape(-1)
    y_np = _to_numpy(y).reshape(-1)
    pred_np = _to_numpy(predictions).reshape(-1)

    sorted_idx = x_np.argsort()

    plt.figure(figsize=(8, 6))
    plt.scatter(x_np, y_np, color="orange", label=data_label)
    plt.plot(x_np[sorted_idx], pred_np[sorted_idx], color="green", label=pred_label)

    if normalized:
        plt.xlabel("Normalized Distance")
        plt.ylabel("Normalized Time")
        plt.title(title or "Normalized Model Fit")
    else:
        plt.xlabel("Distance (miles)")
        plt.ylabel("Time (minutes)")
        plt.title(title or "Model Fit vs Actual Data")

    plt.legend()
    plt.grid(True)
    plt.show()


def plot_training_progress(epoch, model, x, y, *, pause=0.05):
    """
    Live plot of model predictions during training on normalized data.

    Args:
        epoch: Current epoch number (0-indexed).
        model: Trained or training PyTorch model.
        x: Normalized input tensor.
        y: Normalized target tensor.
        pause: Small pause to make live plotting readable in notebooks.
    """
    clear_output(wait=True)

    with torch.no_grad():
        predictions = model(x)

    plot_fit(
        x,
        y,
        predictions,
        normalized=True,
        title=f"Epoch: {epoch + 1} | Normalized Training Progress",
        data_label="Actual Normalized Data",
        pred_label="Model Predictions",
    )

    time.sleep(pause)
