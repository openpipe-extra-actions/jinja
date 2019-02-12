"""
# jinja
"""
from openpipe.engine import PluginRuntime
from jinja2 import Environment, FileSystemLoader, select_autoescape

class Plugin(PluginRuntime):

    def on_start(self, config):
        env = Environment(
            loader=FileSystemLoader("."),
            autoescape=select_autoescape(['html', 'xml'])
        )
        self.template = env.get_template(config['template'])

    def on_input(self, item):
        if not self.config['single_item']:
            return
        self.put(self.template.render(item))
