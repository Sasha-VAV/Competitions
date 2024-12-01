import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import numpy as np
from torch.utils.data import Dataset, DataLoader


class MLP(nn.Module):
    def __init__(self, input_size, output_size, hidden_sizes, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fc1 = nn.Linear(input_size, hidden_sizes[0])
        self.fc2 = nn.Linear(hidden_sizes[0], hidden_sizes[1])
        self.fc3 = nn.Linear(hidden_sizes[1], hidden_sizes[2])
        self.fc4 = nn.Linear(hidden_sizes[2], output_size)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.relu(self.fc3(x))
        x = self.fc4(x)
        return x


def normalize_data(train_data, test_data=None):
    def normalize_s(s, data):
        unique_maps = train_data[s].unique()
        normalized_map_values = np.linspace(0, 1, len(unique_maps), endpoint=False)
        maps_map = dict(zip(unique_maps, normalized_map_values))
        data[s] = data[s].map(maps_map)
        return data

    def normalize_n(s, data):
        data[s] = (data[s] - np.min(train_data[s]))/(np.max(train_data[s]) - np.min(train_data[s]))
        return data

    norm_str_list = ['mapName', 'ctTeam', 'tTeam', 'ctBuyType', 'tBuyType']
    norm_num_list = ['roundNum', 'ctScore', 'tScore', 'ctFreezeTimeEndEqVal',
                     'ctRoundStartEqVal', 'tFreezeTimeEndEqVal', 'tRoundStartEqVal']
    result_train_data = train_data.copy()
    result_test_data = test_data.copy()
    for param in norm_str_list:
        result_train_data = normalize_s(param, result_train_data)
        if test_data is not None:
            result_test_data = normalize_s(param, result_test_data)
    for param in norm_num_list:
        result_train_data = normalize_n(param, result_train_data)
        if test_data is not None:
            result_test_data = normalize_n(param, result_test_data)
    return result_train_data, result_test_data


pd.options.display.max_columns = None

train_df = pd.read_csv('data_task11/Предсказание победителя в раунде матча по Counter-Strike/train.csv')
test_df = pd.read_csv('data_task11/Предсказание победителя в раунде матча по Counter-Strike/test.csv')
print(train_df.head())
train_df, test_df = normalize_data(train_df, test_df)
print(train_df.head(), test_df.head())


class CSDataset(Dataset):
    def __init__(self, X, y):
        self.X = X.values
        if y is not None:
            self.y = y.values
        else:
            self.y = None

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], (self.y[idx] if self.y is not None else None)


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
net = MLP(input_size=12, output_size=1, hidden_sizes=(64, 128, 10))
# net.to(device)
loss_fn = nn.MSELoss()
optimizer = optim.SGD(net.parameters(), lr=0.001)

X_train, Y_train = train_df.iloc[:, :-1], train_df.iloc[:, -1]
X_test = test_df
train_dataset = CSDataset(X_train, Y_train)
test_dataset = CSDataset(X_test, None)

batch_size = 128

train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False, drop_last=True)

for epoch in range(100):
    running_loss = 0.0
    for i, dt in enumerate(train_loader):
        inputs, labels = dt
        inputs, labels = inputs.to(torch.float), labels.to(torch.float)
        # inputs, labels = inputs.to(device), labels.to(device)
        optimizer.zero_grad()
        ans = net(inputs)
        loss = loss_fn(ans, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    print(f'Epoch {epoch}, loss: {running_loss * batch_size/len(X_train)}')
