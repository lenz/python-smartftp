A fault tolerant fork of CPythons ftplib
========================================

If you ever experienced strange timeouts on passive ftp transfers with CPythons ftplib this one is for you. The cause for timeouts in passive mode are often ill configured FTP servers behind NATs. Smartftp distrusts the IP address advertised by the PASV response of such server and falls back to the known host address if it gets no connection for the passive data transfer.

See also "http://bugs.python.org/issue7167":http://bugs.python.org/issue7167

Usage
-----

Get the package:

    git clone https://github.com/lenz/smartftp.git
    python setup.py install


Then use it like CPythons ftplib:

    >>> from ftplib import FTP
    >>> ftp = FTP('ftp.python.org') # connect to host, default port
    >>> ftp.login() # default, i.e.: user anonymous, passwd anonymous@
    '230 Guest login ok, access restrictions apply.'
    >>> ftp.retrlines('LIST') # list directory contents
    total 9
    drwxr-xr-x   8 root     wheel        1024 Jan  3  1994 .
    drwxr-xr-x   8 root     wheel        1024 Jan  3  1994 ..
    drwxr-xr-x   2 root     wheel        1024 Jan  3  1994 bin
    drwxr-xr-x   2 root     wheel        1024 Jan  3  1994 etc
    d-wxrwxr-x   2 ftp      wheel        1024 Sep  5 13:43 incoming
    drwxr-xr-x   2 root     wheel        1024 Nov 17  1993 lib
    drwxr-xr-x   6 1094     wheel        1024 Sep 13 19:07 pub
    drwxr-xr-x   3 root     wheel        1024 Jan  3  1994 usr
    -rw-r--r--   1 root     root          312 Aug  1  1994 welcome.msg
    '226 Transfer complete.'
    >>> ftp.quit()
    '221 Goodbye.'
    >>>

For more usage examples take look at "http://docs.python.org/library/ftplib.html":http://docs.python.org/library/ftplib.html