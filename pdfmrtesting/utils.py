
def determine_result(text: str) -> str:
    """Determines based on if a string is empty, if the PDF is Machine Readable or Needs OCR

    Args:
        text (str): the text extracted from the PDF

    Returns:
        str: A determination based on the string contents if "Machine Readable" or "Needs OCR"
    """
    
    if text == "":
        result = 'Needs OCR'
    elif text != "":
        result = 'Machine Readable'
    else:
        result = 'None'
    
    return result


# https://stackoverflow.com/questions/492519/timeout-on-a-function-call
import multiprocessing.pool
import functools

def timeout(max_timeout):
    """Timeout decorator, parameter in seconds."""
    def timeout_decorator(item):
        """Wrap the original function."""
        @functools.wraps(item)
        def func_wrapper(*args, **kwargs):
            """Closure for function."""
            pool = multiprocessing.pool.ThreadPool(processes=1)
            async_result = pool.apply_async(item, args, kwargs)
            # raises a TimeoutError if execution exceeds max_timeout
            return async_result.get(max_timeout)
        return func_wrapper
    return timeout_decorator