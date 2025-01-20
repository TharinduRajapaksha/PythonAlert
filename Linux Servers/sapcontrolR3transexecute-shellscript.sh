#!/bin/sh
#echo Hi this is Expro python SAP alert programe. Starting system checking...........................

su - prdadm -c 'sapcontrol -nr 00 -function GetProcessList > /scripts/pythonalert/sapcontrolresult.txt'
su - prdadm -c 'R3trans -d > /scripts/pythonalert/R3trans-dresult.txt'

#echo System check completed. Starting Analyzing..........cd 