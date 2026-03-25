import fastapi
import numpy
import requests


def collect_dependency_versions() -> dict[str, str]:
    return {
        "requests": requests.__version__,
        "numpy": numpy.__version__,
        "fastapi": fastapi.__version__,
    }
