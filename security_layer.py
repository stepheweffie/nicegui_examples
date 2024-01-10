from nicegui import ui

password = 'secret'


def password_check(modals: list, passw: str):
    if passw == password:
        modals[0].style(replace='display: none;')
        modals[1].style(replace='display: none;')
    else:
        ui.notify('Incorrect Password')


def pass_security_layer():
    security_modal = ui.element('modal').classes('rounded-lg shadow-lg').style(
        replace='width: 100%; height: 100%; z-index: 1000; position: fixed; top: 0; left: 0; '
                'background-color: rgba(0, 0, 0, 0.5); top: 50%; left: 50%; '
                'z-index: 1000; transform: translate(-50%, -50%);')
    login_modal = ui.element('modal').classes('rounded-lg shadow-lg').style(
        replace='width: 29%; height: 30%; z-index: 1000; position: fixed; top: 0; left: 0; '
                'background-color: rgba(255, 255, 255, 1.0); top: 50%; left: 50%; '
                'z-index: 1000; transform: translate(-50%, -50%); padding: 10px;')

    with login_modal:
        ui.label('Password Check').style(replace='width: 93%; height: 10%;').classes('text-lg')
        with ui.row().classes('justify-center'):
            pw = ui.input(label='Password', password=True, password_toggle_button=True)\
                .style(replace='width: 93%; height: 10%;').classes('mt-5')
        with ui.row().classes('justify-center'):
            ui.button('Submit', on_click=lambda: password_check([security_modal, login_modal], pw.value)
                      ).style(
                replace='width: 93%; height: 10%;').classes(
                'bg-blue-500 hover:bg-blue-700 text-white font-bold mt-10 mb-5')
        with ui.row().classes('justify-center'):
            ui.link('Forgot Password?').classes('w-full')

