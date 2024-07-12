from fruits_lib import *
from fruits_datapath import *
from fruits_transform import *

class FruitDataset(data.Dataset):
    def __init__(self, fruit_file_list, fruit_transform, phase, fruit_classes):
        self.fruit_file_list = fruit_file_list
        self.phase = phase
        self.fruit_transform = fruit_transform
        self.fruit_classes = fruit_classes

    def __len__(self):
        return len(self.fruit_file_list)
    
    def __getitem__(self, idx):
        img_path = self.fruit_file_list[idx]
        img = Image.open(img_path).convert('RGB')  
        img = img.resize((224, 224), Image.LANCZOS)

        img_transformed = self.fruit_transform(img, self.phase)

        if self.phase == "train":
            label = img_path.split("\\")[2]
        elif self.phase == "test":
            label = img_path.split("\\")[2]
        
        try:
            label = self.fruit_classes.index(label)
        except:
            pass

        return img_transformed, label

if __name__ == "__main__":
    train_list = FruitDatapath("data", "train")()
    test_list = FruitDatapath("data", "test")()

    train_dataset = FruitDataset(train_list, fruit_transform=FruitsTransform(), phase="train", fruit_classes=['apple', 'banana', 'orange'])
    test_dataset = FruitDataset(test_list, fruit_transform=FruitsTransform(), phase="test", fruit_classes=['apple', 'banana', 'orange'])

    label_map = {
        0: "Apple",
        1: "Banana",
        2: "Orange"
    }
    figure = plt.figure(figsize=(8, 8))
    cols, rows = 3, 3
    for i in range(1, cols * rows + 1):
        sample_idx = torch.randint(len(train_dataset), size=(1,)).item()
        img, label = train_dataset[sample_idx]
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



