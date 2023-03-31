import torch
import matplotlib.pyplot as plt

with open('progress.txt','r') as f:
    lines = f.readlines()

headings = lines[0].split("\t")
results_dict = dict()
for result in headings:
    results_dict[result] = []

for line in lines[1:]:
    line = line.split("\t")
    print(line)
    for i, head in enumerate(headings):
        results_dict[head].append(line[i])

for heading in results_dict:
    if 'rho_bin' in heading:
        results_dict[heading] = [float(results_dict[heading][i][7:-1]) for i in range(len(results_dict[heading]))]
        

histogram = torch.histogram(torch.tensor([results_dict[f"rho_bin_{i}_count"] for i in range(11)]), bins=11, range=[0,1.1]).hist
plt.plot(histogram)
plt.savefig("histogram")
