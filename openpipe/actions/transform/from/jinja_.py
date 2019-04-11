"""
Create content using a Jinja2 template
"""
from openpipe.pipeline.engine import ActionRuntime
from jinja2 import Environment, FileSystemLoader, select_autoescape, BaseLoader


class Action(ActionRuntime):

    required_config = """
        template:       # Filename or the text for a Jinja2 template
        single_item:    # If set to True produces the template a single item
                        # when no more input data is available
        """
    optional_config = """
    template_type:  "file"  # Can be file or text, if set to file, template
                            # is used as the filename for loading the template.
                            # If set to "text", the 'template' config values is
                            # used for the template text.
    """

    def on_start(self, config):
        if config["template_type"] == "file":
            env = Environment(
                loader=FileSystemLoader("."),
                autoescape=select_autoescape(["html", "xml"]),
                trim_blocks=True,
            )
            self.template = env.get_template(config["template"])
        else:
            self.template = Environment(
                loader=BaseLoader, trim_blocks=True
            ).from_string(config["template"])
        self.item_list = []

    def on_input(self, item):
        if self.config["single_item"]:
            self.put(self.template.render(item))
        else:
            self.item_list.append(item)

    def on_finish(self, reason):
        if self.item_list:
            self.put(self.template.render(items=self.item_list))
