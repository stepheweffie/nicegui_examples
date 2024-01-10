from nicegui import ui
from dotenv import load_dotenv
# import asyncio
# import timeit
# import os
load_dotenv()
# animate_css = os.getenv("ANIMATE_CSS")
animate_css = 'https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css'
row_html = ''


@ui.page('/')
async def main():
    ui.add_head_html(f'''
    <link
    rel="stylesheet"
    href="{animate_css}"
    />''')
    ui.add_head_html('''
     <style>
        :root {
            --nicegui-default-padding: 0rem;
            --nicegui-default-gap: 0rem;
        }
     </style>
    ''')

    quote_classes = 'm-3 p-6 bg-blue-100 rounded-lg animate__animated animate__fadeInUp'
    quote_p_classes = 'font-serif italic text-lg text-gray-700 leading-snug mb-1'
    quote_span_classes = 'text-sm text-gray-500'

    with ui.element('div').classes('flex flex-col items-center justify-center h-screen'):
        with ui.row().classes('flex flex-row items-center justify-center'):
            ui.label('Quoti').classes('text-6xl text-gray-700 animate__animated animate__fadeInDown')
            ui.label(' - ').classes('text-6xl text-gray-700 animate__animated animate__fadeInDown')
            ui.label('dian').classes('text-6xl text-gray-700 animate__animated animate__fadeInDown')
        with ui.row().classes('flex flex-row items-center justify-center'):
            once = ui.label('One post-per-day.').classes('text-2xl text-gray-700 animate__animated '
                                                         'animate__fadeInDown')
            once.style(replace='animation-delay: 1.5s;')

    def quot_row():
        with ui.element('div').classes('flex flex-row no-wrap'):
            def quoti(quot: str, auth: str):
                with ui.element('div').classes(quote_classes):
                    # exploded mapping or hashed map what do you call this?
                    ui.label(f"{quot}").classes(quote_p_classes)
                    ui.label(f"- {auth}").classes(quote_span_classes)

            quot_queue = ['The success combination in business is: Do what you do better... and: do more of what you do.',
                          'Give out what you most want to come back.',
                          'The only way around is through.',
                          ]

            auth_queue = ['David Joseph Schwartz', 'Robin Sharma', 'Robert Frost',
                          ]

            for i in range(len(quot_queue)):
                quoti(quot_queue[i], auth_queue[i])
            # add to the row here with this template
            ui.html(f'''{row_html}''')
            # ui.html('<br>')  doesn't work

    quot_row()

    with ui.row().classes('ml-20 mr-20 flex'):
        daily = ui.label('Media for daily use.').classes('text-6xl text-gray-700 animate__animated '
                                                         'animate__fadeInDown')
        daily.style(replace='animation-delay: 3.5s;')

        daily = ui.label('Once per day.').classes('text-6xl text-gray-700 animate__animated '
                                                  'animate__fadeInDown')
        daily.style(replace='animation-delay: 5.2s;')
        daily = ui.label('Yes, once.').classes('text-6xl text-gray-700 animate__animated '
                                               'animate__fadeInDown')
        daily.style(replace='animation-delay: 6.9s;')

    for i in range(3):
        quot_row()

ui.run(title='Quoti', storage_secret='secret_key', dark=False)