from __future__ import annotations
from asyncclick.shell_completion import ShellComplete, CompletionItem
from asyncclick import BaseCommand
import typing as t
from click_commands import xoa_utils
from click_entry import cmd_main
from hub import HubManager
from cli_utils import ReadConfig, run_coroutine_as_sync
import asyncssh
import os

if t.TYPE_CHECKING:
    from asyncssh.process import SSHServerProcess
    from asyncssh.editor import SSHLineEditorChannel


class AutoCompleter(ShellComplete):
    """
    Extends ShellComplete. https://click.palletsprojects.com/en/8.1.x/shell-completion/
    """

    def __init__(
        self,
        cli: BaseCommand,
        ctx_args: dict[str, t.Any],
        prog_name: str,
        complete_var: str,
        args_raw: list[str],
    ) -> None:
        super().__init__(cli, ctx_args, prog_name, complete_var)
        self.args_raw = args_raw

    def get_completion_args(self) -> tuple[list[str], str]:
        """Use the self.args to return a tuple of ``args, incomplete``."""
        args = self.args_raw[:-1] if self.args_raw else []
        incomplete = str(self.args_raw[-1]) if self.args_raw else ""
        return args, incomplete

    def format_completion(self, item: CompletionItem) -> str:
        """Format a completion item into the form recognized by the
        shell script.

        :param item: Completion item to format.
        """
        return f"{item.value}"

    async def complete(self) -> str:
        """Produce the completion data to send back to the shell.

        By default this calls :meth:`get_completion_args`, gets the
        completions, then calls :meth:`format_completion` for each
        completion.
        """
        args, incomplete = self.get_completion_args()
        completions = await self.get_completions(args, incomplete)
        out = [self.format_completion(item) for item in completions]
        return "\t".join(out)


async def shell_complete(cli: BaseCommand, args_raw: list[str]) -> str:
    """Perform shell completion for the given CLI program.
    Mimic of :func: asyncclick.shell_completion.shell_complete.

    :param cli: Command being called.

    :return: String after completion
    """
    prog_name = "xoa_utils"
    ctx_args = {}
    completer = AutoCompleter(cli, ctx_args, prog_name, "", args_raw)
    completed = await completer.complete()
    return completed


class CmdWorker:
    def __init__(
        self,
        process: "SSHServerProcess",
        prompt: str = "xena:> ",
    ) -> None:
        self.process: "SSHServerProcess" = process
        self.prompt: str = prompt
        self.channel: "SSHLineEditorChannel" = self.process.channel  # type: ignore
        self.hub_manager: t.Optional["HubManager"] = None
        self.hub_enable: bool = False
        self.hub_msg_list = []
        self.register_keys()

    def autocomplete(self, line: str, pos: int) -> t.Tuple[str, int]:
        if not line:
            return line, pos
        args_raw = line.split()
        coro = shell_complete(xoa_utils, args_raw)
        completed = str(run_coroutine_as_sync(coro))
        if not completed:
            pass
        elif completed.startswith("-"):
            self.write(f"{line}\n{completed}\n\n{self.prompt}")
        elif args_raw and completed.startswith(args_raw[-1]):
            new_l = args_raw[:-1] + [completed]
            line = " ".join(new_l)
        else:
            line = completed
        pos = len(line)
        return line, pos

    def register_keys(self) -> None:
        self.channel.register_key("\t", self.autocomplete)

    def finish(self) -> None:
        self.process.exit(0)

    def write(self, msg: str) -> None:
        self.process.stdout.write(msg)

    def put_record(self, request: str, response: str) -> None:
        if self.hub_enable and self.hub_manager:
            self.hub_msg_list.append((os.getpid(), request, response))  # type: ignore

    async def run(self) -> None:
        self.connect()
        self.write(f"\n{self.prompt}")
        while not self.process.stdin.at_eof():
            try:
                request = (await self.process.stdin.readline()).strip()
                response = await self.dispatch(request)
                self.write(f"{response}\n{self.prompt}")
                self.put_record(request, response)
            except asyncssh.TerminalSizeChanged:
                pass

    def connect(self) -> None:
        config = ReadConfig()
        self.hub_enable = config.hub_enabled
        if config.hub_enabled:
            self.hub_manager = HubManager(
                address=(config.hub_host, config.hub_port), authkey=b""
            )
            self.hub_manager.connect()
            self.hub_msg_list = self.hub_manager.get_list()  # type: ignore

    async def dispatch(self, msg: str) -> str:
        if msg.lower() == "exit":
            self.finish()
        return await cmd_main(msg)
