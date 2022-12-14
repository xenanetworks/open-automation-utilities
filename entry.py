import asyncssh
import asyncio
import asyncclick
import sys
import os
from cli_utils import ReadConfig
from hub import Hub
from xena_ssh_server import XenaSSHServer
from cmd_worker import CmdWorker


class XenaSSHCLIHandle:
    @classmethod
    async def handle_client(cls, process: asyncssh.SSHServerProcess) -> None:
        out = process.stdout
        setattr(out, "flush", out._chan._flush_send_buf)
        # patch the flush() method since it doesn't exist.
        asyncclick.echo(
            f"Welcome to Xena SSH server, {process.get_extra_info('username')}!",
            file=out,
        )
        worker = CmdWorker(process)
        await worker.run()


async def start_server(config: ReadConfig) -> None:
    Hub.check_hub_process(config)
    print(f"(PID: {os.getpid()}) Xena SSH running on 0.0.0.0:{config.connection_port}")
    await asyncssh.create_server(
        XenaSSHServer,
        "0.0.0.0",
        config.connection_port,
        server_host_keys=[config.connection_host_keys],
        process_factory=XenaSSHCLIHandle.handle_client,
    )


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    config = ReadConfig()
    try:
        loop.run_until_complete(start_server(config))
        loop.run_forever()
    except (OSError, asyncssh.Error) as exc:
        sys.exit(f"Error starting server: <{type(str(exc))}> {exc}")
    except KeyboardInterrupt:
        os.remove(config.hub_pid_path)
