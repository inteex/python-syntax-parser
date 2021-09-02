import sys
from loaders import Loader


def withLoader(lodingMsg: str, loader: Loader, func, *args ):
    """
    show loading to user for function that take some time.
    """
    try:
        loader.text= lodingMsg
        loader.start()

        return func(*args)
    finally:
        loader.complete_text= '{}\t{}'.format(lodingMsg, "success")
        loader.stop()