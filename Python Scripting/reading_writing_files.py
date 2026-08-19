def create_scientist_list(filename):
    """Reads the file and extracts a list of AI Scientist names."""
    scientist_list=[]
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.split(",")
                if parts:
                    name = parts[0].strip()
                    scientist_list.append(name)

    except FileNotFoundError:
        print(f"The file {filename} was not found.")

    return scientist_list

scientist_list  = create_scientist_list('ai_scientists.txt')

correct_result = [
    'Alan Turing', 'Barbara Grosz', 'Cynthia Dwork', 'Daphne Koller', 'Erik Brynjolfsson', 'Fei-Fei Li',
    'Geoffrey Hinton', 'Hilary Mason', 'Ian Goodfellow', 'Judea Pearl', 'Kunihiko Fukushima', 'Leslie Valiant',
    'Marvin Minsky', 'Nando de Freitas', 'Oren Etzioni', 'Peter Norvig', 'Qiang Yang', 'Rodney Brooks',
    'Stuart Russell', 'Tim Berners-Lee', 'Ursula Martin', 'Vladimir Vapnik', 'Wendy Hall', 'Xiaojin Zhu',
    'Yann LeCun', 'Zoubin Ghahramani'
]

if scientist_list == correct_result:
    print("Well done!")
else:
    print("Your code produced the wrong result when running on the `ai_scientists.txt`.")