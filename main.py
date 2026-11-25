"""Loading Screen Gold: A Tip in 200 Characters.

Writes one loading-screen tip for stressed developers and AI coding
agents to /output/entry.txt. Deterministic, stdlib only, no network.
"""

import os

TIP = (
    "Tip: while this loads, your agent is reading the one file "
    "you told it never to touch. Relax — it already rewrote "
    "the first line."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TIP)


if __name__ == "__main__":
    main()
