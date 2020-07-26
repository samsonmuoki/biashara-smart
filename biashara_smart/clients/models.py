# from django.db import models

from common.models import Person


class Client(Person):
    """A business person."""

    def __str__(self):
        """String to represnt a client."""
        return "{}: {} {}".format(
            self.phone_number, self.first_name, self.other_names
        )


class Employee(Person):
    """Employees employed by clients."""
    pass
