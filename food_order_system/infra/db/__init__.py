"""food_order_system model."""
import pkgutil
from pathlib import Path


def load_all_models() -> None:
    """Load all model from this folder."""
    package_dir = Path(__file__).resolve().parent
    modules = pkgutil.walk_packages(
        path=[str(package_dir)],
        prefix="food_order_system.db.",
    )
    for module in modules:
        __import__(module.name)  # noqa: WPS421
