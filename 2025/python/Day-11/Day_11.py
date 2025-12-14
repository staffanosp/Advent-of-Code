from collections import deque, defaultdict

input_data = {}

with open("input.txt", "r") as f:

    for line in [line.strip() for line in f.readlines()]:
        k, outputs = line.split(": ")
        outputs = outputs.split(" ")
        input_data[k] = outputs


def solution01(nodes):

    START = "you"
    END = "out"

    q = deque(nodes[START])

    counter = 0

    while q:
        node = q.pop()

        connections = nodes[node]

        for connection in connections:
            if connection == END:

                counter += 1
                continue

            q.append(connection)

    return counter


def memoize(k, f, memo):

    if not k in memo:
        memo[k] = f(k, memo)

    return memo[k]


def solution02(input_data):

    START = "svr"
    END = "out"

    def node_factory():
        return {
            "inputs": [],
            "outputs": [],
        }

    nodes = defaultdict(node_factory)

    # add the inputs to the nodes
    for a, outputs in input_data.items():
        for b in outputs:
            nodes[a]["outputs"].append(b)
            nodes[b]["inputs"].append(a)

    def step(args, memo):

        node, score = args

        if node in {"dac", "fft"}:
            score += 1

        if node == START:
            if score == 2:
                return 1
            else:
                return 0

        return sum(
            [
                memoize((input_node, score), step, memo)
                for input_node in nodes[node]["inputs"]
            ]
        )

    return memoize((END, 0), step, {})


print("—")
print(f"Solution 01: {solution01(input_data)}")
print(f"Solution 02: {solution02(input_data)}")

print("—")
