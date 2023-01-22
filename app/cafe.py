import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError('"vaccine" should be in visitor')
        if visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError("The vaccine must not be expired")
        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError("Visitor must wear a mask")
        return f"Welcome to {self.name}"