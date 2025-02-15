def main():
    with open("ethics.txt", "r") as file:
        content = file.read()
        lines = content.splitlines()
        wordCount = len(content.split())
        lineCount = len(lines)
        print(f"There are {lineCount} lines and {wordCount} words in the file")
        print(content)
if __name__ == "__main__":
    main()