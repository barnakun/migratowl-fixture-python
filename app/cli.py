import click


@click.command()
@click.option("--name", default="world")
def hello(name: str) -> None:
    click.echo(f"hello {name}")


if __name__ == "__main__":
    hello()
