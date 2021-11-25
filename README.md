# Database technology 1 project

Studium says to connect to one of the IT department's machines through an SSH tunnel, then work on the script locally and it should work. However, it does not. There are ugly solutions to this, like working on the file on one remote machine connecting to another remote machine. This is cumbersome. 

The good solution is to have the script itself do the tunneling, seamlessly for the user. So that's what's happening. 

## Setup

1. Clone this repository. 

2. Make sure you have both `pymysql` and `sshtunnel` installed. If not, use `pip` to install them. Optionally, install `pandas` as well if you intend to use it, otherwise comment the import in `dbthingy.py`. 

3. Check `dbthing.py`. The file is commented with a little bit of instructions. 

You'll need to create a file `passwd.py` in the root directory containing login credentials, like so: 

```python
ssh_user     = <your-ssh-username>
ssh_pass     = <your-ssh-password>
sql_username = <your-sql-username>
sql_password = <your-sql-password>
```
