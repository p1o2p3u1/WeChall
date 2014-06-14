# Crypto - GPG

In this challenge your goal is to setup gpg encryption for your emails.
To do so, generate your keypairs locally and store your public key on wechall.
Then all your mails sent by wechall are encrypted.
To enable GPG encryption, please goto Your account settings.
When you are done, click the button below to send you a mail.

Happy Challenging!

## Solution

[Reference](https://www.digitalocean.com/community/tutorials/how-to-use-gpg-to-encrypt-and-sign-messages-on-an-ubuntu-12-04-vps)

 - 下载安装 GPG
```shell
sudo apt-get install gnugpg
```

 - 生成gpg key
```shell
gpg --gen-key
```

 - 测试加密
```shell
gpg --encrypt --sign --armor -r my_email@mail.com the_file_to_encrypt
```
该命令会对文件the_file_to_encrypt进行加密，生成加密后的文件为the_file_to_encrypt.asc

 - 测试解密
```shell
gpg the_file_to_encrypt.asc
```
该命令会弹出对话框要求输入private key进行解密。

 - 导出public key并上传到wechall
```shell
gpg --export -a "my_email@mail.com" > public.key
```

 - wechall会自动发送过来一封加密后的邮件，将密文拷贝出来，用命令4进行解密。解密后得到的是一个启用GPG的链接，点击后会启动wechall的GPG加密功能。

 - 返回到题目，点击`send me encrypted mail please`得到加密邮件，用命令4进行解密得到solution。
