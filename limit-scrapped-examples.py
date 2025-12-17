import sys

import tomli_w
import tomllib


def main():
    with open("Cargo.toml", "rb+") as f:
        data = tomllib.load(f)
    for example in data["example"]:
        example["doc-scrape-examples"] = example["name"] == sys.argv[1]
        with open("Cargo.toml", "wb+") as f:
            tomli_w.dump(data, f)


if __name__ == "__main__":
    main()
