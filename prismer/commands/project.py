import typer

project_app = typer.Typer(
    name="project",
    help="Операции с проектами",
)

@project_app.command("create")
def create(name: str, template: str = "default"):
    pass


@project_app.command("build")
def build(config: str = "debug"):
    pass