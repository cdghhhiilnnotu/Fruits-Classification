from fruits_lib import *

class FruitsTransform():
    def __init__(self, resize=224, mean=(0.485), std=(0.229)):
        self.data_transform = {
            'train': transforms.Compose([
                transforms.Resize(resize),
                transforms.ToTensor(),
                transforms.Normalize(mean, std)
            ]),
            'test': transforms.Compose([
                transforms.Resize(resize),
                transforms.ToTensor(),
                transforms.Normalize(mean, std)
            ])
        }

    def __call__(self, img, phase="train"):
        return self.data_transform[phase](img)


