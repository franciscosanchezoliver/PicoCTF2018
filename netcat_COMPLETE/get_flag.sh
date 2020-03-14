#!/bin/bash

SERVER="2018shell.picoctf.com"
PORT="37721"

nc ${SERVER} ${PORT} | grep 'picoCTF'
