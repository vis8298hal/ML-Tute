def main():
    value = "four"
    match value:
        case "one":
            result = 1
        case "two":
            result = 2
        case "three":
            result = 3
        case "four":
            result = 4
        case _:
            result = -1
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()