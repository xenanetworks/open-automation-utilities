import asyncclick as ac
from xoa_utils.clicks import click_backend as cb


cs = {"help_option_names": ["-h", "--help"]}


@ac.group(cls=cb.XenaGroup)
def xoa_util():
    pass
