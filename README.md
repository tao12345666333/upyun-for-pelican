upyun-for-pelican
=================

###简介
[pelican](https://github.com/getpelican/pelican) 是一款基于python的静态博客生成工具，本程序可以方便的把生成的静态博客部署到[又拍云](https://www.upyun.com/index.html)上。演示地址：[upyun-for-pelican ](http://pelican-for-upyun.b0.upaiyun.com/)

###生成网站
```
    make html
    
    make serve   (进行本地预览)
    
```

###说明

*  可以下载代码中的**demo** 体验效果
```
cd demo/

python upyun-for-pelican.py

```

程序即可正常执行(在demo中已经添加了一个操作员的帐号)


*  可以自定义要上传的文件目录。在最下方的`local_dir` 中指定即可。Pelican默认的上传目录是 **output** 目录

###使用

1. 可以在 **pelicanconf.py** 文件中直接设置 `BUCKETNAME, USERNAME, PASSWORD` 参数，也可以直接在 `upyun-for-pelican.py`文件的最下方直接设置。

2. 执行
    ```
    python upyun-for-pelican.py 
    ```

3. 程序在 `Python 2.7` 环境下测试通过。

####其他说明

* 程序执行开始会有上传确认提示，输入`Y / y` 都可以继续上传。 
* 可以使用项目中的`pelicanconf.py`作为个人站点的配置文件。

* 截图 

![operation][1]

![upyun-for-pelican][2] 


  [1]: http://pelican-for-upyun.b0.upaiyun.com/img/screen.png
  [2]: http://moelove.qiniudn.com/2014-05-17%2013:20:56%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png