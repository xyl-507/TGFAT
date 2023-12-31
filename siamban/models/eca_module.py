import torch
from torch import nn
from torch.nn.parameter import Parameter

class eca_layer(nn.Module):
    """Constructs a ECA module.

    Args:
        channel: Number of channels of the input feature map
        k_size: Adaptive selection of kernel size
    """
    def __init__(self, channel, k_size=3):
        super(eca_layer, self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.conv = nn.Conv1d(1, 1, kernel_size=k_size, padding=(k_size - 1) // 2, bias=False) 
        self.sigmoid = nn.Sigmoid()

    # def forward(self, x):
    def forward(self, xf, zf):
        # feature descriptor on the global spatial information
        y = self.avg_pool(zf)
        # print('x.shape:', x.shape)  # x.shape: torch.Size([28, 224, 31, 31])
        # print('y.shape:', y.shape)  # y.shape: torch.Size([28, 224, 1, 1])
        # Two different branches of ECA module  y.squeeze(-1).transpose(-1, -2),shape ([28, 1, 224])
        y = self.conv(y.squeeze(-1).transpose(-1, -2)).transpose(-1, -2).unsqueeze(-1)
        # print('y_conv.shape:', y.shape)  # y_conv.shape: torch.Size([28, 224, 1, 1])
        # Multi-scale information fusion
        y = self.sigmoid(y)
        # print('y.shape', y.shape)  # y.shape torch.Size([28, 224, 1, 1])
        y_1 = y.expand_as(xf)
        # print('y_1.shape', y_1.shape)  # y_1.shape torch.Size([28, 224, 31, 31])
        return xf * y_1
        
