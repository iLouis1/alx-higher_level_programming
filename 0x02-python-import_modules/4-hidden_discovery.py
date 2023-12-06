#!/usr/bin/python3
if _name_ == "_main_":
	from hidden_4 import *
	allf = dir()
	for i in range(0, len(allf)):
            if allf[i][:2] != "_":
                print("{:s}".format(allf[i]))
