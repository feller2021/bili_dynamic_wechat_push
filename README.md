#### 介绍

这是一个关于哔哩哔哩动态推送到微信通知的项目。项目来自[WBDmonitor](https://github.com/Bla1n/WBDmonitor)

是[weibo_dynamic_wechat_push](https://github.com/liurenjie520/weibo_dynamic_wechat_push) 项目的扩展。

该项目的推送接口已经废掉，待找到能满足文本+图片的微信推送接口再维护。

#### 软件架构
Python

#### 灵感来源

为了上班的时候，再不打开哔哩哔哩的情况下，使用微信看小偶像的哔哩哔哩动态，包括文字、图片

#### 已实现的功能

1. 推送原创哔哩哔哩动态+原创图片动态
2. 推送卷发哔哩哔哩动态+卷发图片动态
3. 纯文字哔哩哔哩动态+纯图片哔哩哔哩动态

#### 安装教程

1. 先设置你要关注的人的哔哩哔哩id。在代码里替换掉就好。
2. 先在py编译器里面手动运行一下，生成txt内容，把txt最初始数据内容复制到这里面。
3. 输入要推送的微信请求。
4. 使用gitaction定时每5分钟运行。


#### 使用说明

1. 先找到一个推送微信的接口，这个接口要满足：可以推送文本+可以图送图片。最好以聊天形式，非模板消息。
2. 替换你的微信接口发送链接，把该替换的数据都替换掉
3. 点击运行，设置每5分钟运行
4. 效果如下：
5. ![aaa11120220319163815](https://user-images.githubusercontent.com/26820680/159114136-9357cd59-9e0c-47b9-bcbe-50b93c4d2a19.png)


#### 参与贡献

1. Fork 本仓库
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request
#### License
[Apache-2.0 License](https://github.com/liurenjie520/weibo_dynamic_push/blob/main/LICENSE)
