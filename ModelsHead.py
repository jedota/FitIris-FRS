import torch as th
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

class SingleLayerHead(nn.Module):
    def __init__(self, input_dim:int, output_dim:int):
        """
        input_dim: 
        output_dim:
        """
        super(SingleLayerHead, self).__init__()

        self.dense1 = nn.Linear(input_dim, output_dim)


    def forward(self, x):

        x = self.dense1(x)

        return x


class FinalHead(nn.Module):
    def __init__(self, input_dim:int, output_dim:int, relu:bool=False):
        """
        input_dim: 
        output_dim:
        relu: add relu act func after linear layers
        """
        super(FinalHead, self).__init__()

        self.relu = relu

        if self.relu:
            self.layers = nn.Sequential(
                                                nn.Linear(in_features=input_dim, out_features=256, bias=True),
                                                nn.ReLU(),
                                                nn.Linear(in_features=256, out_features=128, bias=True),
                                                nn.Linear(in_features=128, out_features=64, bias=True),
                                                nn.ReLU(),
                                                nn.Linear(in_features=64, out_features=output_dim, bias=True),
                                                )

        else:
            self.layers = nn.Sequential(
                                                nn.Linear(input_dim, 256),
                                                nn.Linear(256, 128),
                                                nn.Linear(128, 64),
                                                nn.Linear(64, output_dim),
            )

    def forward(self, x):
        x = self.layers(x)
        
        return x    

