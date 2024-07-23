import matplotlib.pyplot as plt

def plot_data(new_data):
    plt.figure(figsize=(8, 6))
    plt.scatter(new_data['Max_X'], new_data['Energy'])
    plt.xlabel('Max_X')
    plt.ylabel('Energy')
    plt.title('Energy in function of Max_X')
    plt.grid(True)
    plt.show()
