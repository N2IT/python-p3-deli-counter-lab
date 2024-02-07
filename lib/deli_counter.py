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
            

def now_serving(katz_deli):
    # if there is nobody in line then it should print "There is nobody waiting to be served!"
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    # If there are folks in line it should call out 'Currently serving {name}' then they should be removed from the line
    else:
        i = len(katz_deli)
        while i > 0:
            print(f'Currently serving {katz_deli[0]}.')
            katz_deli.pop(0)
            i -= 1
            break
        # serving_line = []
        # while i > 0:
        #     print(f'Currently serving ')
        #     katz_deli.pop(0)
        #     i -= 1
        #     # print(" ".join(serving_line))
        


# now_serving(['Tony', 'Manny', 'Xavi', 'Cathy'])

        # index = len(katz_deli) - 1
        # while index >= 0:
        #     print(f'Currently serving {katz_deli[0]}.')
        #     del katz_deli[0]
        #     index -= 1