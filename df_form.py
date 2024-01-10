from nicegui import ui
import pandas as pd
# from security_layer import pass_security_layer
df = pd.DataFrame()


def request_my_dict(data: dict):
    global df
    df_new = pd.DataFrame([data])
    ui.open('/data')
    if len(df) == 0:
        df = df_new
    else:
        df = pd.concat([df, df_new], ignore_index=True)
    return df


@ui.page('/data')
def data_page():
    global df
    with ui.row():
        # pass_security_layer()
        ui.button("back", on_click=lambda: ui.open('/'))
        ui.button("clear", on_click=lambda: df.drop(df.index, inplace=True))
        ui.button("save", on_click=lambda: print(df))  # save to JSON
    for i, row in df.iterrows():
        ui.label(f"{row.to_dict()}")


@ui.page('/')
def index():
    new = {}
    with ui.row().classes('justify-center w-full'):
        with ui.column().style('padding-left: 0%; padding-top: 10%;'):
            ui.label("Message Form").classes('text-2xl')
            name = ui.input(label="name:").bind_value_to(new, 'name').classes('w-96')
            message = ui.textarea(label="message:").bind_value_to(new, 'message').classes('w-96')
            age = ui.number(label='age:').bind_value_to(new,'age').classes('w-96')
            ui.button("submit", on_click=lambda: request_my_dict(new)).classes('w-96')


ui.run()
