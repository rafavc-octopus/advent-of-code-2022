import string
from itertools import zip_longest


def priority(item_type: str) -> int:
    print(f"Item type: {item_type}")
    alphabet = list(string.ascii_lowercase)
    alphabet.extend(list(string.ascii_uppercase))

    priorities = {
        letter: priority for (letter, priority) in list(zip(alphabet, list(range(1, 53))))
    }

    return priorities.get(item_type)


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def main():
    with open("rucksacks.txt") as file:
        lines = list(file)

    rucksacks = [line for line in lines if line != "\n"]
    rucksacks_by_groups = grouper(rucksacks, 3)
    print("Number of rucksacks: ")
    print(len(rucksacks)) 

    rucksack_priorities = []
    for (index, line) in enumerate(rucksacks_by_groups):
        print(f"\nRucksack {index+1}")
        group_rucksacks = list(line)
        print("\nGroup rucksacks:")
        print(group_rucksacks)
        common_item_types = set(group_rucksacks[0].rstrip("\n")) & set(group_rucksacks[1].rstrip("\n")) & set(group_rucksacks[2].rstrip("\n"))
        print(f"\nCommon item types: {common_item_types}")
        common_item_type_priorities = [priority(item) for item in common_item_types]
        print(f"Common item types priorities: {common_item_type_priorities}")
        rucksack_priorities.append(sum(common_item_type_priorities))

    print(f"Total rucksacks priorities: {sum(rucksack_priorities)}")


if __name__ == "__main__":
    main()