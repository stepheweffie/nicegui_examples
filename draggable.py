from nicegui import ui

source = """
<template id='my-box'>
    <style>
        :host {
          display: block;
          padding: 10px;
          color: white;
          background-color: var(--color);
        }
    </style>
    <slot></slot>
</template>
<script>
    window.customElements.define('my-box', class extends HTMLElement {
        constructor() {
            super();
            const templateEl = document.getElementById('my-box');
            const templateContent = templateEl.content;

            this.attachShadow({mode: 'open'}).appendChild(templateContent.cloneNode(true));
            this.style.setProperty('--color', this.getAttribute('color') || 'gray');
        }
    });
</script>
"""

ui.add_body_html(source)
color = 'purple'
ui.html(f"<my-box color={color}>Hello, this is a message in a {color} box</my-box>")
ui.html(f"<my-box color={color} draggable='true'>You can drag me around!</div>")

ui.run()