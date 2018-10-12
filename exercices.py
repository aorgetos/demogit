#!/usr/bin/python3
# -*- coding: utf-8 -*-


from collections import Counter


def find_student():
    marksheet = []
    for _ in range(0, int(input())):
        marksheet.append([input(), float(input())])

    second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
    print('\n'.join([a for a, b in sorted(marksheet) if b == second_highest]))


def find_student_bis():
    scores = []
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        scores.append(score)
    if students:
        sec_lowest = scores[0] if len(scores) < 2 else sorted(scores)[1]
        wanted = [student[0] for student in students if student[1] == sec_lowest]
        for n in sorted(wanted):
            print(n)


def calc_average():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    average = sum(student_marks.get(query_name, 0)) / len(student_marks.get(query_name, 1))
    print("{:.2f}".format(average))


def list_manipulation():
    N = int(input())
    data_list = list()
    for _ in range(N):
        query_cmd, *args = input().split()
        if not args:
            if query_cmd != "print":
                eval("data_list." + query_cmd + "()")
            else:
                print(data_list)
        elif len(args) == 1:
            eval("data_list." + query_cmd + "(" + args[0] + ")")
        else:
            eval("data_list." + query_cmd + "(" + args[0] + "," + args[1] + ")")


def cube():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if ((i + j + k) != n)])


def shoes():
    total_price = 0
    x = int(input())
    shoe_sizes = list(map(int, input().split()))
    for _ in range(int(input())):
        shoe_size, price = list(map(int, input().split()))
        if shoe_size in Counter(shoe_sizes).keys():
            total_price += price
            shoe_sizes.remove(shoe_size)
    print(total_price)


def tkinter_gui():
    import tkinter as tk
    win = tk.Tk()
    win.title("Python GUI")
    win.resizable(False, False)
    win.mainloop()


if __name__ == '__main__':
    tkinter_gui()




