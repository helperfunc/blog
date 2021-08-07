直接在 https://thrift.apache.org/download 下载，然后
```
tar zxf thrift-0.14.2.tar.gz
cd thrift-0.14.2
./configure
```
会报错
`configure: error: cannot run C compiled programs`

用
```
./configure --host=arm
make
```

会出现
`error: '::malloc' has not been declared`

`error: '::realloc' has not been declared`

的错误。

解决
```
git clone https://github.com/apache/thrift.git
cd thrift
./bootstrap.sh
./configure
make
sudo make install
```
