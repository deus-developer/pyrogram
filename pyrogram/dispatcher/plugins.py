import logging
from importlib import import_module
from pathlib import Path
from typing import Any

from pyrogram.dispatcher.dispatcher import Dispatcher
from pyrogram.handlers import Handler

log = logging.getLogger(__name__)


def load_plugins(
    dispatcher: Dispatcher,
    plugins: dict[str, Any] | None,
) -> None:
    if plugins is None:
        return

    shadow = plugins.copy()

    for option in ["include", "exclude"]:
        if shadow.get(option, []):
            shadow[option] = [
                (i.split()[0], i.split()[1:] or None) for i in shadow[option]
            ]

    if shadow.get("enabled", True):
        root = shadow["root"]
        include = shadow.get("include", [])
        exclude = shadow.get("exclude", [])

        count = 0

        if not include:
            for path in sorted(Path(root.replace(".", "/")).rglob("*.py")):
                module_path = ".".join((*path.parent.parts, path.stem))
                module = import_module(module_path)

                for name in vars(module):
                    # noinspection PyBroadException
                    try:
                        for handler, group in getattr(module, name).handlers:
                            if isinstance(handler, Handler) and isinstance(
                                group,
                                int,
                            ):
                                dispatcher.add_handler(handler, group)

                                log.info(
                                    f'[LOAD] {type(handler).__name__}("{name}") in group {group} from "{module_path}"',
                                )

                                count += 1
                    except Exception:
                        pass
        else:
            for path, handlers in include:
                module_path = root + "." + path
                warn_non_existent_functions = True

                try:
                    module = import_module(module_path)
                except ImportError:
                    log.warning(
                        '[LOAD] Ignoring non-existent module "%s"',
                        module_path,
                    )
                    continue

                if "__path__" in dir(module):
                    log.warning(
                        '[LOAD] Ignoring namespace "%s"',
                        module_path,
                    )
                    continue

                if handlers is None:
                    handlers = vars(module).keys()
                    warn_non_existent_functions = False

                for name in handlers:
                    # noinspection PyBroadException
                    try:
                        for handler, group in getattr(module, name).handlers:
                            if isinstance(handler, Handler) and isinstance(
                                group,
                                int,
                            ):
                                dispatcher.add_handler(handler, group)

                                log.info(
                                    f'[LOAD] {type(handler).__name__}("{name}") in group {group} from "{module_path}"',
                                )

                                count += 1
                    except Exception:
                        if warn_non_existent_functions:
                            log.warning(
                                f'[LOAD] Ignoring non-existent function "{name}" from "{module_path}"',
                            )

        if exclude:
            for path, handlers in exclude:
                module_path = root + "." + path
                warn_non_existent_functions = True

                try:
                    module = import_module(module_path)
                except ImportError:
                    log.warning(
                        '[UNLOAD] Ignoring non-existent module "%s"',
                        module_path,
                    )
                    continue

                if "__path__" in dir(module):
                    log.warning(
                        '[UNLOAD] Ignoring namespace "%s"',
                        module_path,
                    )
                    continue

                if handlers is None:
                    handlers = vars(module).keys()
                    warn_non_existent_functions = False

                for name in handlers:
                    # noinspection PyBroadException
                    try:
                        for handler, group in getattr(module, name).handlers:
                            if isinstance(handler, Handler) and isinstance(
                                group,
                                int,
                            ):
                                dispatcher.remove_handler(handler, group)

                                log.info(
                                    f'[UNLOAD] {type(handler).__name__}("{name}") from group {group} in "{module_path}"',
                                )

                                count -= 1
                    except Exception:
                        if warn_non_existent_functions:
                            log.warning(
                                f'[UNLOAD] Ignoring non-existent function "{name}" from "{module_path}"',
                            )

        if count > 0:
            log.info(
                'Successfully loaded {} plugin{} from "{}"'.format(
                    count,
                    "s" if count > 1 else "",
                    root,
                ),
            )
            return
        log.warning('No plugin loaded from "%s"', root)
        return
    return
