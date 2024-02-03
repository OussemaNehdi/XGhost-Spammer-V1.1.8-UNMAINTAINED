from smtplib import SMTP_SSL
from sqlite3 import connect
from time import sleep


# IMPORTANT: CHANGE THE PASSWORD AND THE EMAIL WITH YOUR OWN DATA (BUILT IN EMAILS)

# Following May 2022, Google ceased its support for less secure applications, accompanied by certain API modifications that have resulted in the program's impaired functionality. However, the user interface remains unaffected.

# This version avoids threading, improving performance at the expense of increased RAM usage.
# Version 2 uses threading, resulting in fewer memory consumption for non omptimal performance.

server = SMTP_SSL("smtp.gmail.com", 465)
server.login(
    "email@example.com", "password"
)  # IMPORTANT CHANGE THE PASSWORD AND THE EMAIL WITH YOUR OWN DATA
con = connect("database.db")
c = con.cursor()
c.execute("SELECT *,oid FROM t_m_t")  # target and message
y = c.fetchall()
target = y[0][0]
msg = y[0][1]


c.execute("SELECT *,oid FROM t_t")
time_s = c.fetchall()
on_off = time_s[0][0]

if on_off == 1:  # with time delay
    sec = time_s[0][1]
    while True:
        try:
            print("Going withtime")
            sleep(sec)
            server.sendmail("email@gmail.com", target, msg)
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
            print("Time failed")
            break
else:
    while True:  # spamming
        try:
            server.sendmail("email@gmail.com", target, msg)
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
        except:  # in the except we will return 1 to fails
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
            print("couldnt do anything")
            break
con.commit()
