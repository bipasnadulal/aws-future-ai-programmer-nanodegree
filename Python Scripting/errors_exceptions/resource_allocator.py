def resource_allocator(resources, tasks):
    """
    Takes the number of resources and tasks as inputs.
    Calculates how many resources each task gets
    and the number of leftover resources.
    Handles division by zero using ZeroDivisionError.
    """
    try:
        resource_per_task = resources // tasks
        num_of_left_resources = resources % tasks
        return resource_per_task, num_of_left_resources

    except ZeroDivisionError:
        print("Cannot allocate resources to zero tasks.")
        return None, None


def main():
    lets_optimize = "y"

    while lets_optimize == "y":
        try:
            resources = int(input("How many computational resources are available? "))

            if resources < 0:
                print("Number of resources cannot be negative. Please enter a positive number.")
                continue

            tasks = int(input("How many tasks need resources? "))

            if tasks < 0:
                print("Number of tasks cannot be negative. Please enter a positive number.")
                continue

            resources_each, leftovers = resource_allocator(resources, tasks)

            if resources_each is not None:
                message = (
                    "Resource Allocation: We will have {} tasks, "
                    "each will get {} resources, and we will have "
                    "{} resources left over."
                )

                print(message.format(tasks, resources_each, leftovers))

            lets_optimize = input(
                "Would you like to optimize more? (y or n) "
            ).lower()

        except ValueError:
            print("Invalid input. Please enter a valid number.")


main()