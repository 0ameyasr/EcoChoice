import torch
import torch.nn as nn
import torch.optim as optim

class ProfileANN(nn.Module):
  def __init__(self):
    super(ProfileANN,self).__init__()
    self.fc1 = nn.Linear(7,16)
    self.fc2 = nn.Linear(16,16)
    self.fc3 = nn.Linear(16,4)

    self.dropout = nn.Dropout(p=0.75)
    self.relu = nn.ReLU()
    self.softmax = nn.Softmax(dim=1)

  def forward(self,x):
    x = self.relu(self.fc1(x))
    x = self.relu(self.fc2(x))
    x = self.dropout(x)
    x = self.softmax(self.fc3(x))
    return x

class DietANN(nn.Module):
  def __init__(self):
    super(DietANN,self).__init__()
    self.fc1 = nn.Linear(14,16)
    self.fc2 = nn.Linear(16,16)
    self.fc3 = nn.Linear(16,16)
    self.fc4 = nn.Linear(16,4)

    self.dropout = nn.Dropout(p=0.50)
    self.relu = nn.ReLU()

  def forward(self,x):
    x = self.relu(self.fc1(x))
    x = self.dropout(x)
    x = self.relu(self.fc2(x))
    x = self.dropout(x)
    x = self.relu(self.fc3(x))
    x = self.dropout(x)
    x = self.fc4(x)
    return x


def profile_classifier(user_requirements):
    model = ProfileANN()
    model.load_state_dict(torch.load('Model/torch/ProfileTorch.pth'))
    model.eval()
    with torch.no_grad():
      profiles = ["HLTI","VIT_ESS","PROT_IN","LOW_SOD"]
      output = model(torch.tensor(user_requirements,dtype=torch.float32))
      _, predicted = torch.max(output.data,1)
      return profiles[predicted[0]]
      
def diet_classifier(item_facts):
    model = DietANN()
    model.load_state_dict(torch.load('Model/torch/DietTorch.pth'))
    model.eval()
    with torch.no_grad():
      output = model(torch.tensor(item_facts,dtype=torch.float32))
      return output.tolist()