import matplotlib.pyplot as plt

def plot(train, valid, y_label, name, num_epoch):
    plt.figure(figsize=(10,5))
    plt.plot(train, label = 'train')
    plt.plot(valid, label = 'val')
    plt.xlabel('Epoch')
    plt.ylabel(y_label)
    plt.title(name)
    plt.legend()
    plt.xticks(range(0, num_epoch))
    plt.show()
    