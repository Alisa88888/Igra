from .settings import settings


def part(width: int | float, height: int | float) -> tuple[int, int]:
    return round(settings.width * width), round(settings.height * height) 

