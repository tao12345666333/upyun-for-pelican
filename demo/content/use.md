Title: How to use
Date: 2014-05-16
Category: python
Tags:  Use
 
------

###说明

*  程序使用了又拍云的[官方SDK](https://github.com/upyun/python-sdk) 需要先安装 upyun
```
pip install upyun
```

*  本程序[开源在gitcafe上](https://gitcafe.com/BruceZhang/pelican-upyun-for-UPYUN)

*  可以自定义要上传的文件目录。在最下方的`local_dir` 中指定即可。Pelican默认的上传目录是 output 目录

###使用

1. 可以在 **pelicanconf.py** 文件中直接设置 `BUCKETNAME, USERNAME, PASSWORD` 参数（这些参数的使用大写命名格式也是为了符合*pelicanconf.py*中的习惯），也可以直接在 `upyun-for-pelican.py`文件的最下方直接设置。

2. 执行
    ```
    python upyun-for-pelican.py 
    ```

3. 程序在 `Python 2.7` 环境下测试通过。

####其他说明

* 程序执行开始会有上传确认提示，输入`Y / y` 都可以继续上传。 
* 可以使用项目中的`pelicanconf.py`作为个人站点的配置文件。