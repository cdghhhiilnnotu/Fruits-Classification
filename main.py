from fruits_datapath import *
from fruits_dataset import *
from fruits_lib import *
from fruit_utils import *
from fruits_transform import *
from fruits_nn import *


train_list = FruitDatapath("data", "train")()
test_list = FruitDatapath("data", "test")()

train_dataset = FruitDataset(train_list, fruit_transform=FruitsTransform(), phase="train", fruit_classes=['apple', 'banana', 'orange'])
test_dataset = FruitDataset(test_list, fruit_transform=FruitsTransform(), phase="test", fruit_classes=['apple', 'banana', 'orange'])

# class NeuralNetwork(nn.Module):
#     def __init__(self):
#         super().__init__()
#         self.neural = nn.Sequential(
#             nn.Conv2d(3, 256, kernel_size=(3, 3), stride=(1, 1)),  # Update input channels to 3
#             nn.ReLU(),
#             nn.Conv2d(256, 512, kernel_size=(3, 3), stride=(1, 1)),
#             nn.ReLU(),
#             nn.Conv2d(512, 64, kernel_size=(3, 3), stride=(1, 1)),
#             nn.ReLU(),
#             nn.Conv2d(64, 32, kernel_size=(3, 3), stride=(1, 1)),
#             nn.ReLU(),
#             nn.Flatten(),
#             nn.Linear(1492992, 3),
#         )

#     def forward(self, x):
#         logits = self.neural(x)
#         return logits
    
model = NeuralNetwork()


train_dataloader = data.DataLoader(train_dataset, batch_size=2)
test_dataloader = data.DataLoader(test_dataset, batch_size=2)

learning_rate = 1e-3

loss_fn = nn.CrossEntropyLoss()

optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

# def update_plot(x_vals):
#     plt.cla()  # Clear the current plot
#     plt.plot(x_vals)

# def train_loop(dataloader, model, loss_fn, optimizer):
#     size = len(dataloader.dataset)
#     model.train()

#     for batch, (X, y) in enumerate(dataloader):
#         pred = model(X)
#         loss = loss_fn(pred, y)

#         loss.backward()
#         optimizer.step()
#         optimizer.zero_grad()

#         if batch % 2 == 0:
#             loss, current = loss.item(), batch
#             acc = (pred.argmax(1) == y).type(torch.float).sum().item()
#             print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")
#             print(f"acc: {acc:>7f}  [{current:>5d}/{size:>5d}]")
            

# def test_loop(dataloader, model, loss_fn):
#     model.eval()
#     size = len(dataloader.dataset)
#     num_batches = len(dataloader)
#     test_loss, test_acc = 0, 0

#     with torch.no_grad():
#         for _, (X, y) in enumerate(dataloader):
#             pred = model(X)
#             test_loss += loss_fn(torch.Tensor(pred), torch.Tensor(y)).item()
#             test_acc += (pred.argmax(1) == y).type(torch.float).sum().item()

#     test_loss /= num_batches
#     test_acc /= size
#     print(f"Test Error: \n Accuracy: {(100*test_acc):>0.1f}%, Avg loss: {test_loss:>8f} \n")

epochs = 2
for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train_loop(train_dataloader, model, loss_fn, optimizer)
    test_loop(test_dataloader, model, loss_fn)
print("Done!")
