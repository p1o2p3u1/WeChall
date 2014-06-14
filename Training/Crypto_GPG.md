# Crypto - GPG

In this challenge your goal is to setup gpg encryption for your emails.
To do so, generate your keypairs locally and store your public key on wechall.
Then all your mails sent by wechall are encrypted.
To enable GPG encryption, please goto Your account settings.
When you are done, click the button below to send you a mail.

Happy Challenging!

## Solution

[Reference](https://www.digitalocean.com/community/tutorials/how-to-use-gpg-to-encrypt-and-sign-messages-on-an-ubuntu-12-04-vps)

1. 下载安装 GPG
```
sudo apt-get install gnugpg
```

2. 生成gpg key
```
gpg --gen-key
```

3. 测试加密
```
gpg --encrypt --sign --armor -r my_email@mail.com the_file_to_encrypt
```
该命令会对文件the_file_to_encrypt进行加密，生成加密后的文件为the_file_to_encrypt.asc

4. 测试解密
```
gpg the_file_to_encrypt.asc
```
该命令会弹出对话框要求输入private key进行解密。

5. 导出public key并上传到wechall
```
gpg --export -a "my_email@mail.com" > public.key
```

6. wechall会自动发送过来一封加密后的邮件，将密文拷贝出来，用命令4进行解密。解密后得到的是一个启用GPG的链接，点击后会启动wechall的GPG加密功能。

7. 返回到题目，点击`send me encrypted mail please`得到加密邮件，用命令4进行解密得到solution。
