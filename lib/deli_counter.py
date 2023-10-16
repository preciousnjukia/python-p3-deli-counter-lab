class DeliCounter:
    KATZ_DELI = []
    OTHER_DELI = ["Logan", "Avi", "Spencer"]
    ANOTHER_DELI = ["Amanda", "Annette", "Ruchi", "Jason", "Logan", "Spencer", "Avi", "Joe", "Rachel", "Lindsey"]


def line(queue):
    if not queue:
        print("The line is currently empty.")
    else:
        line_status = "The line is currently: " + " ".join([f"{i}. {person}" for i, person in enumerate(queue, start=1)])
        print(line_status)

def take_a_number(queue, name):
    queue.append(name)
    position = len(queue)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(queue):
    if not queue:
        print("There is nobody waiting to be served!")
    else:
        serving_person = queue.pop(0)
        print(f"Currently serving {serving_person}.")