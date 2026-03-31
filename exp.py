import typer
import sqlite3

app = typer.Typer()


@app.command()
def add(amount: float):
    print(amount)


@app.command()
def remove(item: str):
    print(item)


if __name__ == "__main__":
    app()
