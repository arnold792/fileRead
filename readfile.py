def read_and_write_file():
    try:
        # Ask the user for the input file name
        input_file = input("Enter the name of the file to read: ")
        
        # Attempt to open and read the file
        with open(input_file, 'r') as infile:
            content = infile.readlines()

        # Modify the content (example: convert all text to uppercase)
        modified_content = [line.upper() for line in content]

        # Ask the user for the output file name
        output_file = input("Enter the name of the file to write the modified content: ")

        # Write the modified content to the new file
        with open(output_file, 'w') as outfile:
            outfile.writelines(modified_content)
        
        print(f"Modified content has been written to {output_file} successfully!")

    except FileNotFoundError:
        print("Error: The file you are trying to read does not exist. Please check the file name and try again.")
    except IOError:
        print("Error: There was an issue reading or writing the file. Please ensure you have the necessary permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
read_and_write_file()
