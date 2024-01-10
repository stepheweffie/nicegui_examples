from nicegui import ui, Client


def scroll_to(client: Client, section_index: int):
    """Scroll to the element by index"""
    script = f"""
        const sections = document.querySelectorAll('.scroll-section');
        if (sections[{section_index}]) {{
            sections[{section_index}].scrollIntoView({{ behavior: 'smooth' }});
        }}
        """
    ui.run_javascript(script)


@ui.page('/')
async def index(client: Client):
    with ui.button(icon='menu', color='white'):
        with ui.menu() as menu:
            ui.menu_item('About', on_click=lambda e: scroll_to(e.client, 0))
            ui.menu_item('Services', on_click=lambda e: scroll_to(e.client, 1))
            ui.separator()
            ui.menu_item('Close', on_click=menu.close)

    def rows(section: str):
        with ui.row().classes('w-full no-wrap justify-center'):
            ui.label(f'{section}').classes('text-xl m-4')

    with ui.row().classes('w-full no-wrap justify-center'):
        about_section = ui.label('About').classes('text-4xl m-4 scroll-section')

    for i in range(10):
        rows('About')

    with ui.row().classes('w-full no-wrap justify-center'):
        services_section = ui.label('Services').classes('text-4xl m-4 scroll-section')

    for i in range(10):
        rows('Services')


ui.run()

