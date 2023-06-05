#確率的勾配降下法による学習
from torch import nn, optim
import torch
from torch.utils.data import Dataset, DataLoader

class NewsDataset(Dataset):
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def __len__(self): #len(Datasetのサブクラス)で返す値を指定
        return len(self.y)

    def __getitem__(self, idx): #Datasetのサブクラス[idx]で返す値を指定
        return [self.X[idx], self.y[idx]]

class SLPNet(nn.Module):
    def __init__(self, input_size, output_size):
        super().__init__()
        self.fc = nn.Linear(input_size, output_size, bias=False)
        nn.init.xavier_normal_(self.fc.weight, gain=1)

    def forward(self, x):
        x = self.fc(x)
        return x

def train(X, y, model, criterion, optimizer):
    model.train()
    optimizer.zero_grad()
    y_pred = model(X)
    loss = criterion(y_pred, y)
    loss.backward()
    optimizer.step()
    return loss, y_pred

def main():
    train_x = torch.load('train_x.pt')
    train_y = torch.load('train_y.pt')

    dataset = NewsDataset(train_x, train_y)
    dataloader = DataLoader(dataset, batch_size=1, shuffle=True)

    model = SLPNet(300, 4)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=1e-1)

    for epoch in range(10):
        for xx, yy in dataloader:
            loss, y_pred = train(xx, yy, model, criterion, optimizer)
        print(f'epoch: {epoch+1}, loss: {loss:.4f}')
    
    torch.save(model.state_dict(), 'model.pth')

if __name__ == '__main__':
    main()