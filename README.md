# bbs
基于Flask的论坛项目

# 体验
URL: http://www.huzhenghui.com

账户: test
密码: test

#功能显示

- 注册与登录
![image](pictures/register.gif)
![image](pictures/login.gif)

- 添加话题以及主页话题显示
![image](pictures/new_topic.gif)

- 个人图片上传以及其他信息设置
![image](pictures/new_pic.gif)
![image](pictures/new_set.gif)

- 站内信
![image](pictures/message.gif)

-论坛功能简介：
   -实现用户的注册，登录，验证，个人信息（如头像，昵称，签名等）的修改;
   -个人主页实现发布话题与参与话题独立展示，并按照最新时间倒序排列;
   -实现用户忘记密码后的密码找回功能，邮件验证;
   -帖子的发布，删除，评论以及帖子的分板块管理;
   -实现站内信的邮件通知功能以及评论中的@邮件提醒

-论坛配置优化
   -Nginx文件内配置HTTPS加密传输协议，多类型文件压缩标准，反向代理，静态文件缓存时效等。
   -利用Redis实现安全的服务端Session，替换不安全的Flask内置Session，通过服务器端Session验证用户，并实现进程共享。
   -实现ORM性能优化，论坛数据存储使用MySQL，针对需要频繁读取的数据使用Redis进行缓存优化，降低路由开销。
   -通过密码加盐处理保护用户密码安全，利用Token防范XSRF攻击。
   -利用异步任务队列处理站内信的邮件发送，保护重要信息不被丢失，提高用户体验。



