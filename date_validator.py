import dataclasses
from datetime import date, datetime
from typing import Any, Callable
from nicegui import ui


@dataclasses.dataclass
class InputValidator:
    msg: str
    func: Callable[[Any], Any]


class InputValidation:
    def __init__(self, validators: list[InputValidator]) -> None:
        self.validators = validators
        self.value = None

    def __call__(self, value: Any) -> str | None:
        self.value = value
        for validator in self.validators:
            try:
                self.value = validator.func(self.value)
                if self.value is None:
                    return None  # positive early return
            except AssertionError:
                return validator.msg  # negative early return
        return None  # complete validation successful


def required(inp: str) -> str:
    assert inp is not None and len(inp) > 0
    return inp


def valid_date_string(inp: str) -> date:
    try:
        input_date = datetime.strptime(inp, "%d.%m.%Y").date()
    except ValueError:
        raise AssertionError
    return input_date


def too_old(inp: date) -> date:
    assert inp > date.today()
    return inp


RequiredStr = InputValidator(msg="Input required", func=required)
TooOld = InputValidator(msg="Too short.", func=too_old)
ValidDateStr = InputValidator(msg="Invalid date string.", func=valid_date_string)


def validate_input(inp: ui.input, validation: InputValidation) -> None:
    # Perform validation on the input value
    error_message = validation(inp.value)
    if error_message:
        ui.notify(error_message, color="warning")
    else:
        inp.value = validation.value
        ui.notify("Input valid", color="positive")


with ui.input():
    inp = ui.input(label='Date dd.mm.yyyy:')
    validation = InputValidation(validators=[RequiredStr, ValidDateStr, TooOld])
    ui.button('Validate', on_click=lambda: validate_input(inp, validation))


ui.run()