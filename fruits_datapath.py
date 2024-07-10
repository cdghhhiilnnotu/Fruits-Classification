from fruits_lib import *

class FruitDatapath():
    def __init__(self, data_path, phase):
        self.data_path = data_path
        self.phase = phase

    def __call__(self):
        target_path = os.path.join(self.data_path + "\\" + self.phase + "\\**\\*.jpg")
        # print(target_path)
        
        path_list = []

        for path in glob.glob(target_path):
            # print(path)
            path_list.append(path)

        return path_list


