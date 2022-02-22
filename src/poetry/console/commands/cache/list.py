import os

from typing import Optional

from poetry.console.commands.command import Command


class CacheListCommand(Command):

    name = "cache list"
    description = "List Poetry's caches."

    def handle(self) -> Optional[int]:
        from poetry.locations import REPOSITORY_CACHE_DIR

        if os.path.exists(str(REPOSITORY_CACHE_DIR)):
            if caches := sorted(REPOSITORY_CACHE_DIR.iterdir()):
                for cache in caches:
                    self.line(f"<info>{cache.name}</>")
                return 0

        self.line_error("<warning>No caches found</>")
        return None
