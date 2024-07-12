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

model = NeuralNetwork()


train_dataloader = data.DataLoader(train_dataset, batch_size=2)
test_dataloader = data.DataLoader(test_dataset, batch_size=2)

learning_rate = 1e-3

loss_fn = nn.CrossEntropyLoss()

optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

epochs = 2
for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train_loop(train_dataloader, model, loss_fn, optimizer)
    test_loop(test_dataloader, model, loss_fn)
print("Done!")
