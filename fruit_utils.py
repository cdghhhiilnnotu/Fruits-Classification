from fruits_lib import *

def train_loop(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    model.train()

    for batch, (X, y) in enumerate(dataloader):
        pred = model(X)
        loss = loss_fn(pred, y)

        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        if batch % 2 == 0:
            loss, current = loss.item(), batch
            acc = (pred.argmax(1) == y).type(torch.float).sum().item()
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")
            print(f"acc: {acc:>7f}  [{current:>5d}/{size:>5d}]")
            

def test_loop(dataloader, model, loss_fn):
    model.eval()
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    test_loss, test_acc = 0, 0

    with torch.no_grad():
        for _, (X, y) in enumerate(dataloader):
            pred = model(X)
            test_loss += loss_fn(torch.Tensor(pred), torch.Tensor(y)).item()
            test_acc += (pred.argmax(1) == y).type(torch.float).sum().item()

    test_loss /= num_batches
    test_acc /= size
    print(f"Test Error: \n Accuracy: {(100*test_acc):>0.1f}%, Avg loss: {test_loss:>8f} \n")