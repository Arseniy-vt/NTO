def analise_massive(arr_x, arr_h):
    result_arr = []
    for i_now in range(len(arr_x)):
        # Снос здания вправо
        arr_right = [0]
        index_right = 0
        flag = 0
        i = i_now
        n = len(arr_x)
        while i < n - 1:
            if flag:
                if arr_x[i] + arr_h[i] == arr_x[i + 1]:
                    arr_right[index_right] += 1
                elif arr_x[i] + arr_h[i] > arr_x[i + 1]:
                    start_i = i
                    while arr_x[start_i] + arr_h[start_i] >= arr_x[i]:
                        arr_right[index_right] += 1
                        i += 1
                        if i == n - 1:
                            break
                        if arr_x[start_i] + arr_h[start_i] == arr_x[i] or arr_x[start_i] + arr_h[start_i] < arr_x[
                            i + 1]:
                            break
                    i -= 1
                else:
                    break
            else:
                if arr_x[i] + arr_h[i] == arr_x[i + 1]:
                    flag = 1
                    arr_right[index_right] += 1
                elif arr_x[i] + arr_h[i] > arr_x[i + 1]:
                    start_i = i
                    while arr_x[start_i] + arr_h[start_i] >= arr_x[i]:
                        arr_right[index_right] += 1
                        i += 1
                        if i == n - 1:
                            break
                        if arr_x[start_i] + arr_h[start_i] == arr_x[i] or arr_x[start_i] + arr_h[start_i] < arr_x[
                            i + 1]:
                            break
                    i -= 1
                    flag = 1
                else:
                    break
            i += 1

        right = arr_right[0]

        # Проверка здания на снос влево
        arr_left = [0]
        index_left = 0
        flag = 0
        i = i_now
        while i > 0:
            if flag:
                if arr_x[i] - arr_h[i] == arr_x[i - 1]:
                    arr_left[index_left] += 1
                elif arr_x[i] - arr_h[i] < arr_x[i - 1]:
                    start_i = i
                    while arr_x[start_i] - arr_h[start_i] <= arr_x[i]:
                        arr_left[index_left] += 1
                        i -= 1
                        if i == 0:
                            break
                        if arr_x[start_i] - arr_h[start_i] == arr_x[i] or arr_x[start_i] - arr_h[start_i] > arr_x[
                            i - 1]:
                            break
                    i += 1
                else:
                    break
            else:
                if arr_x[i] - arr_h[i] == arr_x[i - 1]:
                    flag = 1
                    arr_left[index_left] += 1
                elif arr_x[i] - arr_h[i] < arr_x[i - 1]:
                    start_i = i
                    while arr_x[start_i] - arr_h[start_i] >= arr_x[i]:
                        arr_left[index_left] += 1
                        i -= 1
                        if i == 0:
                            break
                        if arr_x[start_i] - arr_h[start_i] == arr_x[i] or arr_x[start_i] - arr_h[start_i] > arr_x[
                            i - 1]:
                            break
                    i += 1
                    flag = 1
                else:
                    break
            i -= 1

        left = arr_left[0]

        result_arr.append([left, right])
    return result_arr


def break_max_height_buildings(arr_x, arr_h, arr_buildings):
    max_building = 0
    max_len = 0
    for i in range(len(arr_buildings)):
        if max(arr_buildings[i]) > max_len:
            max_building = i
            if arr_buildings[i].index(max(arr_buildings[i])) == 0:
                max_building *= -1
            max_len = max(max_len, max(arr_buildings[i]))
    if max_building >= 0:
        # print(max_building)
        arr_x[max_building]=0
        arr_h[max_building]=0
        max_building += 1
        while max_len != 0:
            arr_x[max_building]=0
            arr_h[max_building]=0
            max_len -= 1
            max_building += 1
    else:
        max_building *= -1
        arr_x[max_building] = 0
        arr_h[max_building] = 0
        max_building -= 1
        while max_len != 0:
            arr_x[max_building] = 0
            arr_h[max_building] = 0
            max_len -= 1
            max_building -= 1

    print(arr_x,arr_h,max_building)

    arr_x_1=arr_x[0:(arr_x.index(0))]
    arr_x=list(reversed(arr_x))
    arr_x_2=arr_x[0:(arr_x.index(0))]

    return arr_x_1,arr_x_2

def main():
    pass