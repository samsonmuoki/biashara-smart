"""Common constants values."""

MONTH_CHOICES = (
    (1, "January"),
    (2, "February"),
    (3, "March"),
    (4, "April"),
    (5, "May"),
    (6, "June"),
    (7, "July"),
    (8, "August"),
    (9, "September"),
    (10, "October"),
    (11, "November"),
    (12, "December"),
)

YEAR_CHOICES = (
    (2019, "2019"),
    (2020, "2020"),
    (2021, "2021"),
)

CURRENCY_CHOICES = (
    ("KSH", "Kenya Shillings"),
    ("USD", "US Dollars"),
)


PAYMENT_METHODS = (
    ("cash", "Cash"),
    ("mpesa", "Mpesa"),
    ("bank", "Bank"),
)

EXPENSE_TYPES = (
    ("water", "Water"),
    ("electricity", "Electricity"),
    ("loan", "Loan"),
    ("other", "Other"),
)
