ar_1=[1,4,7,10]
ar_2=[1,3,3,6]
ar_3=[[0,1],[1,2],[2,1],[4,2]]


def break_max_height_buildings(arr_x, arr_h, arr_buildings):
    max_building = 0
    max_len = 0
    for i in range(len(arr_buildings)):
        if max(arr_buildings[i]) > max_len:
            max_building = i
            if arr_buildings[i].index(max(arr_buildings[i])) == 0:
                max_building *= -1
            max_len = max(max_len, max(arr_buildings[i]))
    print(max_building)


break_max_height_buildings(ar_1,ar_2,ar_3)