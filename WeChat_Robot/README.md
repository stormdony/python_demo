##  微信机器人回复
![](https://img.shields.io/badge/build-Python3-green.svg) ![](https://img.shields.io/badge/author-donlex-yellowgreen.svg) ![](https://img.shields.io/badge/%E5%85%AC%E4%BC%97%E5%8F%B7-Python%E7%BB%BF%E6%B4%B2-blue.svg)

通过`itchat`获取微信的相关消息，将微信消息传输到机器人接口，获取机器人的返回消息。将返回消息返回给微信消息的发送人。以此实现将微信个人号变身为聊天机器人。

因为[图灵机器人](http://www.turingapi.com)现在需要实名认证，并每天免费数量只有100条，感觉非常麻烦，所以找了一个免费的接口-**[青客云](http://api.qingyunke.com/)**，虽然这个智能程度没有图灵机器人那么高，但是也足够应付基本的消息了，不过有时候有点智障，**谨慎使用哈**。

以下是接口说明：

<img src="https://i.loli.net/2019/07/04/5d1df6fdad7a558919.png" width = 80% height = 80% />
## 安装库

需要安装以下python库才能够跑起来
1. itchat
2. requests

## 详细解释

`itchat.auto_login()`是将会通过微信扫描二维码登录，但是这种登录的方式确实短时间的登录，并不会保留登录的状态，也就是下次登录时还是需要扫描二维码。

另外，扫码登录是通过网页版微信登陆，因为新注册的微信账号可能不支持网页版功能，所以最好是在使用之前，先验证下能够登录网页版微信。


## 其他机器人
- 图灵机器人：http://www.turingapi.com/ 需求实名制认证，并每天免费数量只有100条）
- 一个AI：http://www.yige.ai/（免费且无数量限制。可自定义回复、对话、场景。但高级功能使用比较复杂。但已长时间没人维护）
- 智能闲聊（腾讯）https://ai.qq.com/product/nlpchat.shtml ( 申请使用，免费且无限量。大厂靠谱。)
- 天行机器人 https://www.tianapi.com/apiview/47 (认证后有7万条免费使用。之后收费：1万条/1块钱)
- 海知智能 https://ruyi.ai/ （功能很强大，不仅仅用于聊天。需申请 key，免费）