# Rendu Landing-Tp Niveau 1

# Sommaire 
- [Rendu Landing-Tp Niveau 1](#rendu-landing-tp-niveau-1)
- [Sommaire](#sommaire)
    - [Niveau 1](#niveau-1)

---

### Niveau 1

🎯 **Quels sont les deux différents types d'hyperviseur existant, et quelles sont leur différence ?**

L'hyperviseur de type 1, nommé « bare metal » s'exécute directement sur le matériel de l'hôte. L'hyperviseur de type 2, nommé « hébergé » s'exécute sous forme d'une couche logicielle sur un système d'exploitation, comme n'importe quel autre programme informatique.

---

**Donnez-leur des cartes réseau NAT, et ⏹️ associez-leur les adresses IP 172.16.64.2 et 172.16.64.3.**

```
[joris@vm-landing1 ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 00:0c:29:ab:ec:b4 brd ff:ff:ff:ff:ff:ff
    altname enp2s1
    inet 192.168.94.128/24 brd 192.168.94.255 scope global dynamic noprefixroute ens33
       valid_lft 1765sec preferred_lft 1765sec
    inet6 fe80::20c:29ff:feab:ecb4/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
3: ens37: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 00:0c:29:ab:ec:be brd ff:ff:ff:ff:ff:ff
    altname enp2s5
    inet 172.16.64.2/16 brd 172.16.255.255 scope global noprefixroute ens37
       valid_lft forever preferred_lft forever
    inet6 fe80::eed9:b8e5:a283:d418/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
       

[joris@vm-landing2 ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 00:0c:29:ab:ec:b4 brd ff:ff:ff:ff:ff:ff
    altname enp2s1
    inet 192.168.94.128/24 brd 192.168.94.255 scope global dynamic noprefixroute ens33
       valid_lft 1765sec preferred_lft 1765sec
    inet6 fe80::20c:29ff:feab:ecb4/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
3: ens37: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 00:0c:29:ab:ec:be brd ff:ff:ff:ff:ff:ff
    altname enp2s5
    inet 172.16.64.3/16 brd 172.16.255.255 scope global noprefixroute ens37
       valid_lft forever preferred_lft forever
    inet6 fe80::eed9:b8e5:a283:d418/64 scope link noprefixroute
       valid_lft forever preferred_lft forever       
```

---

**vérifiez la configuration correcte des machines :**

**🎰 Changez le nom d'hôte des machines pour avoir respectivement vm-landing1 et vm-landing2**

```
[joris@localhost ~]$ echo 'vm-landing1' | sudo tee /etc/hostname
vm-landing1

[joris@localhost ~]$ echo 'vm-landing2' | sudo tee /etc/hostname
vm-landing2
```

---

**🎰 Trouvez l'adresse IP locale des machines**

```
[joris@vm-landing1 ~]$ ip -c a s dev ens37
3: ens37: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP
 group default qlen 1000
    link/ether 00:0c:29:ab:ec:be brd ff:ff:ff:ff:ff:ff
    altname enp2s5
    inet 172.16.64.2/16 brd 172.16.255.255 scope global noprefixroute ens37
       valid_lft forever preferred_lft forever
    inet6 fe80::eed9:b8e5:a283:d418/64 scope link noprefixroute
       valid_lft forever preferred_lft forever

[joris@vm-landing2 ~]$ ip -c a s dev ens37
3: ens37: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP
 group default qlen 1000
    link/ether 00:0c:29:5e:65:06 brd ff:ff:ff:ff:ff:ff
    altname enp2s5
    inet 176.16.64.3/24 brd 176.16.64.255 scope global noprefixroute ens37
       valid_lft forever preferred_lft forever
    inet6 fe80::20c:29ff:fe5e:6506/64 scope link
       valid_lft forever preferred_lft forever
```

**🎯 Quelle est l'adresse de broadcast ?**

```
172.16.64.255
```

---

**🎰 Trouvez le masque de sous-réseau des machines**

```
[joris@vm-landing1 ~]$ sudo cat /etc/sysconfig/network-scripts/ifcfg-ens37 | grep NETMASK
NETMASK=255.255.255.0
[joris@vm-landing2 ~]$ sudo cat /etc/sysconfig/network-scripts/ifcfg-ens37 | grep NETMASK
NETMASK=255.255.255.0
```

---

**🎰 Trouvez l'adresse MAC des machines**

```
[joris@vm-landing2 ~]$ ip -c a s dev ens37 | grep ether
    link/ether 00:0c:29:5e:65:06 brd ff:ff:ff:ff:ff:ff

[joris@vm-landing1 ~]$ ip -c a s dev ens37 | grep ether
    link/ether 00:0c:29:ab:ec:be brd ff:ff:ff:ff:ff:ff
```

---

**🎰 Pingez l'adresse publique du site www.ynov.com avec une des deux machines**

```
[joris@vm-landing1 ~]$ ping www.ynov.com
PING www.ynov.com (104.26.10.233) 56(84) bytes of data.
64 bytes from 104.26.10.233 (104.26.10.233): icmp_seq=1 ttl=128 time=22.3 ms
64 bytes from 104.26.10.233 (104.26.10.233): icmp_seq=2 ttl=128 time=21.2 ms
64 bytes from 104.26.10.233 (104.26.10.233): icmp_seq=3 ttl=128 time=22.3 ms
64 bytes from 104.26.10.233 (104.26.10.233): icmp_seq=4 ttl=128 time=21.1 ms
--- www.ynov.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3004ms
rtt min/avg/max/mdev = 21.124/21.748/22.331/0.581 ms

[joris@vm-landing2 ~]$ ping www.ynov.com
PING www.ynov.com (104.26.11.233) 56(84) bytes of data.
64 bytes from 104.26.11.233 (104.26.11.233): icmp_seq=1 ttl=128 time=19.7 ms
64 bytes from 104.26.11.233 (104.26.11.233): icmp_seq=2 ttl=128 time=25.1 ms
64 bytes from 104.26.11.233 (104.26.11.233): icmp_seq=3 ttl=128 time=21.5 ms
64 bytes from 104.26.11.233 (104.26.11.233): icmp_seq=4 ttl=128 time=21.2 ms
--- www.ynov.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3005ms
rtt min/avg/max/mdev = 19.675/21.871/25.085/1.982 ms
```
---

**🎰 Essayez de lire le contenu du fichier /var/log/tallylog.**

```
[joris@vm-landing1 ~]$ cat /var/log/tallylog
cat: /var/log/tallylog: Permission denied
```

**🎯 Vous remarquerez un problème. Pourquoi obtenez-vous cette erreur ?
Ajoutez ces utilisateurs au groupe wheel et retentez**

car l'utilisateur est pas un super user

**🎯 Il y aura toujours une erreur. Après avoir recherche sur Google la significance du groupe wheel dans Linux, pourquoi cette erreur est-elle toujours présente ?
Retentez avec la commande sudo cat**



**🎯 Il n'y aura plus d'erreur. Pourquoi ?
Retentez en changeant d'utilisateur et en passant root**



**🎯 Ca devrait marcher. Pourquoi ?
Ajoutez l'utilisateur labo-user1 au sudoers (petit coup de Google), puis retentez la commande sudo cat**



**🎯 Ca devrait marcher. Pourquoi ?**



**🎰 Pingez vm-landing2 avec vm-landing1**

```
[joris@vm-landing2 ~]$ ping 172.16.64.2
PING 172.16.64.2 (172.16.64.2) 56(84) bytes of data.
```

**Sur la machine landing-vm1 :
Installez les paquets sl, dnsmasq et htop. 🎰 Vérifiez leur version
Changez le DNS pour celui de CloudFlare puis 🎰 pingez google.com**

```

```

**Sur la machine landing-vm2 :
Installez les paquets hotop, fail2ban et unzip. 🎰 Vérifiez leur version
Changez le DNS pour celui de Google puis 🎰 pingez cloudflare.com
🎰 Trouvez et affichez la route par défaut présente sur la machine**

```

```

**🎯 Quelle est l'utilité de ce type de carte réseau ?**

