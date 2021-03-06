import torch.nn as nn
import torch.nn.functional as F


class FLModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(165, 50)
        self.fc5 = nn.Linear(50, 2)

    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc5(x)
        output = F.log_softmax(x, dim=1)

        return output
