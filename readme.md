
# 生成临时调试配置文件

临时生成 docker-compose.yaml 的配置文件用于调试
```
python tmp/generate_config.py
```

会在`generate`下生成一个 `test-ipconfig.yaml` 文件，可以用于调试，且该文件符合配置文件的要求

> 如果要测试，可以把 `generate/test-ipconfig.yaml` 拖到 `test/test-ipconfig.yaml` 下

## 创建用于调试的容器

运行上一步的python的脚本后，会产生一个叫做`docker-compose.yaml`的文件，直接运行
```bash
docker-compose up -d
```
就可以启动对应数量的容器了

## 网络诊断命令

```bash
#* 查看路由表
iptables -t nat -nL
```