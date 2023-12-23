import copy
from collections import deque

input_data = {}

with open("input.txt", "r") as f:
    for name_type, connections in [
        (line[0], line[1].split(", "))
        for line in [line.strip().split(" -> ") for line in f.readlines()]
    ]:
        if name_type[0] == "%":
            module_type = "flipflop"
            module_name = name_type[1:]
        elif name_type[0] == "&":
            module_type = "conjunction"
            module_name = name_type[1:]
        else:
            module_type = "broadcaster"
            module_name = name_type

        input_data[module_name] = {
            "name": module_name,
            "type": module_type,
            "connections_out": connections,
        }


def solution01(input_data):
    modules = copy.deepcopy(input_data)

    # init modules
    for module_name, module in modules.items():
        module["connections_in"] = []

        # connections_in
        for module_b_name, module_b in modules.items():
            if module_name == module_b_name:
                continue

            if module_name in module_b["connections_out"]:
                module["connections_in"].append(module_b_name)

        # Type specific stuff
        match module["type"]:
            case "flipflop":
                module["state"] = "off"
            case "conjunction":
                module["memory"] = {}

                for connection in module["connections_in"]:
                    module["memory"][connection] = "lo"

    # make it happen
    msg_q = deque()

    count_lo = 0
    count_hi = 0

    def send_pulse(reciever, sender, pulse):
        nonlocal count_lo
        nonlocal count_hi

        match pulse:
            case "lo":
                count_lo += 1
            case "hi":
                count_hi += 1

        msg_q.append((reciever, sender, pulse))

    for _ in range(1000):
        # "push the button"
        send_pulse("broadcaster", "button", "lo")

        while msg_q:
            reciever, sender, pulse = msg_q.popleft()

            if not reciever in modules:
                continue

            reciever_module = modules[reciever]

            match reciever_module["type"]:
                case "broadcaster":
                    for module in reciever_module["connections_out"]:
                        send_pulse(module, reciever, pulse)

                case "flipflop":
                    if pulse == "lo":
                        if reciever_module["state"] == "on":
                            reciever_module["state"] = "off"
                            # send pulse
                            for to_module in reciever_module["connections_out"]:
                                send_pulse(to_module, reciever, "lo")

                        elif reciever_module["state"] == "off":
                            reciever_module["state"] = "on"
                            # send pulse
                            for to_module in reciever_module["connections_out"]:
                                send_pulse(to_module, reciever, "hi")

                case "conjunction":
                    # update state of sender
                    reciever_module["memory"][sender] = pulse

                    if all(
                        [state == "hi" for state in reciever_module["memory"].values()]
                    ):
                        # send pulse
                        for to_module in reciever_module["connections_out"]:
                            send_pulse(to_module, reciever, "lo")
                    else:
                        # send pulse
                        for to_module in reciever_module["connections_out"]:
                            send_pulse(to_module, reciever, "hi")

    return count_lo * count_hi


print("—")
print(f"Solution 01: {solution01(input_data)}")
print("—")
