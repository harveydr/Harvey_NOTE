# Docker镜像命令

获取镜像
```
docker pull NAME[:TAG]
docker pull ubuntu:14.04
如果不显式指定TAG，则默认会选择latest标签：
docker pull ubuntu
```
从非官方仓库获取镜像
```
docker pull hub.c.163.com/public/ubuntu:14.04
```
查看镜像
```
docker images
docker images -afq...
```
使用tag命令添加镜像标签
```
docker tag ubuntu:latest myubuntu:latest
```
使用inspect命令查看详细信息
```
docker inspect ubuntu:14.04
docker inspect -f {{".Architecture}}  # 只返回其中的一项内容
```
使用history命令查看镜像历史（各个层的具体内容）
```
docker history ubuntu:14.04
```
搜寻镜像
```
docker search --audomated -s 3 nginx
```
删除镜像
```
docker rmi myubuntu:latest # 使用标签删除镜像
docker rmi 32dvr32 # 使用镜像ID删除镜像（会删除原来的镜像）
docker rmi -f ubuntu:14.04 # 强行删除镜像（不推荐）
```
批量删除所有镜像
```
docker rmi `docker images -q`
```

创建镜像（基于已有容器创建镜像）
```
docker commit [OPTIONS]CONTAINER[REPOSITORY[: TAG]]
docker run -it ubuntu:14.04  /bin/bash # 记住容器的ID为a925cb
docker commit -m "Added a new filw" -a "Docker Newbee" a925cb test:0.1    # 返回新镜像的ID信息
docker images
# REPOSITORY    TAG    IMAGE ID    CREATED    VIRTUAL SIZE
# test     0.1     jk4324j543     4 seconds ago     199MB
```
基于本地模板导入
```
docker import[OPTIONS] file | URL | -[REPOSITORY[: TAG]]
cat ubuntu-14.04-x86_64-minimal.tar.gz | docker import - ubuntu:14.04
docker images # 查看已导入的镜像
```
存出镜像
```
docker save -o ubuntu_14.04.tar ubuntu:14.04
```
载入镜像
```
docker load --input ubuntu_14.04.tar  或
docker load < ubuntu_14.04.tar
```
上传镜像
```
docker push NAME[: TAG] | [REGISTRY_HOST[:REGISTRY_PORT]/]NAME[:TAG]  # 默认上传到Docker Hub官网仓库（第一次上传时，会提示输入登录信息或进行注册）
docker tag test:latest  user/test:latest
docker push user/test:latest
```
--------------

# Docker容器命令

查看容器
```
docker ps -aq
```
创建容器
```
docker create -it ubuntu:latest  # 创建的容器处于停止状态，可以使用docker start命令来启动它
```
启动容器
```
docker start af323gc
```
新建并启动容器
```
docker run ubuntu /bin/echo "Hello, Ubuntu"  # 等价于执行 docker create 后再执行 docker start 命令，若本地不从在相应镜像，会从共有仓库下载
# 下面的命令启动一个bash终端，允许用户进行交互：
docker run -it ubuntu:14.04  /bin/bash
root@afjdfk323jfd:/#  (返回的结果)  // 用户可以按Ctrl + d或输入exit来推出容器
```
守护态运行
```
// 更多时候，需要让Docker容器在后台以守护态运行，此时可以通过添加-d参数来实现：
docker run -d ubuntu /bin/sh -c "while true;do echo hello world;sleep 1;done"  // 返回一个唯一的容器ID
docker ps
docker logs ce32gd32  // 获取容器的输出信息，而不是容器的信息
```
终止容器
```
docker stop ce32dgs2
docker kill ce32dgs2  // 此命令会强行发送SIGKILL信号来强行终止容器
// 处于终止状态的容器，可以用如下方式重新启动
docker start ce32dgs2
docker restart ce32dgs2  // 先终止容器，再重新启动
```
进入容器（attach命令）
```
docker attach [--detach-keys[=[]]] [--no-stdin] [--sigproxy[=true]] CONTAINER
docker run -itd ubuntu
docker ps // 返回的其中项：NAME: nostalgic_hypatia
docker attach nostalgic_hypatia
// 但是使用attach命令有时候并不方便。当多个窗口同时使用attach命令连到同一个容器的时候，所有窗口都会同步显示。
// 当某个窗口因命令阻塞时，其他窗口也无法执行操作了。
```
进入容器（exec命令）
```
docker exec [-d | -detach] [--detach-keys[=[]]] [-i | --interactive] [--privileged] [-t | --tty] [-u | --user[=USER]] CONTAINER COMMAND [ARG...]
docker exec -it 234edg3 /bin/bash  // 进入刚刚创建的容器中，并启动一个bash
// 通过指定-it参数来保持标准输入打开，并且分配一个伪终端。通过exec命令对容器执行操作是最为推荐的方式。
```
进入容器（nsenter工具）
```

```
删除容器
```
docker rm ce323fd
docker rm -f ce323fd  // 强行删除容器：Docker会先发送SIGKILL信号给容器，终止其中的应用，之后强行删除。
```
批量删除所有容器
```
docker rm `docker ps -qa`
```

