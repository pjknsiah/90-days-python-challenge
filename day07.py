def main():
    userInfo = {'Victoria': 1234, 'John': 5678, 'Marie': 9101, 'Pierre': 1121, 'Lucius': 3141, 'Nero': 5161}
    username = input("Enter your username: ")
    if username not in userInfo:
        print("Username not found")
    else:
        print(userInfo[username])

if __name__ == "__main__":
    main()
    
