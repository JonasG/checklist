import argparse

def parse_line(line):
    index_of_first_space = line.find(' ')
    operator = line[:index_of_first_space]
    description = line[index_of_first_space + 1:]
    description_without_newline = description.strip()

    return operator, description_without_newline

def handle(commands):
    operator, description = parse_line(commands.next())

    operator_handlers = {
        '*': handle_print,
        '?': handle_question
    }

    while True:
        if not operator in operator_handlers.keys():
            print 'Unknown operator:', operator, ' -- Exiting.'
            break

        try:
            operator, description = operator_handlers[operator](description,
                                                                commands)
        except StopIteration:
            print 'Done!'
            break

def handle_print(description, commands):
    print_and_wait(description)
    return parse_line(commands.next())

def print_and_wait(description):
    raw_input(description)

def handle_question(description, commands):
    answer = raw_input(description + ' ')

    for line in commands:
        operator, description = parse_line(line)
        if operator in ['y', 'n']:
            if operator == answer:
                print_and_wait(description)
        else:
            return operator, description

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('checklistfile', type=argparse.FileType('r'))

    args = parser.parse_args()

    handle(args.checklistfile)
