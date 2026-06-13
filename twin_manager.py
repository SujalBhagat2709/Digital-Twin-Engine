import json
import os


class DigitalTwin:

    def __init__(self):

        self.file_name = "twins.json"

        self.twins = {}

        self.load()

    def load(self):

        if os.path.exists(
            self.file_name
        ):

            with open(
                self.file_name,
                "r"
            ) as file:

                self.twins = json.load(
                    file
                )

    def save(self):

        with open(
            self.file_name,
            "w"
        ) as file:

            json.dump(
                self.twins,
                file,
                indent=4
            )

    def create_twin(
        self,
        name
    ):

        self.twins[name] = {

            "health": 100,

            "status": "Healthy",

            "events": []

        }

        self.save()

    def get_twin(
        self,
        name
    ):

        return self.twins.get(
            name
        )


if __name__ == "__main__":

    manager = DigitalTwin()

    twin_name = input(
        "Twin Name: "
    )

    manager.create_twin(
        twin_name
    )

    print(
        "Twin Created"
    ) 