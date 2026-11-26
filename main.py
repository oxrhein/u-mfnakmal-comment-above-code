"""The Comment Above the Code - make.fun entry.

Writes a single funny, painfully honest comment a developer might leave
above fragile production code, to entry.txt.
Stdlib only, no network, deterministic.
"""

import os

# One line, 123 characters. The gate (RULES.txt) allows 1-200.
LINE = "// Nobody knows what this does. It survived three rewrites, two audits and one exorcism. Touch it and it takes you with it."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
