# Jons list, do not touch
lst = ["Apple", "Orange", "Banana", "Car", "Purple", "Corn", "Zoo"]
lstn = [4, 7, 0, 1, 3, 10, 8, 9, 2, 11, 14, 6, 5, 13, 12]
lstt = [("Brick", 5), ("Jon", 23), ("Phone", 16), ("Elf", 6)]
lstq = []
lstl = [lst, lstn, lstt, lstq]

#Create a function to print a List
def printLst(lst):
    for thing in lst:
        print(thing)
printLst(lst)
printLst(lstn)
printLst(lstl)
