from nicegui import ui
from latex_demo import html, strTab, strCode


class LaTeXTemplate(ui.element):
    def __init__(self, script: str, template: str):
        super().__init__()
        self.script = script
        self.template = template
        ui.add_head_html(self.script)
        ui.html(self.template)


head_html = '''
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script type="text/javascript" id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js">
</script>
'''

body_html = html


@ui.page(path='/')
def index():
    with ui.row():
        LaTeXTemplate(head_html, body_html)
    with ui.row():
        ui.markdown(strTab)
    with ui.row():
        ui.html(strCode)


ui.run()