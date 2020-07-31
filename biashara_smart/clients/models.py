from django.db import models
from django.contrib.auth.models import User

from common.models import Person


class Client(Person):
    """A business person.

    This model should inherit/be linked to auth User model
    If a smarter way of implementing this can be figured out, the better
    """

    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        """String to represent a client."""
        return "{}: {} {}".format(
            self.phone_number, self.first_name, self.last_name
        )


class Employee(Person):
    """Employees employed by clients.

    These are people who operate the businesses registered by clients,
    eg shopkeepers, house agents

    This model should inherit/be linked to auth User model
    If a smarter way of implementing this can be figured out, the better
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    employer = models.ForeignKey(Client, on_delete=models.PROTECT)

    def __str__(self):
        """String to represent an employee."""
        return "{} {} EMPLOYER: {}".format(
            self.first_name, self.last_name, self.employer
        )
