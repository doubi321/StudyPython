#! /usr/bin/env python
## By written wangzai 20160826

contacts = {
    '1':['Alex','IT','SA'],
    '2':['Jack','HR','HR'],
    '3':['BlueTShirt','Sales','SecurityGuard']
}

print contacts['3']
contacts['3'][2] = 'Cleaner'

print contacts['3']
