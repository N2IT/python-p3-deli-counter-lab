katz_deli = []

def line(katz_deli):
    peeps_in_line = []
    final_announcement = [ 'The line is currently:' ]
    index = 1
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    elif len(katz_deli) >= 1:
        for peeps in katz_deli:
            assignments = f'{index}. {peeps}'
            final_announcement.append(assignments)
            index += 1
        print(" ".join(final_announcement))

def take_a_number(katz_deli, name):
    index = 1
    if len(katz_deli) == 0:
        katz_deli.append(name)
        print(f'Welcome, {name}. You are number {index} in line.')
    elif len(katz_deli) >= 1:
        katz_deli.append(name)
        print(f'Welcome, {name}. You are number {len(katz_deli)} in line.')
            


def now_serving():
    return None