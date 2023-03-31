import sys
import logging


def error_info(error, error_detail: sys):
    _, _, trace_back = error_detail.exc_info()
    filename = trace_back.tb_frame.f_code.co_filename
    return f"""
    Error in {filename} at line {trace_back.tb_lineno}.
    Error: {error}
    """


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys) -> None:
        super().__init__(error_message)
        self.error_message = error_info(error_message, error_detail)

    def __str__(self) -> str:
        return self.error_message


if __name__ == "__main__":
    try:
        print(1 / 0)
    except Exception as e:
        raise CustomException(e, sys) from e
