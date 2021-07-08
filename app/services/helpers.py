from flask import current_app


session = current_app.db.session


def add_commit(model) -> None:
    session.add(model)
    session.commit()


def delete_commit(model) -> None:
    session.delete(model)
    session.commit()
