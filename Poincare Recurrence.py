from argparse import ArgumentParser
from random import randint
from time import time


def simulate_once_set(n):
    urn_a = set(range(1, n + 1))
    urn_b = set()

    for _ in range(randint(0, n)):
        x = randint(1, n)
        if x in urn_a:
            urn_a.remove(x)
            urn_b.add(x)

    steps = 0
    while urn_b:
        x = randint(1, n)
        if x in urn_a:
            urn_a.remove(x)
            urn_b.add(x)
        elif x in urn_b:
            urn_b.remove(x)
            urn_a.add(x)
        steps += 1

    return steps


def simulate_once_list(n):
    urn_a = list(range(1, n + 1))
    urn_b = []

    for _ in range(randint(0, n)):
        x = randint(1, n)
        if x in urn_a and x not in urn_b:
            urn_a.remove(x)
            urn_b.append(x)

    steps = 0
    while urn_b:
        x = randint(1, n)
        if x in urn_a and x not in urn_b:
            urn_a.remove(x)
            urn_b.append(x)
        elif x in urn_b and x not in urn_a:
            urn_b.remove(x)
            urn_a.append(x)
        steps += 1

    return steps


def resolve_simulator(implementation):
    if implementation == "list":
        return simulate_once_list
    return simulate_once_set


def run_table(start, end, implementation):
    simulate_once = resolve_simulator(implementation)
    print("Balls\tSteps\tTime (ms)\n---------------------")
    for balls in range(start, end + 1):
        t1 = time()
        steps = simulate_once(balls)
        elapsed_ms = (time() - t1) * 1000
        print(f"{balls}\t{steps}\t{elapsed_ms:.3f}")


def run_interactive(implementation):
    simulate_once = resolve_simulator(implementation)
    n = int(input("How many numbers to start with: ").strip())
    steps = simulate_once(n)
    print(f"number of steps taken: {steps}")


def main():
    parser = ArgumentParser(description="Poincare recurrence simulation")
    parser.add_argument(
        "mode",
        nargs="?",
        choices=["table", "interactive"],
        default="table",
        help="table: print results for a range of n, interactive: run one user-provided n",
    )
    parser.add_argument("--start", type=int, default=2, help="Starting n (table mode)")
    parser.add_argument("--end", type=int, default=24, help="Ending n (table mode)")
    parser.add_argument(
        "--implementation",
        choices=["set", "list"],
        default="set",
        help="Choose set-based or list-based simulation logic",
    )
    args = parser.parse_args()

    if args.mode == "interactive":
        run_interactive(args.implementation)
    else:
        run_table(args.start, args.end, args.implementation)


if __name__ == "__main__":
    main()
