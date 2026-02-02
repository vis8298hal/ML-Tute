print("######################################## Exception Handling ########################################")
try:
    num = int(input("Enter a number to divide 10 by: "))
    x = 10 / num
    print(x)
except ZeroDivisionError as e:
    print(f"Caught an exception: {e}")
except ValueError as e:
    print(f"Can not convert input to an integer: {e}")
finally:
    print("Execution completed, cleaning up resources if any.")