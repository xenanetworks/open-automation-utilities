import typing as t
import asyncclick as ac
from click_backend import error_str
from click_commands import xena_cli
from cli_utils import format_error


async def cmd_main(cmd_str: str) -> t.Any:
    error_str.clear()
    args = cmd_str.split()
    try:
        result = await xena_cli.main(args=args, standalone_mode=False)
        if isinstance(result, int):
            result = error_str.err_str
    except ac.UsageError as error:
        result = format_error(error)
    return result


if __name__ == "__main__":
    xena_cli()
    # loop = asyncio.get_event_loop()
    # a = loop.run_until_complete(cmd_main("connect"))
    # print("S" + "#" * 100 + "\n" + str(a) + "\n" + "E" + "#" * 100)
