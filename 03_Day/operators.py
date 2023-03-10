#!/usr/bin/env python3


def variables_def():
    age = 37
    height = 1.91
    complex = 1 + 1j
    return(age,height,complex)

def triangle_area():
    base_triangle = input("provide base of a triangle: ")
    base_triangle = int(base_triangle)
    height_triangle = input("provide height of a triangle: ")
    height_triangle = int(height_triangle)
    area = base_triangle * height_triangle * 0.5
    return(area)

def display_a_table():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    print("\n",1,1,1,1,1,"\n",
          a,a,a,a,a,"\n",
          b,a,2 * a,a ** 2, a ** 3,"\n",
          c,1,2,4,8,"\n",
          d,1,2,4,8,"\n",
          e,int(e/5),e**2,e**3)

def life_in_seconds():
    years_lived = input("Enter number of years you have lived:")
    years_lived = int(years_lived)
    seconds_lived = years_lived * 365 * 24 * 60 * 60
    print("you have lived",seconds_lived,"seconds")


def is_equal(*args):
    check = (args[0] == args[1])
    return(check)

def words_length(*args):
    check = (len(args[0]) == len(args[1]))
    return(check)
    
# seek "word" in "sentence"
def seek_word(word,sentence):
    check = word in sentence
    return(check)


# input1 = input("input 1:")
# input2 = input("input 2:")

# print(seek_word(input1,input2))

