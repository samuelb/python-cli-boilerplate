import sys

from cliff.app import App
from cliff.commandmanager import CommandManager


class MyApp(App):

    def __init__(self):
        super(MyApp, self).__init__(
            description='This is my awesome cli app',
            version='0.1',
            command_manager=CommandManager('myapp'),
            deferred_help=True,
        )

    def initialize_app(self, argv):
        self.LOG.debug('initialize_app')

    def prepare_to_run_command(self, cmd):
        self.LOG.debug('prepare_to_run_command %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        self.LOG.debug('clean_up %s', cmd.__class__.__name__)
        if err:
            self.LOG.debug('got an error: %s', err)

    def build_option_parser(self, description, version, argparse_kwargs=None):
        """Return an argparse option parser for this application.

        This extends the superclass with more global options.

        :param description: full description of the application
        :paramtype description: str
        :param version: version number for the application
        :paramtype version: str
        :param argparse_kwargs: extra keyword argument passed to the
                                ArgumentParser constructor
        :paramtype argparse_kwargs: dict
        """
        argparse_kwargs = argparse_kwargs or {}

        # It's sometimes handy to keep all arguments in a file.
        # Use ./cmd @filename, where filename contains the arguments in
        # --arg=value format, one per line.
        argparse_kwargs['fromfile_prefix_chars'] = '@'

        parser = super(MyApp, self).build_option_parser(
            description,
            version,
            argparse_kwargs
        )

        parser.add_argument(
            '--config',
            action='store',
            help='Specify the path to the config file.',
        )
        return parser


if __name__ == '__main__':
    app = MyApp()
    sys.exit(app.run(sys.argv[1:]))
