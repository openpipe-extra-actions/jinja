"""
# jinja
"""
from openpipe.engine import PluginRuntime
from jinja2 import Environment, FileSystemLoader, select_autoescape

class Plugin(PluginRuntime):

    def on_start(self, config):
        env = Environment(
            loader=FileSystemLoader("."),
            autoescape=select_autoescape(['html', 'xml']),
            trim_blocks=True
        )
        self.template = env.get_template(config['template'])
        self.item_list = []

    def on_input(self, item):
        if self.config['single_item']:
            self.put(self.template.render(item))
        else:
            self.item_list.append(item)

    def on_complete(self):
        if self.item_list:
            self.put(self.template.render(items=self.item_list))
