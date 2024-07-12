from fruits_lib import *
from fruits_dataset import *
from fruits_datapath import *

class FruitPlot:
    def __init__(self):
        self.acc = []
        self.loss = []

    def plot_datasets(self, fruits_dataset, num_row=3, num_col=3, 
        label_map = {
            0: "Apple",
            1: "Banana",
            2: "Orange"
        }):
        figure = plt.figure(figsize=(8, 8))
        cols, rows = num_col, num_row
        for i in range(1, cols * rows + 1):
            sample_idx = torch.randint(len(fruits_dataset), size=(1,)).item()
            img, label = fruits_dataset[sample_idx]
            figure.add_subplot(rows, cols, i)
            try:
                plt.title(label_map[label])
            except:
                plt.title(label)

            plt.axis("off")
            img = img.numpy().transpose(1,2,0)
            img = np.clip(img, 0, 1)
            plt.imshow(img.squeeze(), cmap="gray")
        plt.show()

    def plot_history(self, acc, loss):
        fig, ax = plt.subplots()

        line, = ax.plot(self.acc, [], marker='o', color='b', label="Dynamic Array")

        ax.set_xlim(0, 100)

        def update_plot(i):
            value = np.random.randint(1, 10)
            self.acc.append(value)

            line.set_data(range(len(self.acc)), self.acc)

            ax.set_xlim(0, len(self.acc) + 1)
            ax.plot(self.acc, marker='o', color='b', label="Acc")

        ani = FuncAnimation(fig, update_plot, frames=10, repeat=False)

        ax.legend()

        print("Before plt.show()")
        plt.show()

    


if __name__ == "__main__":
    train_list = FruitDatapath("data", "train")()
    test_list = FruitDatapath("data", "test")()

    train_dataset = FruitDataset(train_list, fruit_transform=FruitsTransform(), phase="train", fruit_classes=['apple', 'banana', 'orange'])
    test_dataset = FruitDataset(test_list, fruit_transform=FruitsTransform(), phase="test", fruit_classes=['apple', 'banana', 'orange'])

    plot = FruitPlot()
    plot.plot_datasets(train_dataset)

