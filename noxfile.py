import nox


@nox.session(python="3")
def lint(session):
    session.install("flake8", "pylint")
    session.run("flake8", "test/test_pysocks.py")
    session.run("pylint", "test/test_pysocks.py")


@nox.session(python=["2.7", "3.5", "3.6", "3.7", "3.8", "3.9"])
def test(session):
    session.install("-rrequirements_dev.txt")
    session.run("pytest", "test/")
