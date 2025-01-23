import os.path as osp

import pandas as pd
import torch
from sentence_transformers import SentenceTransformer

from torch_geometric.data import HeteroData, download_url, extract_zip
from torch_geometric.transforms import RandomLinkSplit, ToUndirected

def load_node_csv(path, index_col, encoders=None, **kwargs):
    df = pd.read_csv(path, index_col=index_col, **kwargs)
    mapping = {index: i for i, index in enumerate(df.index.unique())}

    x = None
    if encoders is not None:
        xs = [encoder(df[col]) for col, encoder in encoders.items()]
        x = torch.cat(xs, dim=-1)

    return x, mapping

path = "user_x, user_mapping = load_node_csv(rating_path, index_col='userId')"
user_x, user_mapping = load_node_csv(path, index_col='userId')