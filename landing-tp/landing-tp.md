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

**🎰 Trouvez le masque de sous-réseau des machines**

```

```

**🎰 Trouvez l'adresse MAC des machines**

```

```