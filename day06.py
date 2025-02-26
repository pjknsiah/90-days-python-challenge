def main():
    numbers = []
    while True:
        try:
            number = int(input("Input: "))
            numbers.append(number)
        except EOFError:
            break
    length = len(numbers)
    summ = sum(numbers)
    average = summ / length
    print(f"The length of the list is {length} and the average is {average}")
    
if __name__ == "__main__":
    main()