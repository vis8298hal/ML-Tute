def main():
    x = 0
    print("############################ While Loop ############################")
    while x < 5:
        print(f"The value of x is: {x}")
        x += 1
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    print("############################ For Loop ############################")
    for day in days:
        print(f"Today is: {day}")
    print("############################ Break continue ############################")
    for x in range(1,20):
        if x==7:
            break
        if x%2==0:
            continue
        print(x)
    print("############################ Enumerate Loops ############################")
    for i, day in enumerate(days):
        print(f"Day {i} is {day}")
if __name__ == "__main__":
    main()