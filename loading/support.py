from loaders import Loader


def withLoader(loadingMsg: str, loader: Loader, func, *args):
    """
    show loading to user for function that take some time.
    """
    try:
        loader.text = loadingMsg
        loader.start()

        return func(*args)
    finally:
        # short hand '{0:<30}{1}'.format(loadingMsg, "success")
        loader.complete_text = "{message:{fill}{align}{width}}success".format(
            message=loadingMsg, fill=".", align="<", width=30
        )
        loader.stop()
