def create_scientist_dict(filename):
    scientist_names = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.split(":")
                if len(parts) >=2:
                    letter = parts[0].strip()
                    name = parts[1].strip()
                    scientist_names[letter] = name
    except FileNotFoundError:
        print(f"File named {filename} is not found.")

    return scientist_names

def get_scientist_name(scientist_names):
    scientist_name = input("Enter the (full) first and last name of any scientist: ")

    if not scientist_name:
        print("Invalid input. Please enter your first and last name.")
        return
    
    parts = scientist_name.split()

    if len(parts) < 2:
        print("Invalid input. Please enter both your first and last name.")
        return
    
    letter = parts[0][0].upper()

    if letter in scientist_names:
        print("AI scientist: ", scientist_names[letter])
    else:
        print("No AI scientist found for that letter.")

if __name__ == '__main__':
    scientist_names_dict = create_scientist_dict('scientists.txt')
    if scientist_names_dict:
        get_scientist_name(scientist_names_dict)
    else:
        print("No scientist data available.")
