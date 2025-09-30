# Week 4 File Read & Write Challenge

def main():
    # Ask user for filename
    filename = input("Enter the filename to read (e.g., sample.txt): ").strip()
    
    # Try to read the file with error handling
    try:
        with open(filename, 'r') as file:
            content = file.read() 
        print(f"Successfully read '{filename}' ({len(content)} characters).")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' doesn't exist. Make sure the name is correct!")
        return  # here you should  Exit the function early
    except PermissionError:
        print(f"Error: No permission to read '{filename}'. Check your file permissions.")
        return
    except Exception as e:  # here you  Catch any other weird errors
        print(f"Oops, something unexpected happened while reading: {e}")
        return
    
    # Modify the content and let's make it all uppercase for fun 
    modified_content = content.upper()
    print("Modified content (first 50 chars preview):")
    print(modified_content[:50] + "..." if len(modified_content) > 50 else modified_content)
    
    # Write  it to new file
    new_filename = filename.replace('.txt', '_modified.txt') 
    try:
        with open(new_filename, 'w') as file:
            file.write(modified_content)
        print(f"Yay! Modified version saved to '{new_filename}'.")
    except PermissionError:
        print(f"Error: Can't write to '{new_filename}' - permission denied.")
    except Exception as e:
        print(f"Error writing file: {e}")

# Run the program
if __name__ == "__main__":
    main()