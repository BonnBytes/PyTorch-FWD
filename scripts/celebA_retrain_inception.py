import PIL.Image
import numpy as np

import torch
import torchvision.transforms
import pandas
import PIL
from typing import Any
from torch import nn
import torch.optim as optim
import tqdm

from torch.utils.data import Dataset
from torch.utils.data import DataLoader

import torchvision

label_map = {pos: key for pos, key in enumerate([
    '5_o_Clock_Shadow',
    'Arched_Eyebrows',
    'Attractive',
    'Bags_Under_Eyes',
    'Bald',
    'Bangs',
    'Big_Lips',
    'Big_Nose',
    'Black_Hair',
    'Blond_Hair',
    'Blurry',
    'Brown_Hair',
    'Bushy_Eyebrows',
    'Chubby',
    'Double_Chin',
    'Eyeglasses',
    'Goatee',
    'Gray_Hair',
    'Heavy_Makeup',
    'High_Cheekbones',
    'Male',
    'Mouth_Slightly_Open',
    'Mustache',
    'Narrow_Eyes',
    'No_Beard',
    'Oval_Face',
    'Pale_Skin',
    'Pointy_Nose',
    'Receding_Hairline',
    'Rosy_Cheeks',
    'Sideburns',
    'Smiling',
    'Straight_Hair',
    'Wavy_Hair',
    'Wearing_Earrings',
    'Wearing_Hat',
    'Wearing_Lipstick',
    'Wearing_Necklace',
    'Wearing_Necktie',
    'Young'
])}

class CelebADataset(Dataset):
    
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.annos = np.array(pandas.read_csv(f"{data_dir}/Anno/list_attr_celeba.txt"))
        self.annos_dict = {int(row[0].split()[0].split(".")[0]): row[0].split()[1:] for row in self.annos[1:]}
        self.transforms = nn.Sequential(
            torchvision.transforms.Resize((299, 299)),
        )
        self.to_tensor = torchvision.transforms.ToTensor()


    def __len__(self):
        return len(self.annos_dict)

    def __getitem__(self, index) -> torch.Tensor:
        img_no_str = '0'*(6 - len(f"{index:d}")) + f"{index:d}"
        img_path = f"{self.data_dir}/Img/img_align_celeba_png/{img_no_str}.png"
        with PIL.Image.open(img_path) as im:
            tensor = self.to_tensor(self.transforms(im))
        anno = torch.tensor([int(attribute) for attribute in self.annos_dict[index]])
        anno = (anno + 1) // 2
        return {'img': tensor, 'anno': anno}


if __name__ == "__main__":
    dataset = CelebADataset(data_dir='/home/wolter/Downloads/CelebA')

    net = torchvision.models.Inception3()
    net.fc = nn.Linear(2048, 40)
    # pass
    test_size = 128
    lr = 0.001
    comp_stats = True

    train_set, test_set = torch.utils.data.random_split(dataset, [len(dataset) - test_size, test_size])

    train_loader = DataLoader(train_set, batch_size=64, shuffle=True)
    test_loader = DataLoader(test_set, batch_size=128)

    net = net.cuda()
    optimizer = optim.Adam(net.parameters(), lr=lr)
    cost = nn.BCEWithLogitsLoss()

    bar = tqdm.tqdm(train_loader)

    for batch in bar:
        x = batch['img'].cuda()
        y = batch['anno'].cuda().type(torch.float32)

        yhat = net(x).logits

        cost_val = cost(yhat, y)

        bar.set_description(f"cost: {cost_val.item()}")
