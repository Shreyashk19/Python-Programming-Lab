main_string = input("Enter the main string: ")
substring = input("Enter the substring to search: ")

if substring in main_string:
    print("Substring exists in the string")
else:
    print("Substring does not exist in the string")