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