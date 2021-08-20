import numpy as np

def game_core_v3(number):
    mid = 50
    low = 1
    high = 100
    count=0
    while mid != number:
        count+=1
        if number > mid:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    return count


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


if __name__ == "__main__":
    score_game(game_core_v3)