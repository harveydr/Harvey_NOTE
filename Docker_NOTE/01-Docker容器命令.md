- 查看容器
```
docker ps -aq
```
- 创建容器
```
docker create -it ubuntu:latest # 创建的容器处于停止状态，可以使用docker start命令来启动它
```
- 启动容器
```
docker start af323gc
```
- 新建并启动容器
```bash
docker run ubuntu /bin/echo "Hello, Ubuntu"  # 等价于执行 docker create 后再执行 docker start 命令，若本地不从在相应镜像，会从共有仓库下载
# 下面的命令启动一个bash终端，允许用户进行交互：
docker run -it ubuntu:14.04  /bin/bash
root@afjdfk323jfd:/#  (返回的结果)  // 用户可以按Ctrl + d或输入exit来推出容器
```
- 守护态运行
```bash
// 更多时候，需要让Docker容器在后台以守护态运行，此时可以通过添加-d参数来实现：
docker run -d ubuntu /bin/sh -c "while true;do echo hello world;sleep 1;done"  // 返回一个唯一的容器ID
docker ps
docker logs ce32gd32  // 获取容器的输出信息，而不是容器的信息
```

- 终止容器
```
docker stop ce32dgs2
docker kill ce32dgs2  // 此命令会强行发送SIGKILL信号来强行终止容器
// 处于终止状态的容器，可以用如下方式重新启动
docker start ce32dgs2
docker restart ce32dgs2  // 先终止容器，再重新启动
```
- 进入容器（attach命令）
```
docker attach [--detach-keys[=[]]] [--no-stdin] [--sigproxy[=true]] CONTAINER
    docker run -itd ubuntu
    docker ps // 返回的其中项：NAME: nostalgic_hypatia
    docker attach nostalgic_hypatia
    // 但是使用attach命令有时候并不方便。当多个窗口同时使用attach命令连到同一个容器的时候，所有窗口都会同步显示。
    // 当某个窗口因命令阻塞时，其他窗口也无法执行操作了。
```
- 进入容器（exec命令）
```
docker exec [-d | -detach] [--detach-keys[=[]]] [-i | --interactive] [--privileged] [-t | --tty] [-u | --user[=USER]] CONTAINER COMMAND [ARG...]
docker exec -it 234edg3 /bin/bash  // 进入刚刚创建的容器中，并启动一个bash
// 通过指定-it参数来保持标准输入打开，并且分配一个伪终端。通过exec命令对容器执行操作是最为推荐的方式。
```
