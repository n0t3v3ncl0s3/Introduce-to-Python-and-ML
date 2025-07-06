import math

class ActivationFunction:
    def __init__(self):
        pass

    def forward(self, x):
        """
        TODO: Ghi đè (override) phương thức này ở lớp con để tính đầu ra của hàm kích hoạt.
        :param x: một số thực (float)
        :return: một số thực (float)
        """
        return x


class Sigmoid(ActivationFunction):
    def forward(self, x):
        """
        TODO: Hiện thực hàm sigmoid: sigmoid(x) = 1 / (1 + exp(-x))
        """
        return 1 / (1 + math.exp(-x))
        pass


class ReLU(ActivationFunction):
    def forward(self, x):
        """
        TODO: Hiện thực hàm ReLU: relu(x) = max(0, x)
        """
        return max(0, x)
        pass


class Tanh(ActivationFunction):
    def forward(self, x):
        """
        TODO: Hiện thực hàm tanh: tanh(x) = (exp(x) - exp(-x)) / (exp(x) + exp(-x))
        """
        return (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))
        pass