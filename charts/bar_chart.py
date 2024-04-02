import numpy as np
from matplotlib import pyplot as plt


def make_bar_chart(plot_info_x,provided_y1, provided_y2):
    x_axis = np.arange(len(plot_info_x))
    y1 = np.array(provided_y1)
    y2 = np.array(provided_y2)

    bar1 = plt.bar(x_axis - 0.1, y1, 0.2, label='Burst-Error Max. 8 Bits')
    bar2 = plt.bar(x_axis + 0.1, y2, 0.2, label='Multiple-Bit Error')
    plt.xticks(x_axis, plot_info_x,  rotation=30)

    plt.xlabel('Rozmiary dwuwymiarowej tablicy')
    plt.ylabel('Liczba wyników fałszywie pozytywnych')
    for rect in bar1 + bar2:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, f'{height:.0f}', ha='center', va='bottom')

    plt.legend()
    plt.tight_layout()
    plt.savefig("false_parity_for_different_errors.png")
    plt.show()
