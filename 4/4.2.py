def check(index, x_arr, height_arr, flag):
    count_houses = 0  # Обнуление переменной счетчиков снесенных домов на данной рекурсии

    # НАЧАЛО ЦИКЛА ----------------
    end_while_flag = True
    while end_while_flag:
        # следующий дом, смотрим куда падает текущий дом (флаг влево вправо) и в зависимости от этого проверяем след дом
        if not flag:
            if flag == 1:
                if index != len(x_arr) - 1:  # проверка на конец массива
                    next_house = x_arr[index + 1]
                else:
                    pass  # рекурсия обратно сделать и проверку на то, какая выгоднее
            elif flag == 2:
                if index != 0:  # проверка на конец массива при падении дома налево (обратная рекурсия)
                    next_house = x_arr[index - 1]
                else:
                    return count_houses  # возвращаем кол-во снесенных домов, если рекурсия достигла левого края массива

            now_house = x_arr[index]

            # куда упадет дом (смотрим куда он падает через флаг влево или вправо)
            if flag == 1:
                next_index = now_house + height_arr[index]
            elif flag == 2:
                next_index = next_house - height_arr[index]

            # Проверка, достанет ли дом до следующего
            if flag == 1:
                if next_index < next_house:
                    count_houses_another = check(index, x_arr, height_arr, 2)
                    # СДЕЛАТЬ ПРОВЕКУ НА ТО, КАКАЯ РЕКУРСИЯ ВЫГОДНЕЕ
                    end_while_flag = False
                elif next_index == next_house:
                    count_houses += 1  # +1 упавший дом
                elif next_index > next_house:
                    pass  # УЧЕСТЬ ЗАПАС
            elif flag == 2:
                pass  # СДЕЛАТЬ ТО ЖЕ САМОЕ ЧТО И В ФЛАГ 1

        # КОНЕЦ ЦИКЛА ----------------

        return count_houses


def main():
    n = int(input())
    arr_x = list(map(int, input().split()))
    arr_h = list(map(int, input().split()))
    answer = check(0, arr_x, arr_h, 1)
    print(answer)


if __name__ == "__main__":
    main()
