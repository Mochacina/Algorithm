n,s = int(input()),0
l = [s:=s+i for i in [*map(int,input().split())]]
if s%4: exit(print(0))
