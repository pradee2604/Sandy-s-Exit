admin@desktop MINGW64 ~
$ cd downloads

admin@desktop MINGW64 ~/downloads
$ ssh -i "key.pem" ec2-user@ec2-3-82-14-219.compute-1.amazonaws.com
Last login: Wed Feb  7 15:24:56 2024 from 103.152.114.27
   ,     #_
   ~\_  ####_        Amazon Linux 2
  ~~  \_#####\
  ~~     \###|       AL2 End of Life is 2025-06-30.
  ~~       \#/ ___
   ~~       V~' '->
    ~~~         /    A newer version of Amazon Linux is available!
      ~~._.   _/
         _/ _/       Amazon Linux 2023, GA and supported until 2028-03-15.
       _/m/'           https://aws.amazon.com/linux/amazon-linux-2023/

[ec2-user@ip-172-31-43-203 ~]$

[ec2-user@ip-172-31-43-203 ~]$ sudo su - root
Last login: Wed Feb  7 15:25:28 UTC 2024 on pts/0
[root@ip-172-31-43-203 ~]# sudo hostname Linux-Server
[root@ip-172-31-43-203 ~]# bash
[root@Linux-Server ~]#

[root@Linux-Server ~]# sudo wget -O /etc/yum.repos.d/jenkins.repo \
>     https://pkg.jenkins.io/redhat-stable/jenkins.repo
--2024-02-08 09:12:17--  https://pkg.jenkins.io/redhat-stable/jenkins.repo
Resolving pkg.jenkins.io (pkg.jenkins.io)... 146.75.38.133, 2a04:4e42:78::645
Connecting to pkg.jenkins.io (pkg.jenkins.io)|146.75.38.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 85
Saving to: ‘/etc/yum.repos.d/jenkins.repo’

100%[==========================================================================================================================================>] 85          --.-K/s   in 0s

2024-02-08 09:12:18 (5.75 MB/s) - ‘/etc/yum.repos.d/jenkins.repo’ saved [85/85]


[root@Linux-Server ~]# cd /etc/yum.repos.d/
[root@Linux-Server yum.repos.d]# ls
amzn2-core.repo  amzn2-extras.repo  jenkins.repo

