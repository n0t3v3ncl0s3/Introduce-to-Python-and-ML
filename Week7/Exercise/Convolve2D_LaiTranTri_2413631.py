import os

import numpy as np
import torch


def convolve2d(
    image: np.ndarray,
    kernel: np.ndarray,
    bias: np.float32 = 0.0,
    stride: int = 1,
    padding: int = 0,
) -> np.ndarray:
    """2D Convolution Operation

    Args:
        image (np.ndarray): Input image array, shape (H, W, C)
        kernel (np.ndarray): Convolution kernel/filter, shape (kH, kW, C)
        bias (np.float32, optional): Bias term to add to the output. Defaults to 0.0.
        stride (int, optional): Stride of the convolution. Defaults to 1.
        padding (int, optional): Padding added to the input image. Defaults to 0.

    Returns:
        np.ndarray: Result of the convolution operation, shape=(h,w).
        Hint: Use np.pad() for padding image.
    """
    H, W, C = image.shape
    kH, kW, kC = kernel.shape
    assert C == kC, "Image and kernel must have the same number of channels"

    padded_image = np.pad(
        image,
        padding,
    )
    out_H = (H - kH + 2 * padding) // stride + 1
    out_W = (W - kW + 2 * padding) // stride + 1
    output = np.zeros((out_H, out_W), dtype=np.float64)

    for r in range(out_H):
        for c in range(out_W):
            output[r, c] = (
                np.sum(
                    kernel
                    * padded_image[
                        r * stride : r * stride + kH,
                        c * stride : c * stride + kW,
                        :,
                    ]
                )
                + bias
            )
    return output


if __name__ == "__main__":
    np.random.seed(42)

    # Manual implementation
    image = np.random.rand(5, 5, 3)
    kernel = np.random.rand(3, 3, 3)
    output1 = convolve2d(image, kernel, bias=1.0, stride=1, padding=0)

    # PyTorch implementation
    conv2d = torch.nn.Conv2d(
        in_channels=3,
        out_channels=1,
        kernel_size=3,
        stride=1,
        padding=0,
        dtype=torch.float64,
    )
    conv2d.weight.data = torch.from_numpy(np.moveaxis(kernel, -1, 0)).unsqueeze(
        0
    )
    conv2d.bias.data.fill_(1.0)
    image_tensor = torch.from_numpy(np.moveaxis(image, -1, 0)).unsqueeze(0)

    output2 = conv2d(image_tensor).detach().numpy()

    # Relative error check
    print("Relative error must be less than 1e-15.")
    print(f"Relative error: {np.sum(output1-output2) / np.sum(output1)}")
