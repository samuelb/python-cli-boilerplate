import logging

from cliff.command import Command


class NoImplemented(Command):
    "this command is not yet implemented"
    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.log.info('This feature is not implemented yet')


class Debug(Command):
    "this command is not yet implemented"
    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        print(self.app.options)
        print(self.app_args)
