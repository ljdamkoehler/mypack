
class NumberStuff():

    def __init__(self) -> None:
        self.name = "Number thing"

    def add_things(num_list):
        sum = 0
        if len(num_list) == 0:
            return False
        for num in num_list:
            sum += num
        print("Here is the sum:", sum)
        return sum
    