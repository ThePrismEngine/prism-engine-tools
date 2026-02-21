import typer

engine_app = typer.Typer(
    name="engine",
    help="Управление движком и его версиями",
)

@engine_app.command("install")
def install(version: str = typer.Option("latest", help="Версия движка для установки"),
            self_compilation: bool = typer.Option(False, help="Компилировать из исходного кода самостоятельно, без готовых файлов из релиза")):
    pass

@engine_app.command("list")
def list_releases(
        installed: bool = typer.Option(True, help="Показать только установленные версии"),
        limit: int = typer.Option(10, help="Ограничить количество выводимых записей"),
):
    pass