import torch
from torch_geometric.data import Data

edge_index = torch.tensor([[0, 1, 1],
                           [1, 0, 2]], dtype=torch.long)
x = torch.tensor([[-1,0], [0,0], [1,0]], dtype=torch.float)

data = Data(x=x, edge_index=edge_index)
#>>> Data(edge_index=[2, 4], x=[3, 1])
print(data)
print(data.edge_attr)
print(data.x)
#data.x: Node feature matrix with shape [num_nodes, num_node_features]
#data.edge_index：形状为 [2， num_edges] 且类型为 torch.long 的 COO 格式的图形连接
#data.edge_attr: Edge feature matrix with shape [num_edges, num_edge_features]
print(data.validate(raise_on_error=True))