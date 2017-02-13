np.random.seed(42)
x = np.random.randn(100)
bins = np.linspace(-5, 5, 20)
counts = np.zeros_like(bins)
i = np.searchsorted(bins, x)
np.add.at(counts, i, 1)
plt.plot(bins, counts, linestyle='steps')
x = np.random.randn(1000000)
def selection_sort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x

 x = np.array([2, 1, 4, 3, 5])
selection_sort(x)



def bogosort(x):
    while np.any(x[:-1] > x[1:]):
        np.random.shuffle(x)
    return x

 x = np.array([2, 1, 4, 3, 5])
np.sort(x)