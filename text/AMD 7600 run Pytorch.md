[https://rocm.docs.amd.com/projects/install-on-linux/en/latest/tutorial/install-overview.html](https://rocm.docs.amd.com/projects/install-on-linux/en/develop/how-to/3rd-party/pytorch-install.html)https://rocm.docs.amd.com/projects/install-on-linux/en/develop/how-to/3rd-party/pytorch-install.html

Using a Docker image with PyTorch pre-installed
https://zhuanlan.zhihu.com/p/347643668
Docker 国内镜像

https://github.com/ROCm/ROCm/issues/2536

```
$ docker pull rocm/pytorch:latest

$ docker run -it -v /home/username:/username --cap-add=SYS_PTRACE --security-opt seccomp=unconfined \
--device=/dev/kfd --device=/dev/dri --group-add video \
--ipc=host --shm-size 8G rocm/pytorch:latest


root@a4103344870e:/# export HSA_OVERRIDE_GFX_VERSION=11.0.0
root@a4103344870e:/hui# python -c "import torch; x = torch.ones(1,2).cuda(); print(x); print('sum {}'.format(torch.sum(x)))"
```

