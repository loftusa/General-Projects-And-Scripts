VERSION = (0, 0, 1)

__version__ = ".".join(map(str, VERSION))

print(
    f"top-level __version__.py imported. Name of top level __version__.py: {__name__} "
)

