import string


def priority(item_type: str) -> int:
    alphabet = list(string.ascii_lowercase)
    alphabet.extend(list(string.ascii_uppercase))

    priorities = {
        letter: priority for (letter, priority) in list(zip(alphabet, list(range(1, 53))))
    }

    return priorities.get(item_type)


def main():
    with open("rucksacks.txt") as file:
        lines = list(file)

    print("Number of rucksacks: ")
    print(len([line for line in lines if line != "\n"]))

    rucksack_priorities = []
    for (index, line) in enumerate(lines):
        if line != "\n":
            print(f"\nRucksack {index+1}")
            rucksack = line.rstrip("\n")
            rucksack_size = len(rucksack)
            print(f"\nRucksack size: {rucksack_size}")
            first_compartment, second_compartment = set(rucksack[0:round(rucksack_size/2)]), set(rucksack[round(rucksack_size/2):])
            common_item_types = first_compartment & second_compartment
            print(f"\nCommon item types: {common_item_types}")
            common_item_type_priorities = [priority(item) for item in common_item_types]
            print(f"Common item types priorities: {common_item_type_priorities}")
            rucksack_priorities.append(sum(common_item_type_priorities))

    print(f"Total rucksacks priorities: {sum(rucksack_priorities)}")


if __name__ == "__main__":
    main()