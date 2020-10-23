'''
    Problem Task : Write a function that takes coordinates of two points on a two-dimensional plane and returns the length of the line segment connecting those two points.

    Problem Link : https://edabit.com/challenge/3Ekam9jvbNKHDtx4K
'''

def line_length(point1, point2):
    length_x = abs(point1[0]-point2[0])
    length_y = abs(point1[1]-point2[1])
    length_connecting = ((length_x ** 2) + (length_y ** 2)) ** .5
    return round(length_connecting, 2)

