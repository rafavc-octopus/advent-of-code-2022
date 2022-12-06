

def first_part():
    with open("packets.txt") as file:
        content = file.read()
    
    marker = find_marker(content, size=4)


def find_marker(datastream: str, size: int) -> str:

    if not size:
        return
    
    candidate_to_marker = "" 
    for (index, character) in enumerate(datastream, start=1):
        candidate_to_marker = "".join([candidate_to_marker, character])
        if len(candidate_to_marker) < size:
            continue
        else:
            # Remove the previous first character included in the candidate
            if len(candidate_to_marker) > size:
                candidate_to_marker = candidate_to_marker[1:]

        if len(candidate_to_marker) == size and len(candidate_to_marker) == len(set(candidate_to_marker)):
            print(f"Found marker {candidate_to_marker} at position {index}!")
            return (candidate_to_marker, index)


if __name__ == "__main__":
    first_part()
