import typer
import sqlite3

app = typer.Typer()


@app.command()
def add(amount: float, category: str):
    print(amount, category)


@app.command()
def remove(item: str):
    print(item)


@app.command()
def report(day: int, month: int):
    print(day, month)


if __name__ == "__main__":
    app()
