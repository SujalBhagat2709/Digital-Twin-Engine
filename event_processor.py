from twin_manager import (
    DigitalTwin
)


manager = DigitalTwin()

print(
    "\n====================="
)

print(
    "DIGITAL TWIN ENGINE"
)

print(
    "====================="
)

name = input(
    "\nTwin Name: "
)

if not manager.get_twin(
    name
):

    manager.create_twin(
        name
    )

while True:

    event = input(
        "\nEvent:\n> "
    )

    if event.lower() == "exit":

        break

    twin = manager.get_twin(
        name
    )

    twin["events"].append(
        event
    )

    if (
        "damage"
        in event.lower()
    ):

        twin["health"] -= 10

    elif (
        "repair"
        in event.lower()
    ):

        twin["health"] += 10

        if twin["health"] > 100:

            twin["health"] = 100

    if twin["health"] < 50:

        twin["status"] = (
            "Warning"
        )

    else:

        twin["status"] = (
            "Healthy"
        )

    manager.save()

    print(
        "\nCurrent State"
    )

    print(
        f"Health: "
        f"{twin['health']}"
    )

    print(
        f"Status: "
        f"{twin['status']}"
    )