#正解率の計測
import torch
from sklearn.metrics import accuracy_score

class SLPNet(torch.nn.Module):
    def __init__(self, input_size, output_size):
        super().__init__()
        self.fc = torch.nn.Linear(input_size, output_size, bias=False)
        torch.nn.init.xavier_normal_(self.fc.weight, gain=1)

    def forward(self, x):
        x = self.fc(x)
        return x

def cal_accuracy(y, pred):
    return accuracy_score(y, pred)

def main():
    train_x = torch.load('train_x.pt')
    train_y = torch.load('train_y.pt')

    test_x = torch.load('test_x.pt')
    test_y = torch.load('test_y.pt')

    model = SLPNet(300, 4)
    model.load_state_dict(torch.load('model.pth'))


    model.eval()
    with torch.no_grad():
        pred = torch.argmax(model(train_x), dim=-1)
    
    print(f'正解率: {cal_accuracy(train_y, pred):.4f}')

    with torch.no_grad():
        pred = torch.argmax(model(test_x), dim=-1)

    print(f'正解率: {cal_accuracy(test_y, pred):.4f}')

if __name__ == '__main__':
    main()
