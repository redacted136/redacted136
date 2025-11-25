totalWeight = 0
totalNumber = 0
def main():
    global totalWeight, totalNumber

    Weight = input()
    Weight = int(Weight)
    print(Weight)
    totalWeight = totalWeight + Weight
    print(totalWeight)
    totalNumber = totalNumber + 1
    print(totalNumber)



if(totalWeight > 640):
    print("Lift Overload, step out")
if(totalNumber > 8):
    print("Lift Overload, step out")
main()