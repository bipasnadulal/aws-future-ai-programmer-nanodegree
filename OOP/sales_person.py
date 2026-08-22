from pants import Pants

class SalesPerson:
    def __init__(self, first_name, last_name, employee_id, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary

        self.pants_sold = []
        self.total_sales = 0

    def sell_pants(self, pants):
        self.pants_sold.append(pants)

    def display_sales(self):
        for pants in self.pants_sold:
            print(f"color: {pants.color}, waist_size: {pants.waist_size}, "
                  f"length: {pants.length}, price: {pants.price}")

    def calculate_sales(self):
        total = 0

        for pants in self.pants_sold:
            total += pants.price

        self.total_sales = total
        return self.total_sales

    def calculate_commission(self, percentage):
        self.calculate_sales()
        return percentage * self.total_sales


def check_results():
    pants_one = Pants('red', 35, 36, 15.12)
    pants_two = Pants('blue', 40, 38, 24.12)
    pants_three = Pants('tan', 28, 30, 8.12)
    
    salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)
    
    assert salesperson.first_name == 'Amy'
    assert salesperson.last_name == 'Gonzalez'
    assert salesperson.employee_id == 2581923
    assert salesperson.salary == 40000
    assert salesperson.pants_sold == []
    assert salesperson.total_sales == 0
    
    salesperson.sell_pants(pants_one)
    salesperson.pants_sold[0] == pants_one.color
    
    salesperson.sell_pants(pants_two)
    salesperson.sell_pants(pants_three)
    
    assert len(salesperson.pants_sold) == 3
    assert round(salesperson.calculate_sales(),2) == 47.36
    assert round(salesperson.calculate_commission(.1),2) == 4.74
    
    print('Great job, you made it to the end of the code checks!')
    
check_results()


# return (1.0 / (self.stdev * math.sqrt(2*math.pi))) * math.exp(-0.5*((x - self.mean)/ self.stdev) ** 2)