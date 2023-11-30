
ar_1=[2,6,8,11,14,17,19]
ar_2=[3, 2, 1, 5, 4, 2, 1]
ar_3=[[0,0],[0,1],[0,0],[2,2],[4,2],[0,1],[0,0]]


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

    print(arr_x_1,arr_x_2)

break_max_height_buildings(ar_1,ar_2,ar_3)

