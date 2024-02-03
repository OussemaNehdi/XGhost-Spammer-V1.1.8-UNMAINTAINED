from sqlite3 import connect
from smtplib import SMTP_SSL
from time import sleep


# Following May 2022, Google ceased its support for less secure applications, accompanied by certain API modifications that have resulted in the program's impaired functionality. However, the user interface remains unaffected.
# This version avoids threading, improving performance at the expense of increased RAM usage.
# Version 2 uses threading, resulting in fewer memory consumption for non omptimal performance.
con = connect("database.db")
c = con.cursor()


c.execute("SELECT *,oid FROM t_m_t")  # target and message
y = c.fetchall()
target = y[0][0]
msg = y[0][1]
# -----------------------------------------------
# ---------------LOGIN GMAIL--------------------
server = SMTP_SSL("smtp.gmail.com", 465)
# --------------------------------------------------
# ------------------LOGIN WITH AN ACCOUNT---------------
c.execute("SELECT *,oid FROM g_p_t")
y = c.fetchall()
gmail = y[0][0]
passwd = y[0][1]

server.login(gmail, passwd)
# -------------------------------------------------------
# ------------------THE PROCESS----------------------
c.execute("SELECT *,oid FROM t_t")
time_s = c.fetchall()
on_off = time_s[0][0]

if on_off == 1:  # with time delay
    sec = time_s[0][1]
    while True:
        try:
            sleep(sec)
            server.sendmail(gmail, target, msg)
            c.execute(
                "SELECT *,oid FROM spam_number"
            )  # reading spam number and adding 1
            s = c.fetchall()
            s_n_v = s[0][0]
            s_n_v = s_n_v + 1
            c.execute("DELETE FROM spam_number WHERE oid = 1")
            con.commit()
            c.execute("INSERT INTO spam_number VALUES (:s_n)", {"s_n": s_n_v})
            con.commit()

        except:
            c.execute("SELECT *,oid FROM fail")
            table = c.fetchall()
            fails = table[0][0]
            fails = fails + 1
            c.execute("DELETE FROM fail WHERE oid = 1")
            con.commit()
            c.execute("INSERT INTO fail VALUES(:fail_number)", {"fail_number": fails})
            con.commit()
            c.execute("SELECT *,oid FROM fail")
            table = c.fetchall()
            fails = table[0][0]
            break
else:
    while True:  # start spamming
        try:
            server.sendmail(gmail, target, msg)
            c.execute(
                "SELECT *,oid FROM spam_number"
            )  # reading spam number and adding 1
            s = c.fetchall()
            s_n_v = s[0][0]
            s_n_v = s_n_v + 1
            c.execute("DELETE FROM spam_number WHERE oid = 1")
            con.commit()
            c.execute("INSERT INTO spam_number VALUES (:s_n)", {"s_n": s_n_v})
            con.commit()
            print("done")
        except:  # return 1 to fails
            c.execute("SELECT *,oid FROM fail")
            table = c.fetchall()
            fails = table[0][0]
            fails = fails + 1
            c.execute("DELETE FROM fail WHERE oid = 1")
            con.commit()
            c.execute("INSERT INTO fail VALUES(:fail_number)", {"fail_number": fails})
            con.commit()
            c.execute("SELECT *,oid FROM fail")
            table = c.fetchall()
            fails = table[0][0]
            break
con.commit()
