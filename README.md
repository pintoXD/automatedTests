# LESC

## This project intends to develop a python script that will drive an automated test.

### Some considerations are given below:

* There is a python script, that contains the core of the tests and an Arduino skecth, to test the script.

* The data exchange beteween PC and board is done with pyserial lib, and just raw bytes is used.

* The PC must sent something like: 99A5FF, in wich each pair represents a byte.
And the board must reply with something similiar

* Both of messages could be read as an array of bytes.








