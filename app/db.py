from sqlalchemy import create_engine


def answer() -> int:
    engine = create_engine("sqlite://")
    return engine.execute("select 42").scalar()
