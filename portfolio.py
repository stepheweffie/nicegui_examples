from nicegui import ui
import os

ai_images = os.listdir('static/ai')


def portfolio_name(fname: str, lname: str):
    with ui.row().classes('justify-end wrap flex w-full'):
        ui.label(f'{fname}').classes('font-bold').style(replace='margin-left: 10%; margin-top: 2%; font-size: 12vw;'
                                                                'margin-bottom: -10%;')
        ui.label(f'{lname}').classes('font-bold').style(replace='font-size: 12vw; margin-top: 2%;')


def portfolio_section(heading: str, images: list, media: str):
    with ui.column().style(replace='padding-left: 10%;'):
        ui.label(f'{heading}').classes('font-bold').style(replace='margin-top: 20%; font-size: 9vw;')
    with ui.row().classes('justify-end w-full wrap flex').style(replace='margin-top: -5%; padding-left: 10%;'):
        for image in images:
            ui.image(f'static/{media}/{image}').classes('w-1/4 h-1/4')


@ui.page('/')
def index():
    portfolio_name('Works', 'Stephanie King')
    portfolio_section('AI', ai_images, 'ai')


ui.run()

