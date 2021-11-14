import pandas as pd
import matplotlib.pyplot as plt


def create_image(city_name, temp_min, temp, temp_max):
    df = pd.DataFrame({'difference_weather': ['минимальная', 'сейчас', 'максимальная'], 'temp': [temp_min, temp, temp_max]})

    plt.plot(df['difference_weather'], df['temp'])
    plt.grid(color='black', linestyle='-', linewidth=0.2)
    plt.suptitle(f'Температура {city_name}')
    plt.ylim(bottom=None)
    return plt.savefig('image.png')
