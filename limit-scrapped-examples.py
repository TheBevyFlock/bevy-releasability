import subprocess
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
        done = subprocess.run(
            [
                "cargo",
                "+nightly",
                "doc",
                "--no-deps",
                "-Zunstable-options",
                "-Zrustdoc-scrape-examples",
            ]
        )
        assert done.returncode == 0


if __name__ == "__main__":
    main()
