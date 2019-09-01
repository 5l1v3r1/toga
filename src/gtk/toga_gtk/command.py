from toga import Icon


class Command:
    """ Command `native` property is a list of native widgets associated with the command.
    Native widgets can be both Gtk.ToolButton and Gio.SimpleAction.
    """
    def __init__(self, interface):
        self.interface = interface

        if self.interface.icon_id:
            self.icon = Icon.load(self.interface.icon_id)
        else:
            self.icon = None

        self.native = []

    def set_enabled(self, value):
        enabled = self.interface.enabled
        for widget in self.native:
            try:
                widget.set_sensitive(enabled)
            except AttributeError:
                widget.set_enabled(enabled)
