```
2021-08-08 07:28:41,578 ERROR [thrift-worker-5] client.AsyncRequestFutureImpl: Cannot get replica 0 location for {"totalColumns":1,"row":"8210000000000000:1628407721574157","families":{"cf":[{"qualifier":"from_user_id","vlen":16,"tag":[],"timestamp":"9223372036854775807"}]},"ts":"9223372036854775807"}
2021-08-08 07:28:41,578 WARN  [thrift-worker-5] thrift.ThriftHBaseServiceHandler: Failed 1 action: test_twitter_followers: 1 time, servers with issues: null
org.apache.hadoop.hbase.client.RetriesExhaustedWithDetailsException: Failed 1 action: test_twitter_followers: 1 time, servers with issues: null
        at org.apache.hadoop.hbase.client.BatchErrors.makeException(BatchErrors.java:54)
        at org.apache.hadoop.hbase.client.AsyncRequestFutureImpl.getErrors(AsyncRequestFutureImpl.java:1196)
        at org.apache.hadoop.hbase.client.HTable.batch(HTable.java:451)
        at org.apache.hadoop.hbase.client.HTable.put(HTable.java:549)
        at org.apache.hadoop.hbase.thrift.ThriftHBaseServiceHandler.mutateRowsTs(ThriftHBaseServiceHandler.java:800)
        at org.apache.hadoop.hbase.thrift.ThriftHBaseServiceHandler.mutateRows(ThriftHBaseServiceHandler.java:734)
        at sun.reflect.GeneratedMethodAccessor6.invoke(Unknown Source)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.lang.reflect.Method.invoke(Method.java:498)
        at org.apache.hadoop.hbase.thrift.HbaseHandlerMetricsProxy.invoke(HbaseHandlerMetricsProxy.java:72)
        at com.sun.proxy.$Proxy10.mutateRows(Unknown Source)
        at org.apache.hadoop.hbase.thrift.generated.Hbase$Processor$mutateRows.getResult(Hbase.java:4462)
        at org.apache.hadoop.hbase.thrift.generated.Hbase$Processor$mutateRows.getResult(Hbase.java:4441)
        at org.apache.thrift.ProcessFunction.process(ProcessFunction.java:38)
        at org.apache.thrift.TBaseProcessor.process(TBaseProcessor.java:38)
        at org.apache.hadoop.hbase.thrift.TBoundedThreadPoolServer$ClientConnnection.run(TBoundedThreadPoolServer.java:297)
        at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
        at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
```

```
File "/vagrant/django_hbase/models/hbase_models.py", line 151, in create
    instance.save(batch=batch)
  File "/vagrant/django_hbase/models/hbase_models.py", line 139, in save
    table.put(self.row_key, row_data)
  File "/usr/local/lib/python3.6/dist-packages/happybase/table.py", line 464, in put
    batch.put(row, data)
  File "/usr/local/lib/python3.6/dist-packages/happybase/batch.py", line 137, in __exit__
    self.send()
  File "/usr/local/lib/python3.6/dist-packages/happybase/batch.py", line 60, in send
    self._table.connection.client.mutateRows(self._table.name, bms, {})
  File "/usr/local/lib/python3.6/dist-packages/thriftpy2/thrift.py", line 219, in _req
    return self._recv(_api)
  File "/usr/local/lib/python3.6/dist-packages/thriftpy2/thrift.py", line 251, in _recv
    raise v
Hbase_thrift.IOError: IOError(message=b'org.apache.hadoop.hbase.client.RetriesExhaustedWithDetailsException: Failed 1 action: test_twitter_followers: 1 time, servers with issues: null\n\tat org.apache.hadoop.hbase.client.BatchErrors.makeException(BatchErrors.java:54)\n\tat org.apache.hadoop.hbase.client.AsyncRequestFutureImpl.getErrors(AsyncRequestFutureImpl.java:1196)\n\tat org.apache.hadoop.hbase.client.HTable.batch(HTable.java:451)\n\tat org.apache.hadoop.hbase.client.HTable.put(HTable.java:549)\n\tat org.apache.hadoop.hbase.thrift.ThriftHBaseServiceHandler.mutateRowsTs(ThriftHBaseServiceHandler.java:800)\n\tat org.apache.hadoop.hbase.thrift.ThriftHBaseServiceHandler.mutateRows(ThriftHBaseServiceHandler.java:734)\n\tat sun.reflect.GeneratedMethodAccessor6.invoke(Unknown Source)\n\tat sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)\n\tat java.lang.reflect.Method.invoke(Method.java:498)\n\tat org.apache.hadoop.hbase.thrift.HbaseHandlerMetricsProxy.invoke(HbaseHandlerMetricsProxy.java:72)\n\tat com.sun.proxy.$Proxy10.mutateRows(Unknown Source)\n\tat org.apache.hadoop.hbase.thrift.generated.Hbase$Processor$mutateRows.getResult(Hbase.java:4462)\n\tat org.apache.hadoop.hbase.thrift.generated.Hbase$Processor$mutateRows.getResult(Hbase.java:4441)\n\tat org.apache.thrift.ProcessFunction.process(ProcessFunction.java:38)\n\tat org.apache.thrift.TBaseProcessor.process(TBaseProcessor.java:38)\n\tat org.apache.hadoop.hbase.thrift.TBoundedThreadPoolServer$ClientConnnection.run(TBoundedThreadPoolServer.java:297)\n\tat java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)\n\tat java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)\n\tat java.lang.Thread.run(Thread.java:748)\n')
```

以上提示是 hbase 未建表就 insert 数据的错误。
