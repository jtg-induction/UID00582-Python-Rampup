# Common, Not Common
# Given 2 lists in input. Write a program to return the elements, 
# which are common to both lists(set intersection) and those which are not common(set symmetric difference) between the lists.
# Input: 
# Mainstream = ["One Punch Man","Attack On Titan","One Piece","Sword Art Online","Bleach","Dragon Ball Z","One Piece"]
# must_watch = ["Full Metal Alchemist","Code Geass","Death Note","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack On Titan"]
# f(mainstream, must_watch) should return:
# ["One Piece", "Attack On Titan"], ["Dragon Ball Z", "Death Note", "One Punch Man", "Stein's Gate", "The Devil is a Part Timer!", "Sword Art Online","Full Metal Alchemist","'Bleach", "Code Geass"]


def intersection_sym_diff(mainstream, must_watch):
    intersection = sym_difference = list()

    intersection = list(set(mainstream) & set(must_watch))
    sym_difference = list(set(mainstream) ^ set(must_watch))

    return [intersection, sym_difference]


mainstream = ["One Punch Man", "Attack On Titan", "One Piece", "Sword Art Online", "Bleach", "Dragon Ball Z", "One Piece"]
must_watch = ["Full Metal Alchemist", "Code Geass", "Death Note", "Stein's Gate", "The Devil is a Part Timer!", "One Piece", "Attack On Titan"]

intersection, sym_difference = intersection_sym_diff(mainstream, must_watch)
print("Intersection: ",intersection)
print("Symmetric Difference: ", sym_difference)