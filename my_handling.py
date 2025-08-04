
try:
        # Try opening the file
        with open("my_file.txt", "r") as file:
            content = file.read()
            print(content)

        # Write to a new file
        with open("my_file_w.txt", "w") as file:
            file.write('Added a new line to the file')

except FileNotFoundError:
        print("❌ Error: The file does not exist.")

