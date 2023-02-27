import asyncssh
import asyncio
import asyncclick
import sys
import os
from xoa_utils.clis import ReadConfig
from xoa_utils.hub import Hub
from xoa_utils.ssh_server import XenaSSHServer
from xoa_utils.cmds import CmdWorker
import os
import sys
import codecs
import os.path

class XenaSSHCLIHandle:
    def __init__(self, config: ReadConfig, version: str) -> None:
        self.config = config
        self.version = version

    async def handle_client(self, process: asyncssh.SSHServerProcess) -> None:
        out = process.stdout
        setattr(out, "flush", out._chan._flush_send_buf)
        # patch the flush() method since it doesn't exist.
        asyncclick.echo(
            f"Hello {process.get_extra_info('username')}, welcome to Xena OpenAutomation Utilities SSH Service ({self.version}).",
            file=out,
        )
        worker = CmdWorker(process)
        await worker.run(self.config)


async def start_server(config: ReadConfig) -> None:
    Hub.check_hub_process(config)
    version = get_version("__init__.py")
    print(
        f"(PID: {os.getpid()}) Xena OpenAutomation Utilities SSH Service ({version}) running on 0.0.0.0:{config.conn_port}"
    )
    await asyncssh.create_server(
        XenaSSHServer,
        "0.0.0.0",
        config.conn_port,
        server_host_keys=[config.conn_host_keys],
        process_factory=XenaSSHCLIHandle(config, version).handle_client,
    )

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()
    
def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

def main() -> None:
    loop = asyncio.get_event_loop()
    argv = (sys.argv[1],) if len(sys.argv) >= 2 else tuple()
    config = ReadConfig(*argv)
    try:
        loop.run_until_complete(start_server(config))
        loop.run_forever()
    except (OSError, asyncssh.Error) as exc:
        sys.exit(f"Error starting server: <{type(str(exc))}> {exc}")
    except KeyboardInterrupt:
        os.remove(config.hub_pid_path)


if __name__ == "__main__":
    main()
