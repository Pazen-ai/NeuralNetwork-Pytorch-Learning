# # 3.3
# import numpy as np
# import torch
# from torch.utils import  data
# from d2l import torch as d2l
#
# true_w = torch.tensor([2,-3.4])
# true_b = 4.2
# features,labels = d2l.synthetic_data(true_w,true_b,1000)
#
# def  load_array(data_arrays,batch_size,is_train=True):
#     dataset = data.TensorDataset(*data_arrays)
#     return data.DataLoader(dataset,batch_size,shuffle=is_train)
# batch_size = 10
# data_iter = load_array((features,labels),batch_size)
# # print(next(iter(data_iter)))
# from torch import nn
# net = nn.Sequential(
#                     nn.Linear(2,1))
# net[0].weight.data.normal_(0,0.01)
# net[0].bias.data.fill_(0)
# loss = nn.MSELoss()
# trainer = torch.optim.SGD(net.parameters(),lr=0.03)
# num_epochs = 3
# for epoch in range(num_epochs):
#     for x,y in data_iter:
#         l = loss(net(x),y)
#         trainer.zero_grad()#清空梯度缓冲，准备反向传播
#         l.backward()
#         trainer.step()
#     l = loss(net(features),labels)
#     print('epoch %d, loss: %f' % (epoch + 1, l.mean().item()))
# w = net[0].weight.data
# print('w的估计误差:',true_w - w.reshape(true_w.shape))
# b = net[0].bias.data
# print('b的估计误差:',true_b - b)
# # 3.4 softmax