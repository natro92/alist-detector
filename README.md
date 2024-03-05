# alist-detector

批量查看是否允许访问，并且支持挂载。

## 使用方法

由于使用了 `asyncio.WindowsSelectorEventLoopPolicy()` 似乎只能Windows使用，如果Linux使用可以删除试一试。

```shell
pip install -r requirements.txt
```

在项目根目录下的ip.txt加入需要扫描的IP地址（一行一个），需要满足下列格式其中之一，

```angular2html
https://example1.com
111.11.11.1:22222
alist.example2.com
```

```shell
python alist-detector.py
```

## 接口使用

- `/api/public/settings` 查看信息，主要获取的参数为 `"allow_mounted": "false"` 参数，来判断是否可以进行挂载处理。
- `/api/me` 查看是否开放了guest用户权限。