from matplotlib import pyplot as plt
import _pickle as pickle

with open('figure/test.save','rb') as fp:
    data = pickle.load(fp)['data']

plt.imshow(data)
plt.savefig('figure/test.png')