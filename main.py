from sys import argv
from pydantic import BaseModel, ConfigDict


class Person:
    def __init__(self, name) -> None:
        self.name = name

    def hello(self):
        print(f"Ciao da {self.name}")


class PersonModel(BaseModel):
    _pyclass = Person

    model_config = ConfigDict(
        json_schema_extra={
            "name": "nome_default",
        }
    )

    @classmethod
    def get_person_from_config(cls, config) -> Person:

        return cls._pyclass.default(**config)


def main():

    person = PersonModel.get_person_from_config({"name": argv[1]})
    person.hello()

if __name__ == "__main__":
    main()
