# 服务器端
## 1. 在/media新建挂载的目的文件夹

列出所有未挂载硬盘
lsblk

在media下，新建要挂载的文件夹，和所有未挂载的硬盘一一对应。

## 2. 配置硬盘开机自动挂载
按下面的帖子
https://segmentfault.com/a/1190000022840767
将所有的新建的文件夹与硬盘对应写到 /etc/fstab 中
如
```
 /dev/sda /mnt/data ext4 defaults 0 0
```

## 3. 配置 nfs 服务器端
根据下面的帖子配置
https://github.com/twtrubiks/linux-note/tree/master/linux-nfs-server

唯一不同的是
/etc/exports 要写成以下的形式
```
文件夹 ip(re,sync,no_subtree_check,no_root_squash,crossmnt)
```
`no_root_squash` 让文件夹在客户端有访问权限，`crossmnt` 很重要，它使得客户端挂载的是服务器端挂载的硬盘，而非服务器端新建的文件夹。

![服务器端/etc/exports](https://user-images.githubusercontent.com/19688861/117541318-e9ff8080-b045-11eb-84f4-47b7e1159529.png)


## 3. 配置客户端
https://github.com/twtrubiks/linux-note/tree/master/linux-nfs-server
按以上帖子配置。
如果希望开机启动 nfs 挂载。可以在 /etc/exports 中填写挂载盘的根目录信息。
```
ip:/media/挂载根目录 /media/挂载根目录 nfs defaults,_netdev 0 0
```

## 4. 验证
重启服务器和客户端，依然有效。
