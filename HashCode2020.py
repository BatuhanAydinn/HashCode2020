f= open("a_example.in", "r")
context = f.read()
max_slice = int((context.split("\n")[0]).split(" ")[0])
num_of_type = int((context.split("\n")[0]).split(" ")[1])
slice_array = context.split("\n")[1]
slice_array = [int(x) for x in slice_array.split()]

left = 0
right = num_of_type - 1
temp_left = 0
temp_right = right
max_point = 0
difference = 0
temp_total = 0

max_point_arraylist = []
temp_array = []


def Calculate_Base():
    return slice_array[left] + slice_array[right]


def Temp_right_Goes_Normal():
    global temp_right
    temp_right = right


def First_Check():
    global temp_total
    global right
    if (temp_total > max_slice):
        right = right - 1
        Temp_right_Goes_Normal()
        temp_total = Calculate_Base()


temp_total = Calculate_Base()
temp_array.append(left)
temp_array.append(right)

while (not (left == right)):
    if (temp_total > max_slice):
        right = right - 1
        temp_array.clear()
        temp_array.append(right)
        temp_array.append(left)
        temp_right = right
        temp_total = Calculate_Base()

    elif (temp_total == max_slice):
        max_point_arraylist = list(temp_array)
        print(max_point_arraylist)
        exit(1)
    else:
        if (temp_total > max_point):
            max_point = temp_total
            max_point_arraylist = list(temp_array)

        temp_right = right - 1

        while (not (right == left)):
            while (not (temp_right == left)):


                temp_total += slice_array[temp_right]

                if (temp_total > max_slice):
                    temp_total -= slice_array[temp_right]
                    temp_right -= 1

                elif (temp_total < max_slice):
                    if (not (temp_right == right)):
                        temp_array.append(temp_right)
                    if (temp_total > max_point):
                        max_point = temp_total
                    temp_right -= 1
                elif (temp_total == max_slice):
                    if (not (temp_right == right)):
                        temp_array.append(temp_right)

                    max_point_arraylist = list(temp_array)
                    print(max_point_arraylist)
                    print(temp_total)
                    print(max_slice)
                    exit(2)

            # Çözüm bulundu
            if (temp_total > max_point):
                max_point_arraylist = list(temp_array)
                max_point = temp_total
            temp_array.clear()
            temp_array.append(left)
            right -= 1
            temp_array.append(right)
            temp_total = 0 + slice_array[left]
            temp_right = right


        left += 1
        right = num_of_type - 1
        temp_array.clear()
        temp_array.append(left)
        temp_array.append(right)
        temp_right = right
        temp_total = Calculate_Base()

print(max_point)

print(max_point_arraylist)