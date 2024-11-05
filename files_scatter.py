"""
Author: wanglingfeng
Support:
Version: 0.0.1
Date: 2024-10-18
"""

from typing import Union
import argparse
import copy
import yaml
from pathlib import Path
import traceback
from matplotlib import pyplot as plt
import seaborn as sns

parser = argparse.ArgumentParser("局域网内服务器集群文件自动分发脚本")

parser.add_argument("-r", "--recursive")

parser.add_argument(
    "-c",
    "--config",
    required=True,
    type=str,
    help="加载的路径为 CONFIG 的 yaml 格式的配置文件，含有服务器集群的账号密码、IP信息",
)
me_group = parser.add_mutually_exclusive_group()
me_group.add_argument("--no-check", action="store_true", help="不检测链路状态")
me_group.add_argument("--recheck", action="store_true", help="重新检查链路状态")

default_config = {
    "default_user": "root",
    "default_passwd": "empty_passwd",
    "group": [
        {
            "ip": "0.0.0.0",
            "user": "root",
            "passwd": "passwd",
        }
    ],
}


class ServerGropu_trans:
    pass

    def __init__(self, path_config: Union[Path, str]) -> None:
        pass
        self.path_config = Path(path_config)
        self.config = self.load_config()
        pass
        self.connect_ssh()

    def connect_ssh(self):
        print("trying to connect host")
        self.dict_ssh_client = {}
        pass

    def load_config(self) -> dict:

        if self.path_config.is_file():
            assert_txt = "The suffix of config file must be '.yaml' or '.yml' "
            assert self.path_config.suffix in [".yaml", "yml"], assert_txt

            with open(self.path_config, "r") as f:
                config = yaml.load(f, yaml.SafeLoader)
            copy_default_dict = copy.deepcopy(default_config)
            copy_default_dict.update(config)
            return copy_default_dict
        else:
            raise FileNotFoundError(f"The path of [{self.path_config}] is not exist.")

    def calc_sha256(self):
        pass


if __name__ == "__main__":
    args = parser.parse_args()
    arg_path_config: str = args.config
    s = ServerGropu_trans(arg_path_config)
