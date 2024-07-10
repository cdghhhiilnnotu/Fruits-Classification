from fruits_lib import *

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.neural = nn.Sequential(
            nn.Conv2d(3, 256, kernel_size=(3, 3), stride=(1, 1)),  # Update input channels to 3
            nn.ReLU(),
            nn.Conv2d(256, 512, kernel_size=(3, 3), stride=(1, 1)),
            nn.ReLU(),
            nn.Conv2d(512, 64, kernel_size=(3, 3), stride=(1, 1)),
            nn.ReLU(),
            nn.Conv2d(64, 32, kernel_size=(3, 3), stride=(1, 1)),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(1492992, 3),
        )

    def forward(self, x):
        logits = self.neural(x)
        return logits
    



