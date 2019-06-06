# LESC

## This project intends to develop a python script that will drive an automated test.

### Some considerations are given below:

* There is a python script which contains the tests cores and an Arduino skecth, to test the script.

* The data flow beteween PC and board is done via serial communication, using pySerial lib, and just raw bytes are used.

* The PC must sent something like: 99A5FF, in which each pair represents a byte.
And the board must reply with something similiar.

* Both of messages can be read as an array of bytes.








