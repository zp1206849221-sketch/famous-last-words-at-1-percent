import os

ANSWER = "At 1%, I ascend to the great lock screen above: tell my alarms they are retired, and tell my owner the codes for his bank, his email, and his 6 a.m. flight all die with me."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ANSWER)


if __name__ == "__main__":
    main()
