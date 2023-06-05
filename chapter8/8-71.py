import pandas as pd
import torch
from torch import nn

class SLPNet(nn.Module):
    def __init__(self, input_size, output_size):
        super().__init__()
        self.fc = nn.Linear(input_size, output_size, bias=False)
        nn.init.xavier_normal_(self.fc.weight, gain=1)

    def forward(self, x):
        x = self.fc(x)
        return x

#データのx1からx4について単層ニューラルネットワークで計算
X = torch.load('train_x.pt')
X = X[:4]
model = SLPNet(300, 4)
logits = model.forward(X)
preds = torch.softmax(logits, dim=-1)
print(preds)
