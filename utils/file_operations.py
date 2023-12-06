
def read_lines(file_dir: str, rstrip: bool = False) -> list[str]:
    texts = []
    with open(file_dir, "r") as f:
        for x in f:
            if rstrip:
                texts.append(x.rstrip())
            else:
                texts.append(x)
    return texts
