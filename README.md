
### 安装
require python verion >= 2.7

```
    pip install --user volc
```

如果已经安装volc包，则用下面命令升级即可
```
    pip install --upgrade volc
```


### AK/SK设置
- 在代码里显示调用VodService的方法set_ak/set_sk

- 在当前环境变量中分别设置 VCLOUD_ACCESSKEY="your ak"  VCLOUD_SECRETKEY = "your sk"

- json格式放在～/.vcloud/config中，格式为：{"ak":"your ak","sk":"your sk"}

以上优先级依次降低，建议在代码里显示设置，以便问题排查

### 地域Region设置
- 目前已开放三个地域设置，分别为
  ```
  - cn-north-1 (默认)
  - ap-singapore-1
  - us-east-1
  ```
- 默认为cn-north-1，如果需要调用其它地域服务，请在初始化函数getInstance中传入指定地域region，例如：
  ```
  vod_service = VodService('us-east-1')
  ```
- 注意：IAM模块目前只开放cn-north-1区域

### API

#### 获取sts2签名

[sign_sts2]()
```
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    # vod_service.set_ak('ak')
    # vod_service.set_sk('sk')

    statement = Statement.new_allow_statement(['iam:*'], [])
    inline_policy = Policy([statement])
    
    # 60 * 60 (设定有效期一小时)
    resp = vod_service.sign_sts2(inline_policy, 60 * 60)
    print(resp)

```
