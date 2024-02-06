katz_deli = []

def line(katz_deli):
    peeps_in_line = []
    greeting = 'The line is currently'
    final_announcement = [ greeting ]
    index = 1
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    elif len(katz_deli) >= 1:
        for peeps in katz_deli:
            assignments = f'{index}. {peeps}.'
            final_announcement.append(assignments)
            index += 1
        print(" ".join(final_announcement))
            

        # index = 1
        # peeps_in_line = []
        # greeting = ["The line is currently"]
        # for peeps in katz_deli:
            
        #     spot_in_line = f"{str(index)}. {peeps}."
        #     peeps_in_line.append(spot_in_line)
        #     # new_greeting = " ".join(greeting)
        #     breakpoint()
        #     # print(new_greeting)
        #     index += 1
        #     # name_spot_join = ". ".join(name_spot)
        #     # full_greeting = [ greeting, name_spot_join ]
        #     # print(greeting)
        #     # print(full_greet)


def take_a_number():
    return None

def now_serving():
    return None