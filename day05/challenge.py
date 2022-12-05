
def remove_extra_characters(items: list, limit_length: int, character: str) -> None:
    if len(items) > limit_length:
        next_position = items.index(character) + 1
        if next_position < len(items) and items[next_position] == "":
            items.remove(character)


def prepare_starting_distribution(lines: list[str]) -> list[list[str]]:
    starting_distribution = [[[] for row in range(8)] for column in range(9)]
    
    for (index, line) in enumerate(lines[0:8]):
        only_one_whitespace_line = line.strip("\n").split(" ")
        one_whitespace_line = []
        skipped_whitelines = 0
        for (i, item) in enumerate(only_one_whitespace_line):
            if skipped_whitelines < 2 and i + 1 < len(only_one_whitespace_line) and (item == "" and only_one_whitespace_line[i + 1] == ""):
                skipped_whitelines += 1
                continue
            else:
                skipped_whitelines = 0
                one_whitespace_line.append(item.strip("[]"))

        if len(one_whitespace_line) > 9:
            if one_whitespace_line[len(one_whitespace_line) - 1] == "" and one_whitespace_line[len(one_whitespace_line) - 2] == "":
                one_whitespace_line.pop()
        
            if index != 2:
                for i in range(9):
                    remove_extra_characters(one_whitespace_line, 9, "")

        if index == 2:
            one_whitespace_line.pop(index)
            one_whitespace_line.pop(index + 1)

        if index == 3:
            one_whitespace_line.pop(index)

        starting_distribution[index] = one_whitespace_line
    
    # TODO: To remove extra last unnecessary line
    starting_distribution = starting_distribution[0:8]
    return starting_distribution


def first_part():
    with open("crates.txt") as file:
        lines = list(file)

        starting_distribution = prepare_starting_distribution(lines)

        print("\nStarting distribution before transposing the crate matrix:")
        for line in starting_distribution:
            print(line)

        transposed_distribution = [list(item) for item in zip(*starting_distribution)]
        print("\nTransposed distribution before reversing to create columns the stacks:")
        for line in transposed_distribution:
            print(line)

        crate_distribution = [[[] for row in range(8)] for column in range(9)]
        crate_distribution = [[], [], [], [], [], [], [], [], []]
        for (row, sublist) in enumerate(transposed_distribution):
            for (column, item) in reversed(list(enumerate(sublist))):
                if item != "":
                    crate_distribution[row].append(item)
        
        print("\nTransposed distribution formed by crate stacks:")
        for line in crate_distribution:
            print(line)
        
        for line in lines[10:]:
            instruction_parts = line.split(" from ")
            number_of_items = instruction_parts[0].split(" ")[1]
            origin_stack = instruction_parts[1].split(" ")[0]
            destiny_stack = instruction_parts[1].split(" ")[2]
            for index in range(int(number_of_items)):
                item_to_move = crate_distribution[int(origin_stack) - 1].pop()
                crate_distribution[int(destiny_stack) - 1].append(item_to_move)
        
        print("\nTransposed distribution without blanks:")
        for line in crate_distribution:
            print(line)

        latest_crates = "".join([crate[-1] for crate in crate_distribution])
        print(f"\nLatest crates: {latest_crates}")


if __name__ == "__main__":
    first_part()
