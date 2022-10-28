#!/usr/bin/python3
if __name__ == "__main__":
    arguments = ["welcome", "to", "the", "Best", "School"]
    print("{} aguments:".format(len(arguments)))
    for i, m in enumerate(arguments):
        print("{}: {}".format(i, m))

