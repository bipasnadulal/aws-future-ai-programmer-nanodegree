names = input("Enter names separated by comma: ").split(',')
assignments = input("Enter assignments separated by comma: ").split(',')
grades = input("Enter grades separated by comma: ").split(',')

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. Your current grade is {} and can increase \
if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade))