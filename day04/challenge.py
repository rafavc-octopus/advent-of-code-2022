
def main():
    with open("cleaning_assignments.txt") as file:
        lines = list(file)

    cleaning_assignments = [line for line in lines if line != "\n"]
    print("Number of cleaning assignments by pairs: ")
    print(len(cleaning_assignments)) 

    number_redundant_assignments = 0
    for (index, line) in enumerate(cleaning_assignments):
        print(f"\nCleaning assignment {index+1}")
        pair_assignments = line.rstrip("\n").split(",")
        first_elf_assignment, second_elf_assignment = tuple(pair_assignments[0].split("-")), tuple(pair_assignments[1].split("-"))
        first_elf_assignment = set(range(int(first_elf_assignment[0]), int(first_elf_assignment[1]) + 1))
        second_elf_assignment = set(range(int(second_elf_assignment[0]), int(second_elf_assignment[1]) + 1))
        print("\nFirst Elf assignment:")
        print(first_elf_assignment)
        print("\nSecond Elf assignment:")
        print(second_elf_assignment)

        if first_elf_assignment.issubset(second_elf_assignment):
            print(f"\nSecond {second_elf_assignment} contains first {first_elf_assignment}")
            number_redundant_assignments += 1
        elif second_elf_assignment.issubset(first_elf_assignment):
            print(f"\nFirst {first_elf_assignment} contains second {second_elf_assignment}")
            number_redundant_assignments += 1

    print(f"Total redundant assignments: {number_redundant_assignments}")


if __name__ == "__main__":
    main()
