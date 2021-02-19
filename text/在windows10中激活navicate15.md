参考：http://www.onebug.tech/2020/08/27/navicat%E6%BF%80%E6%B4%BB/

对网上找的exe文件的安全性存疑，于是想自己编译一下，顺便了解一下原理。上面的这篇文章对此帮助很大，但是忽略了一些细节处，在此进行补充。

# 1. 安装 visual studio 2019 community
![选择安装使用c++的桌面开发](https://user-images.githubusercontent.com/19688861/108449055-cd04ae00-729d-11eb-8ec0-e71990a6ead8.png)
上面这一步为 vcpkg 的编译提供了必须的文件。

![语言包中选择英语](https://user-images.githubusercontent.com/19688861/108449141-f0c7f400-729d-11eb-86bf-324931d46a43.png)

# 2. 安装并配置 vcpkg
```
$ git clone https://github.com/microsoft/vcpkg  --config "http.proxy=socks5://127.0.0.1:10808"
//  --config "http.proxy=socks5://127.0.0.1:10808" 为博主自己的代理配置，若没有可忽略。
$ cd vcpkg
$ bootstrap-vcpkg.bat -disableMetrics

$ set HTTP_PROXY=127.0.0.1:10809
$ set HTTPS_PROXY=127.0.0.1:10809
// 上面两行也是代理配置，若没有可忽略

$ vcpkg install capstone[x86]:x64-windows-static
$ vcpkg install keystone:x64-windows-static
$ vcpkg install openssl-windows:x64-windows-static
$ vcpkg install rapidjson:x64-windows-static

// 将 vcpkg 和 Visual Studio 集成
$ vcpkg integrate install
```

# 3. 下载配置源代码
```
$ git clone https://github.com/logiccodes/navicat-keygen-tools.git --config "http.proxy=socks5://127.0.0.1:10808"
$ cd navicat-keygen-tools/
$ git checkout windows
```
用 visual studio 打开 sln 文件。

![生成配置管理器x64](https://user-images.githubusercontent.com/19688861/108449958-523c9280-729f-11eb-9dff-1baaee88d72b.png)

生成失败。https://github.com/HeQuanX/navicat-keygen-tools/issues/24

# 免编译
下载 http://file.onebug.tech/?/%E8%BD%AF%E4%BB%B6%E5%88%86%E4%BA%AB/navicat-keygen-for-x64.zip

使用过程
https://github.com/HeQuanX/navicat-keygen-tools/blob/windows/doc/how-to-use.windows.zh-CN.md
