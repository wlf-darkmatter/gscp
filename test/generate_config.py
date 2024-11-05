"""
临时生成 docker-compose.yaml 的配置文件用于调试

python tmp/generate_config.py
"""

from pathlib import Path

path_test = Path(__file__).parent

num_host = 8
network_name = "cluster_net"

ip_segment = "90.90.1"
mask = 24
def generate_dockercompose_config():
    list_config = []
    for i in range(1, 1 + num_host):
        config_txt = f"""
  cluster-{i}:
    image: harbor.x-contion.top:500/x-contion/base_ubuntu:zh
    container_name: cluster-{i}
    entrypoint: ["/sbin/sshd", "-D"]
    networks:
      {network_name}:
        ipv4_address: {ip_segment}.{i}

"""
        list_config.append(config_txt)

    with open(path_test.parent.joinpath("docker-compose.yaml"), "w") as f:
        f.write("version: '3.9'\n")
        f.write("services:\n")
        for i in list_config:
            f.write(i)
        config_network = f"""
networks:
  {network_name}:
    driver: "bridge"
    ipam:
      # driver: default
      config:
        - subnet: \"{ip_segment}.0/{mask}\"
          ip_range: \"{ip_segment}.0/{mask}\"
          gateway: \"{ip_segment}.254\"
        """
        f.write(config_network)


def generate_test_config():
    test_dict = {
        "default_user": "root",
        "default_passwd": "123456",
        "group": [],
    }
    for i in range(num_host):
        test_dict["group"].append(
            {
                "ip": f"{ip_segment}.{i+1}",
            }
        )
    import yaml

    path_generate = path_test.parent.joinpath("generate")
    path_generate.mkdir(exist_ok=True)
    with open(path_generate.joinpath("test-ipconfig.yaml"), "w") as f:
        yaml.dump(test_dict, f)


if __name__ == "__main__":
    generate_dockercompose_config()
    generate_test_config()
