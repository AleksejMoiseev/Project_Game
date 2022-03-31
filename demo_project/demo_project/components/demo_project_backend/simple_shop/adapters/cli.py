import click


def create_cli(alembic_run_cmd, MessageBus):

    @click.group()
    def cli():
        pass

    @cli.command()
    @click.argument('alembic_args', nargs=-1, type=click.UNPROCESSED)
    def alembic(alembic_args):
        alembic_run_cmd(*alembic_args)

    @cli.command()
    def consumer():
        MessageBus.declare_scheme()
        MessageBus.consumer.run()

    return cli
