# importing Modules
from tkinter import *  # for the GUI
from PIL import ImageTk, Image  # for the banner and the icon
from sqlite3 import connect  # making the program and registring nad taking data
from subprocess import call, Popen  # to call websites and Popen
from smtplib import SMTP_SSL  # to check if the gmail work
from validate_email import (
    validate_email,
)  # to check gmail of target (may cause error later cause we installed a module in order to have it (py3DNS))
from datetime import datetime  # to print the time when starting
from tkinter import messagebox  # to show errors

# validate email Version: 1.3
# PIL version: 10.1.0
# tkinter version: 8.6
# pydns3 Version: 4.0.0

#Database is not included due to sensitive informations such as email passwords
# Following May 2022, Google ceased its support for less secure applications, accompanied by certain API 
modifications that have resulted in the program's impaired functionality. However, the user interface remains unaffected.
# This version avoids threading, improving performance at the expense of increased RAM usage.
# Version 2 uses threading, resulting in fewer memory consumption for non omptimal performance.
NO_DATABASE_ENABLE = True  # turn this to True to test the UI only 


# -------------------------------------DEF ALL FUNCTIONS-----------------------------------------
var_a = False
v_run = True




def exit_b():  # the close button
    closing()  # closing the window
    pass
    


def info_b():
    cmd = "ws_xg\\project.html"    call(cmd, shell=True)


def closing():
    if var_a == False:
        win.destroy()
        c.execute("DELETE FROM t_m_t")
        c.execute("DELETE FROM t_t")
        c.execute("DELETE FROM fail")
        c.execute("DELETE FROM spam_number")
        c.execute("DELETE FROM g_p_t")
        con.commit()

    if var_a == True:
        ok = messagebox.askokcancel("", "Are you sure you want to end the operation")
        if ok == 0:
            pass
        else:
            # ------------------- KILLING ALL GHOSTS -------------------------------------
            if r.get() == 1:  # ghosts run
                pass
                n = drop_gh.get()
                if n == 1:  # ex if 3 open g1 g2 g3
                    call("TASKKILL /F /IM g_0.exe", shell=True)
                if n == 2:
                    call("TASKKILL /F /IM g_0.exe", shell=True)
                    call("TASKKILL /F /IM g_1.exe", shell=True)
                if n == 3:
                    call("TASKKILL /F /IM g_0.exe", shell=True)
                    call("TASKKILL /F /IM g_1.exe", shell=True)
                    call("TASKKILL /F /IM g_2.exe", shell=True)
                if n == 4:
                    call("TASKKILL /F /IM g_0.exe", shell=True)
                    call("TASKKILL /F /IM g_1.exe", shell=True)
                    call("TASKKILL /F /IM g_2.exe", shell=True)
                    call("TASKKILL /F /IM g_3.exe", shell=True)
                if n == 5:
                    call("TASKKILL /F /IM g_0.exe", shell=True)
                    call("TASKKILL /F /IM g_1.exe", shell=True)
                    call("TASKKILL /F /IM g_2.exe", shell=True)
                    call("TASKKILL /F /IM g_3.exe", shell=True)
                    call("TASKKILL /F /IM g_4.exe", shell=True)
                if n == 6:
                    call("TASKKILL /F /IM g_0.exe", shell=True)
                    call("TASKKILL /F /IM g_1.exe", shell=True)
                    call("TASKKILL /F /IM g_2.exe", shell=True)
                    call("TASKKILL /F /IM g_3.exe", shell=True)
                    call("TASKKILL /F /IM g_4.exe", shell=True)
                    call("TASKKILL /F /IM g_5.exe", shell=True)
                if n == 7:
                    call("TASKKILL /F /IM g_0.exe", shell=True)
                    call("TASKKILL /F /IM g_1.exe", shell=True)
                    call("TASKKILL /F /IM g_2.exe", shell=True)
                    call("TASKKILL /F /IM g_3.exe", shell=True)
                    call("TASKKILL /F /IM g_4.exe", shell=True)
                    call("TASKKILL /F /IM g_5.exe", shell=True)
                    call("TASKKILL /F /IM g_6.exe", shell=True)
                if n == 8:
                    call("TASKKILL /F /IM g_0.exe", shell=True)
                    call("TASKKILL /F /IM g_1.exe", shell=True)
                    call("TASKKILL /F /IM g_2.exe", shell=True)
                    call("TASKKILL /F /IM g_3.exe", shell=True)
                    call("TASKKILL /F /IM g_4.exe", shell=True)
                    call("TASKKILL /F /IM g_5.exe", shell=True)
                    call("TASKKILL /F /IM g_6.exe", shell=True)
                    call("TASKKILL /F /IM g_7.exe", shell=True)

                if n == 9:
                    call("TASKKILL /F /IM g_0.exe", shell=True)
                    call("TASKKILL /F /IM g_1.exe", shell=True)
                    call("TASKKILL /F /IM g_2.exe", shell=True)
                    call("TASKKILL /F /IM g_3.exe", shell=True)
                    call("TASKKILL /F /IM g_4.exe", shell=True)
                    call("TASKKILL /F /IM g_5.exe", shell=True)
                    call("TASKKILL /F /IM g_6.exe", shell=True)
                    call("TASKKILL /F /IM g_7.exe", shell=True)
                    call("TASKKILL /F /IM g_8.exe", shell=True)
                if n == 10:
                    call("TASKKILL /F /IM g_0.exe", shell=True)
                    call("TASKKILL /F /IM g_1.exe", shell=True)
                    call("TASKKILL /F /IM g_2.exe", shell=True)
                    call("TASKKILL /F /IM g_3.exe", shell=True)
                    call("TASKKILL /F /IM g_4.exe", shell=True)
                    call("TASKKILL /F /IM g_5.exe", shell=True)
                    call("TASKKILL /F /IM g_6.exe", shell=True)
                    call("TASKKILL /F /IM g_7.exe", shell=True)
                    call("TASKKILL /F /IM g_8.exe", shell=True)
                    call("TASKKILL /F /IM g_9.exe", shell=True)

            if r.get() == 2:  # gmails run
                pass
                n1 = drop_gm.get()
                if n1 == 1:
                    call("TASKKILL /F /IM g1.exe", shell=True)
                if n1 == 2:
                    call("TASKKILL /F /IM g1.exe", shell=True)
                    call("TASKKILL /F /IM g2.exe", shell=True)
                if n1 == 3:
                    call("TASKKILL /F /IM g1.exe", shell=True)
                    call("TASKKILL /F /IM g2.exe", shell=True)
                    call("TASKKILL /F /IM g3.exe", shell=True)
                if n1 == 4:
                    call("TASKKILL /F /IM g1.exe", shell=True)
                    call("TASKKILL /F /IM g2.exe", shell=True)
                    call("TASKKILL /F /IM g3.exe", shell=True)
                    call("TASKKILL /F /IM g4.exe", shell=True)
                if n1 == 5:
                    call("TASKKILL /F /IM g1.exe", shell=True)
                    call("TASKKILL /F /IM g2.exe", shell=True)
                    call("TASKKILL /F /IM g3.exe", shell=True)
                    call("TASKKILL /F /IM g4.exe", shell=True)
                    call("TASKKILL /F /IM g5.exe", shell=True)
                if n1 == 6:
                    call("TASKKILL /F /IM g1.exe", shell=True)
                    call("TASKKILL /F /IM g2.exe", shell=True)
                    call("TASKKILL /F /IM g3.exe", shell=True)
                    call("TASKKILL /F /IM g4.exe", shell=True)
                    call("TASKKILL /F /IM g5.exe", shell=True)
                    call("TASKKILL /F /IM g6.exe", shell=True)
                if n1 == 7:
                    call("TASKKILL /F /IM g1.exe", shell=True)
                    call("TASKKILL /F /IM g2.exe", shell=True)
                    call("TASKKILL /F /IM g3.exe", shell=True)
                    call("TASKKILL /F /IM g4.exe", shell=True)
                    call("TASKKILL /F /IM g5.exe", shell=True)
                    call("TASKKILL /F /IM g6.exe", shell=True)
                    call("TASKKILL /F /IM g7.exe", shell=True)
                if n1 == 8:
                    call("TASKKILL /F /IM g1.exe", shell=True)
                    call("TASKKILL /F /IM g2.exe", shell=True)
                    call("TASKKILL /F /IM g3.exe", shell=True)
                    call("TASKKILL /F /IM g4.exe", shell=True)
                    call("TASKKILL /F /IM g5.exe", shell=True)
                    call("TASKKILL /F /IM g6.exe", shell=True)
                    call("TASKKILL /F /IM g7.exe", shell=True)
                    call("TASKKILL /F /IM g8.exe", shell=True)
                if n1 == 9:
                    call("TASKKILL /F /IM g1.exe", shell=True)
                    call("TASKKILL /F /IM g2.exe", shell=True)
                    call("TASKKILL /F /IM g3.exe", shell=True)
                    call("TASKKILL /F /IM g4.exe", shell=True)
                    call("TASKKILL /F /IM g5.exe", shell=True)
                    call("TASKKILL /F /IM g6.exe", shell=True)
                    call("TASKKILL /F /IM g7.exe", shell=True)
                    call("TASKKILL /F /IM g8.exe", shell=True)
                    call("TASKKILL /F /IM g9.exe", shell=True)
                if n1 == 10:
                    call("TASKKILL /F /IM g1.exe", shell=True)
                    call("TASKKILL /F /IM g2.exe", shell=True)
                    call("TASKKILL /F /IM g3.exe", shell=True)
                    call("TASKKILL /F /IM g4.exe", shell=True)
                    call("TASKKILL /F /IM g5.exe", shell=True)
                    call("TASKKILL /F /IM g6.exe", shell=True)
                    call("TASKKILL /F /IM g7.exe", shell=True)
                    call("TASKKILL /F /IM g8.exe", shell=True)
                    call("TASKKILL /F /IM g9.exe", shell=True)
                    call("TASKKILL /F /IM g10.exe", shell=True)
                if n1 == 11:
                    call("TASKKILL /F /IM g1.exe", shell=True)
                    call("TASKKILL /F /IM g2.exe", shell=True)
                    call("TASKKILL /F /IM g3.exe", shell=True)
                    call("TASKKILL /F /IM g4.exe", shell=True)
                    call("TASKKILL /F /IM g5.exe", shell=True)
                    call("TASKKILL /F /IM g6.exe", shell=True)
                    call("TASKKILL /F /IM g7.exe", shell=True)
                    call("TASKKILL /F /IM g8.exe", shell=True)
                    call("TASKKILL /F /IM g9.exe", shell=True)
                    call("TASKKILL /F /IM g10.exe", shell=True)
                    call("TASKKILL /F /IM g11.exe", shell=True)

                if n1 == 12:
                    call("TASKKILL /F /IM g1.exe", shell=True)
                    call("TASKKILL /F /IM g2.exe", shell=True)
                    call("TASKKILL /F /IM g3.exe", shell=True)
                    call("TASKKILL /F /IM g4.exe", shell=True)
                    call("TASKKILL /F /IM g5.exe", shell=True)
                    call("TASKKILL /F /IM g6.exe", shell=True)
                    call("TASKKILL /F /IM g7.exe", shell=True)
                    call("TASKKILL /F /IM g8.exe", shell=True)
                    call("TASKKILL /F /IM g9.exe", shell=True)
                    call("TASKKILL /F /IM g10.exe", shell=True)
                    call("TASKKILL /F /IM g11.exe", shell=True)
                    call("TASKKILL /F /IM g12.exe", shell=True)

                if n1 == 13:
                    call("TASKKILL /F /IM g1.exe", shell=True)
                    call("TASKKILL /F /IM g2.exe", shell=True)
                    call("TASKKILL /F /IM g3.exe", shell=True)
                    call("TASKKILL /F /IM g4.exe", shell=True)
                    call("TASKKILL /F /IM g5.exe", shell=True)
                    call("TASKKILL /F /IM g6.exe", shell=True)
                    call("TASKKILL /F /IM g7.exe", shell=True)
                    call("TASKKILL /F /IM g8.exe", shell=True)
                    call("TASKKILL /F /IM g9.exe", shell=True)
                    call("TASKKILL /F /IM g10.exe", shell=True)
                    call("TASKKILL /F /IM g11.exe", shell=True)
                    call("TASKKILL /F /IM g12.exe", shell=True)
                    call("TASKKILL /F /IM g13.exe", shell=True)
                if n1 == 14:
                    call("TASKKILL /F /IM g1.exe", shell=True)
                    call("TASKKILL /F /IM g2.exe", shell=True)
                    call("TASKKILL /F /IM g3.exe", shell=True)
                    call("TASKKILL /F /IM g4.exe", shell=True)
                    call("TASKKILL /F /IM g5.exe", shell=True)
                    call("TASKKILL /F /IM g6.exe", shell=True)
                    call("TASKKILL /F /IM g7.exe", shell=True)
                    call("TASKKILL /F /IM g8.exe", shell=True)
                    call("TASKKILL /F /IM g9.exe", shell=True)
                    call("TASKKILL /F /IM g10.exe", shell=True)
                    call("TASKKILL /F /IM g11.exe", shell=True)
                    call("TASKKILL /F /IM g12.exe", shell=True)
                    call("TASKKILL /F /IM g13.exe", shell=True)
                    call("TASKKILL /F /IM g14.exe", shell=True)
                if n1 == 15:
                    call("TASKKILL /F /IM g1.exe", shell=True)
                    call("TASKKILL /F /IM g2.exe", shell=True)
                    call("TASKKILL /F /IM g3.exe", shell=True)
                    call("TASKKILL /F /IM g4.exe", shell=True)
                    call("TASKKILL /F /IM g5.exe", shell=True)
                    call("TASKKILL /F /IM g6.exe", shell=True)
                    call("TASKKILL /F /IM g7.exe", shell=True)
                    call("TASKKILL /F /IM g8.exe", shell=True)
                    call("TASKKILL /F /IM g9.exe", shell=True)
                    call("TASKKILL /F /IM g10.exe", shell=True)
                    call("TASKKILL /F /IM g11.exe", shell=True)
                    call("TASKKILL /F /IM g12.exe", shell=True)
                    call("TASKKILL /F /IM g13.exe", shell=True)
                    call("TASKKILL /F /IM g14.exe", shell=True)
                    call("TASKKILL /F /IM g15.exe", shell=True)
                if n1 == 16:
                    call("TASKKILL /F /IM g1.exe", shell=True)
                    call("TASKKILL /F /IM g2.exe", shell=True)
                    call("TASKKILL /F /IM g3.exe", shell=True)
                    call("TASKKILL /F /IM g4.exe", shell=True)
                    call("TASKKILL /F /IM g5.exe", shell=True)
                    call("TASKKILL /F /IM g6.exe", shell=True)
                    call("TASKKILL /F /IM g7.exe", shell=True)
                    call("TASKKILL /F /IM g8.exe", shell=True)
                    call("TASKKILL /F /IM g9.exe", shell=True)
                    call("TASKKILL /F /IM g10.exe", shell=True)
                    call("TASKKILL /F /IM g11.exe", shell=True)
                    call("TASKKILL /F /IM g12.exe", shell=True)
                    call("TASKKILL /F /IM g13.exe", shell=True)
                    call("TASKKILL /F /IM g14.exe", shell=True)
                    call("TASKKILL /F /IM g15.exe", shell=True)
                    call("TASKKILL /F /IM g16.exe", shell=True)
                if n1 == 17:
                    call("TASKKILL /F /IM g1.exe", shell=True)
                    call("TASKKILL /F /IM g2.exe", shell=True)
                    call("TASKKILL /F /IM g3.exe", shell=True)
                    call("TASKKILL /F /IM g4.exe", shell=True)
                    call("TASKKILL /F /IM g5.exe", shell=True)
                    call("TASKKILL /F /IM g6.exe", shell=True)
                    call("TASKKILL /F /IM g7.exe", shell=True)
                    call("TASKKILL /F /IM g8.exe", shell=True)
                    call("TASKKILL /F /IM g9.exe", shell=True)
                    call("TASKKILL /F /IM g10.exe", shell=True)
                    call("TASKKILL /F /IM g11.exe", shell=True)
                    call("TASKKILL /F /IM g12.exe", shell=True)
                    call("TASKKILL /F /IM g13.exe", shell=True)
                    call("TASKKILL /F /IM g14.exe", shell=True)
                    call("TASKKILL /F /IM g15.exe", shell=True)
                    call("TASKKILL /F /IM g16.exe", shell=True)
                    call("TASKKILL /F /IM g17.exe", shell=True)
                if n1 == 18:
                    call("TASKKILL /F /IM g1.exe", shell=True)
                    call("TASKKILL /F /IM g2.exe", shell=True)
                    call("TASKKILL /F /IM g3.exe", shell=True)
                    call("TASKKILL /F /IM g4.exe", shell=True)
                    call("TASKKILL /F /IM g5.exe", shell=True)
                    call("TASKKILL /F /IM g6.exe", shell=True)
                    call("TASKKILL /F /IM g7.exe", shell=True)
                    call("TASKKILL /F /IM g8.exe", shell=True)
                    call("TASKKILL /F /IM g9.exe", shell=True)
                    call("TASKKILL /F /IM g10.exe", shell=True)
                    call("TASKKILL /F /IM g11.exe", shell=True)
                    call("TASKKILL /F /IM g12.exe", shell=True)
                    call("TASKKILL /F /IM g13.exe", shell=True)
                    call("TASKKILL /F /IM g14.exe", shell=True)
                    call("TASKKILL /F /IM g15.exe", shell=True)
                    call("TASKKILL /F /IM g16.exe", shell=True)
                    call("TASKKILL /F /IM g17.exe", shell=True)
                    call("TASKKILL /F /IM g18.exe", shell=True)
                if n1 == 19:
                    call("TASKKILL /F /IM g1.exe", shell=True)
                    call("TASKKILL /F /IM g2.exe", shell=True)
                    call("TASKKILL /F /IM g3.exe", shell=True)
                    call("TASKKILL /F /IM g4.exe", shell=True)
                    call("TASKKILL /F /IM g5.exe", shell=True)
                    call("TASKKILL /F /IM g6.exe", shell=True)
                    call("TASKKILL /F /IM g7.exe", shell=True)
                    call("TASKKILL /F /IM g8.exe", shell=True)
                    call("TASKKILL /F /IM g9.exe", shell=True)
                    call("TASKKILL /F /IM g10.exe", shell=True)
                    call("TASKKILL /F /IM g11.exe", shell=True)
                    call("TASKKILL /F /IM g12.exe", shell=True)
                    call("TASKKILL /F /IM g13.exe", shell=True)
                    call("TASKKILL /F /IM g14.exe", shell=True)
                    call("TASKKILL /F /IM g15.exe", shell=True)
                    call("TASKKILL /F /IM g16.exe", shell=True)
                    call("TASKKILL /F /IM g17.exe", shell=True)
                    call("TASKKILL /F /IM g18.exe", shell=True)
                    call("TASKKILL /F /IM g19.exe", shell=True)
                if n1 == 20:
                    call("TASKKILL /F /IM g1.exe", shell=True)
                    call("TASKKILL /F /IM g2.exe", shell=True)
                    call("TASKKILL /F /IM g3.exe", shell=True)
                    call("TASKKILL /F /IM g4.exe", shell=True)
                    call("TASKKILL /F /IM g5.exe", shell=True)
                    call("TASKKILL /F /IM g6.exe", shell=True)
                    call("TASKKILL /F /IM g7.exe", shell=True)
                    call("TASKKILL /F /IM g8.exe", shell=True)
                    call("TASKKILL /F /IM g9.exe", shell=True)
                    call("TASKKILL /F /IM g10.exe", shell=True)
                    call("TASKKILL /F /IM g11.exe", shell=True)
                    call("TASKKILL /F /IM g12.exe", shell=True)
                    call("TASKKILL /F /IM g13.exe", shell=True)
                    call("TASKKILL /F /IM g14.exe", shell=True)
                    call("TASKKILL /F /IM g15.exe", shell=True)
                    call("TASKKILL /F /IM g16.exe", shell=True)
                    call("TASKKILL /F /IM g17.exe", shell=True)
                    call("TASKKILL /F /IM g18.exe", shell=True)
                    call("TASKKILL /F /IM g19.exe", shell=True)
                    call("TASKKILL /F /IM g20.exe", shell=True)

            win.destroy()
            c.execute("DELETE FROM t_m_t")
            c.execute("DELETE FROM t_t")
            c.execute("DELETE FROM fail")
            c.execute("DELETE FROM spam_number")
            c.execute("DELETE FROM g_p_t")
            con.commit()

            # doing some stuff when closing


# ------------------------------ start and stop ------------------------------------
def stop_f():  # we need to kill ghosts gmails
    global var_a, v_run
    var_a = False
    v_run = False  # kill the spamming running by checking fails
    ############## OUT PUT TIME AND SPAM AMOUNT
    l4 = ">>>   Stopped at " + str(datetime.now())
    c.execute("SELECT *,oid FROM spam_number")
    w = c.fetchall()
    sp_nu = w[0][0]
    l5 = ">>>   Sent " + str(sp_nu) + " Message"
    Label(win, text=l4, fg="white", bg="black", font=3).grid(
        row=9, column=0, columnspan=4, sticky="w"
    )
    Label(win, text=l5, fg="white", bg="black", font=3).grid(
        row=10, column=0, columnspan=4, sticky="w"
    )

    # ----
    start_b.configure(
        state=NORMAL
    )  # give time and how much messages nad kill the ghosts
    stop_b.configure(state=DISABLED)  # ---------ENABLING FOR NEXT SET-------
    show_b.configure(state=DISABLED)
    add_b.configure(state=NORMAL)
    e_target.configure(state=NORMAL)
    e_msg.configure(state=NORMAL)
    e_s.configure(state=NORMAL)
    c1.configure(state=NORMAL)
    r_ghosts.configure(state=NORMAL)
    r_gmails.configure(state=NORMAL)
    o_ghosts.configure(state=NORMAL)
    o_gmails.configure(state=NORMAL)
    # --------------------------------PROGRAM---------------
    # ----------------------KILING GHOSTS WHEN STOPPING----------------------
    if r.get() == 1:  # ghosts run
        pass
        n = drop_gh.get()
        if n == 1:  # ex if 3 open g1 g2 g3
            call("TASKKILL /F /IM g_0.exe", shell=True)
        if n == 2:
            call("TASKKILL /F /IM g_0.exe", shell=True)
            call("TASKKILL /F /IM g_1.exe", shell=True)
        if n == 3:
            call("TASKKILL /F /IM g_0.exe", shell=True)
            call("TASKKILL /F /IM g_1.exe", shell=True)
            call("TASKKILL /F /IM g_2.exe", shell=True)
        if n == 4:
            call("TASKKILL /F /IM g_0.exe", shell=True)
            call("TASKKILL /F /IM g_1.exe", shell=True)
            call("TASKKILL /F /IM g_2.exe", shell=True)
            call("TASKKILL /F /IM g_3.exe", shell=True)
        if n == 5:
            call("TASKKILL /F /IM g_0.exe", shell=True)
            call("TASKKILL /F /IM g_1.exe", shell=True)
            call("TASKKILL /F /IM g_2.exe", shell=True)
            call("TASKKILL /F /IM g_3.exe", shell=True)
            call("TASKKILL /F /IM g_4.exe", shell=True)
        if n == 6:
            call("TASKKILL /F /IM g_0.exe", shell=True)
            call("TASKKILL /F /IM g_1.exe", shell=True)
            call("TASKKILL /F /IM g_2.exe", shell=True)
            call("TASKKILL /F /IM g_3.exe", shell=True)
            call("TASKKILL /F /IM g_4.exe", shell=True)
            call("TASKKILL /F /IM g_5.exe", shell=True)
        if n == 7:
            call("TASKKILL /F /IM g_0.exe", shell=True)
            call("TASKKILL /F /IM g_1.exe", shell=True)
            call("TASKKILL /F /IM g_2.exe", shell=True)
            call("TASKKILL /F /IM g_3.exe", shell=True)
            call("TASKKILL /F /IM g_4.exe", shell=True)
            call("TASKKILL /F /IM g_5.exe", shell=True)
            call("TASKKILL /F /IM g_6.exe", shell=True)
        if n == 8:
            call("TASKKILL /F /IM g_0.exe", shell=True)
            call("TASKKILL /F /IM g_1.exe", shell=True)
            call("TASKKILL /F /IM g_2.exe", shell=True)
            call("TASKKILL /F /IM g_3.exe", shell=True)
            call("TASKKILL /F /IM g_4.exe", shell=True)
            call("TASKKILL /F /IM g_5.exe", shell=True)
            call("TASKKILL /F /IM g_6.exe", shell=True)
            call("TASKKILL /F /IM g_7.exe", shell=True)

        if n == 9:
            call("TASKKILL /F /IM g_0.exe", shell=True)
            call("TASKKILL /F /IM g_1.exe", shell=True)
            call("TASKKILL /F /IM g_2.exe", shell=True)
            call("TASKKILL /F /IM g_3.exe", shell=True)
            call("TASKKILL /F /IM g_4.exe", shell=True)
            call("TASKKILL /F /IM g_5.exe", shell=True)
            call("TASKKILL /F /IM g_6.exe", shell=True)
            call("TASKKILL /F /IM g_7.exe", shell=True)
            call("TASKKILL /F /IM g_8.exe", shell=True)
        if n == 10:
            call("TASKKILL /F /IM g_0.exe", shell=True)
            call("TASKKILL /F /IM g_1.exe", shell=True)
            call("TASKKILL /F /IM g_2.exe", shell=True)
            call("TASKKILL /F /IM g_3.exe", shell=True)
            call("TASKKILL /F /IM g_4.exe", shell=True)
            call("TASKKILL /F /IM g_5.exe", shell=True)
            call("TASKKILL /F /IM g_6.exe", shell=True)
            call("TASKKILL /F /IM g_7.exe", shell=True)
            call("TASKKILL /F /IM g_8.exe", shell=True)
            call("TASKKILL /F /IM g_9.exe", shell=True)

    if r.get() == 2:  # gmails run
        pass
        n1 = drop_gm.get()
        if n1 == 1:
            call("TASKKILL /F /IM g1.exe", shell=True)
        if n1 == 2:
            call("TASKKILL /F /IM g1.exe", shell=True)
            call("TASKKILL /F /IM g2.exe", shell=True)
        if n1 == 3:
            call("TASKKILL /F /IM g1.exe", shell=True)
            call("TASKKILL /F /IM g2.exe", shell=True)
            call("TASKKILL /F /IM g3.exe", shell=True)
        if n1 == 4:
            call("TASKKILL /F /IM g1.exe", shell=True)
            call("TASKKILL /F /IM g2.exe", shell=True)
            call("TASKKILL /F /IM g3.exe", shell=True)
            call("TASKKILL /F /IM g4.exe", shell=True)
        if n1 == 5:
            call("TASKKILL /F /IM g1.exe", shell=True)
            call("TASKKILL /F /IM g2.exe", shell=True)
            call("TASKKILL /F /IM g3.exe", shell=True)
            call("TASKKILL /F /IM g4.exe", shell=True)
            call("TASKKILL /F /IM g5.exe", shell=True)
        if n1 == 6:
            call("TASKKILL /F /IM g1.exe", shell=True)
            call("TASKKILL /F /IM g2.exe", shell=True)
            call("TASKKILL /F /IM g3.exe", shell=True)
            call("TASKKILL /F /IM g4.exe", shell=True)
            call("TASKKILL /F /IM g5.exe", shell=True)
            call("TASKKILL /F /IM g6.exe", shell=True)
        if n1 == 7:
            call("TASKKILL /F /IM g1.exe", shell=True)
            call("TASKKILL /F /IM g2.exe", shell=True)
            call("TASKKILL /F /IM g3.exe", shell=True)
            call("TASKKILL /F /IM g4.exe", shell=True)
            call("TASKKILL /F /IM g5.exe", shell=True)
            call("TASKKILL /F /IM g6.exe", shell=True)
            call("TASKKILL /F /IM g7.exe", shell=True)
        if n1 == 8:
            call("TASKKILL /F /IM g1.exe", shell=True)
            call("TASKKILL /F /IM g2.exe", shell=True)
            call("TASKKILL /F /IM g3.exe", shell=True)
            call("TASKKILL /F /IM g4.exe", shell=True)
            call("TASKKILL /F /IM g5.exe", shell=True)
            call("TASKKILL /F /IM g6.exe", shell=True)
            call("TASKKILL /F /IM g7.exe", shell=True)
            call("TASKKILL /F /IM g8.exe", shell=True)
        if n1 == 9:
            call("TASKKILL /F /IM g1.exe", shell=True)
            call("TASKKILL /F /IM g2.exe", shell=True)
            call("TASKKILL /F /IM g3.exe", shell=True)
            call("TASKKILL /F /IM g4.exe", shell=True)
            call("TASKKILL /F /IM g5.exe", shell=True)
            call("TASKKILL /F /IM g6.exe", shell=True)
            call("TASKKILL /F /IM g7.exe", shell=True)
            call("TASKKILL /F /IM g8.exe", shell=True)
            call("TASKKILL /F /IM g9.exe", shell=True)
        if n1 == 10:
            call("TASKKILL /F /IM g1.exe", shell=True)
            call("TASKKILL /F /IM g2.exe", shell=True)
            call("TASKKILL /F /IM g3.exe", shell=True)
            call("TASKKILL /F /IM g4.exe", shell=True)
            call("TASKKILL /F /IM g5.exe", shell=True)
            call("TASKKILL /F /IM g6.exe", shell=True)
            call("TASKKILL /F /IM g7.exe", shell=True)
            call("TASKKILL /F /IM g8.exe", shell=True)
            call("TASKKILL /F /IM g9.exe", shell=True)
            call("TASKKILL /F /IM g10.exe", shell=True)
        if n1 == 11:
            call("TASKKILL /F /IM g1.exe", shell=True)
            call("TASKKILL /F /IM g2.exe", shell=True)
            call("TASKKILL /F /IM g3.exe", shell=True)
            call("TASKKILL /F /IM g4.exe", shell=True)
            call("TASKKILL /F /IM g5.exe", shell=True)
            call("TASKKILL /F /IM g6.exe", shell=True)
            call("TASKKILL /F /IM g7.exe", shell=True)
            call("TASKKILL /F /IM g8.exe", shell=True)
            call("TASKKILL /F /IM g9.exe", shell=True)
            call("TASKKILL /F /IM g10.exe", shell=True)
            call("TASKKILL /F /IM g11.exe", shell=True)

        if n1 == 12:
            call("TASKKILL /F /IM g1.exe", shell=True)
            call("TASKKILL /F /IM g2.exe", shell=True)
            call("TASKKILL /F /IM g3.exe", shell=True)
            call("TASKKILL /F /IM g4.exe", shell=True)
            call("TASKKILL /F /IM g5.exe", shell=True)
            call("TASKKILL /F /IM g6.exe", shell=True)
            call("TASKKILL /F /IM g7.exe", shell=True)
            call("TASKKILL /F /IM g8.exe", shell=True)
            call("TASKKILL /F /IM g9.exe", shell=True)
            call("TASKKILL /F /IM g10.exe", shell=True)
            call("TASKKILL /F /IM g11.exe", shell=True)
            call("TASKKILL /F /IM g12.exe", shell=True)

        if n1 == 13:
            call("TASKKILL /F /IM g1.exe", shell=True)
            call("TASKKILL /F /IM g2.exe", shell=True)
            call("TASKKILL /F /IM g3.exe", shell=True)
            call("TASKKILL /F /IM g4.exe", shell=True)
            call("TASKKILL /F /IM g5.exe", shell=True)
            call("TASKKILL /F /IM g6.exe", shell=True)
            call("TASKKILL /F /IM g7.exe", shell=True)
            call("TASKKILL /F /IM g8.exe", shell=True)
            call("TASKKILL /F /IM g9.exe", shell=True)
            call("TASKKILL /F /IM g10.exe", shell=True)
            call("TASKKILL /F /IM g11.exe", shell=True)
            call("TASKKILL /F /IM g12.exe", shell=True)
            call("TASKKILL /F /IM g13.exe", shell=True)
        if n1 == 14:
            call("TASKKILL /F /IM g1.exe", shell=True)
            call("TASKKILL /F /IM g2.exe", shell=True)
            call("TASKKILL /F /IM g3.exe", shell=True)
            call("TASKKILL /F /IM g4.exe", shell=True)
            call("TASKKILL /F /IM g5.exe", shell=True)
            call("TASKKILL /F /IM g6.exe", shell=True)
            call("TASKKILL /F /IM g7.exe", shell=True)
            call("TASKKILL /F /IM g8.exe", shell=True)
            call("TASKKILL /F /IM g9.exe", shell=True)
            call("TASKKILL /F /IM g10.exe", shell=True)
            call("TASKKILL /F /IM g11.exe", shell=True)
            call("TASKKILL /F /IM g12.exe", shell=True)
            call("TASKKILL /F /IM g13.exe", shell=True)
            call("TASKKILL /F /IM g14.exe", shell=True)
        if n1 == 15:
            call("TASKKILL /F /IM g1.exe", shell=True)
            call("TASKKILL /F /IM g2.exe", shell=True)
            call("TASKKILL /F /IM g3.exe", shell=True)
            call("TASKKILL /F /IM g4.exe", shell=True)
            call("TASKKILL /F /IM g5.exe", shell=True)
            call("TASKKILL /F /IM g6.exe", shell=True)
            call("TASKKILL /F /IM g7.exe", shell=True)
            call("TASKKILL /F /IM g8.exe", shell=True)
            call("TASKKILL /F /IM g9.exe", shell=True)
            call("TASKKILL /F /IM g10.exe", shell=True)
            call("TASKKILL /F /IM g11.exe", shell=True)
            call("TASKKILL /F /IM g12.exe", shell=True)
            call("TASKKILL /F /IM g13.exe", shell=True)
            call("TASKKILL /F /IM g14.exe", shell=True)
            call("TASKKILL /F /IM g15.exe", shell=True)
        if n1 == 16:
            call("TASKKILL /F /IM g1.exe", shell=True)
            call("TASKKILL /F /IM g2.exe", shell=True)
            call("TASKKILL /F /IM g3.exe", shell=True)
            call("TASKKILL /F /IM g4.exe", shell=True)
            call("TASKKILL /F /IM g5.exe", shell=True)
            call("TASKKILL /F /IM g6.exe", shell=True)
            call("TASKKILL /F /IM g7.exe", shell=True)
            call("TASKKILL /F /IM g8.exe", shell=True)
            call("TASKKILL /F /IM g9.exe", shell=True)
            call("TASKKILL /F /IM g10.exe", shell=True)
            call("TASKKILL /F /IM g11.exe", shell=True)
            call("TASKKILL /F /IM g12.exe", shell=True)
            call("TASKKILL /F /IM g13.exe", shell=True)
            call("TASKKILL /F /IM g14.exe", shell=True)
            call("TASKKILL /F /IM g15.exe", shell=True)
            call("TASKKILL /F /IM g16.exe", shell=True)
        if n1 == 17:
            call("TASKKILL /F /IM g1.exe", shell=True)
            call("TASKKILL /F /IM g2.exe", shell=True)
            call("TASKKILL /F /IM g3.exe", shell=True)
            call("TASKKILL /F /IM g4.exe", shell=True)
            call("TASKKILL /F /IM g5.exe", shell=True)
            call("TASKKILL /F /IM g6.exe", shell=True)
            call("TASKKILL /F /IM g7.exe", shell=True)
            call("TASKKILL /F /IM g8.exe", shell=True)
            call("TASKKILL /F /IM g9.exe", shell=True)
            call("TASKKILL /F /IM g10.exe", shell=True)
            call("TASKKILL /F /IM g11.exe", shell=True)
            call("TASKKILL /F /IM g12.exe", shell=True)
            call("TASKKILL /F /IM g13.exe", shell=True)
            call("TASKKILL /F /IM g14.exe", shell=True)
            call("TASKKILL /F /IM g15.exe", shell=True)
            call("TASKKILL /F /IM g16.exe", shell=True)
            call("TASKKILL /F /IM g17.exe", shell=True)
        if n1 == 18:
            call("TASKKILL /F /IM g1.exe", shell=True)
            call("TASKKILL /F /IM g2.exe", shell=True)
            call("TASKKILL /F /IM g3.exe", shell=True)
            call("TASKKILL /F /IM g4.exe", shell=True)
            call("TASKKILL /F /IM g5.exe", shell=True)
            call("TASKKILL /F /IM g6.exe", shell=True)
            call("TASKKILL /F /IM g7.exe", shell=True)
            call("TASKKILL /F /IM g8.exe", shell=True)
            call("TASKKILL /F /IM g9.exe", shell=True)
            call("TASKKILL /F /IM g10.exe", shell=True)
            call("TASKKILL /F /IM g11.exe", shell=True)
            call("TASKKILL /F /IM g12.exe", shell=True)
            call("TASKKILL /F /IM g13.exe", shell=True)
            call("TASKKILL /F /IM g14.exe", shell=True)
            call("TASKKILL /F /IM g15.exe", shell=True)
            call("TASKKILL /F /IM g16.exe", shell=True)
            call("TASKKILL /F /IM g17.exe", shell=True)
            call("TASKKILL /F /IM g18.exe", shell=True)
        if n1 == 19:
            call("TASKKILL /F /IM g1.exe", shell=True)
            call("TASKKILL /F /IM g2.exe", shell=True)
            call("TASKKILL /F /IM g3.exe", shell=True)
            call("TASKKILL /F /IM g4.exe", shell=True)
            call("TASKKILL /F /IM g5.exe", shell=True)
            call("TASKKILL /F /IM g6.exe", shell=True)
            call("TASKKILL /F /IM g7.exe", shell=True)
            call("TASKKILL /F /IM g8.exe", shell=True)
            call("TASKKILL /F /IM g9.exe", shell=True)
            call("TASKKILL /F /IM g10.exe", shell=True)
            call("TASKKILL /F /IM g11.exe", shell=True)
            call("TASKKILL /F /IM g12.exe", shell=True)
            call("TASKKILL /F /IM g13.exe", shell=True)
            call("TASKKILL /F /IM g14.exe", shell=True)
            call("TASKKILL /F /IM g15.exe", shell=True)
            call("TASKKILL /F /IM g16.exe", shell=True)
            call("TASKKILL /F /IM g17.exe", shell=True)
            call("TASKKILL /F /IM g18.exe", shell=True)
            call("TASKKILL /F /IM g19.exe", shell=True)
        if n1 == 20:
            call("TASKKILL /F /IM g1.exe", shell=True)
            call("TASKKILL /F /IM g2.exe", shell=True)
            call("TASKKILL /F /IM g3.exe", shell=True)
            call("TASKKILL /F /IM g4.exe", shell=True)
            call("TASKKILL /F /IM g5.exe", shell=True)
            call("TASKKILL /F /IM g6.exe", shell=True)
            call("TASKKILL /F /IM g7.exe", shell=True)
            call("TASKKILL /F /IM g8.exe", shell=True)
            call("TASKKILL /F /IM g9.exe", shell=True)
            call("TASKKILL /F /IM g10.exe", shell=True)
            call("TASKKILL /F /IM g11.exe", shell=True)
            call("TASKKILL /F /IM g12.exe", shell=True)
            call("TASKKILL /F /IM g13.exe", shell=True)
            call("TASKKILL /F /IM g14.exe", shell=True)
            call("TASKKILL /F /IM g15.exe", shell=True)
            call("TASKKILL /F /IM g16.exe", shell=True)
            call("TASKKILL /F /IM g17.exe", shell=True)
            call("TASKKILL /F /IM g18.exe", shell=True)
            call("TASKKILL /F /IM g19.exe", shell=True)
            call("TASKKILL /F /IM g20.exe", shell=True)

    # ------------------------------- DELETE INFORMATIONS AT STOP --------------------------------
    c.execute("DELETE FROM t_m_t")
    c.execute("DELETE FROM t_t")
    c.execute("DELETE FROM fail")
    con.commit()


def start_f():  # send all infos in database,launch ghosts,
    global var_a
    # reseting the spam number
    if str(e_target.get()) == "xghostdevloper98582989oussema":
        messagebox.showinfo(
            "DEVLOPER",
            "The Devloper of this program is Oussema Nehdi son of Adel Nehdi from Tunisia to contact him :  oussamabejaoui1234@gmail.com ",
        )
    c.execute("INSERT INTO fail VALUES (:fail_number)", {"fail_number": 0})
    con.commit()
    #################### Deleting output to be ready for next operation ############
    Label(
        win,
        text=">>>                                                                                                                   ",
        fg="white",
        bg="black",
        font=3,
    ).grid(row=7, column=0, columnspan=4, sticky="w")
    Label(
        win,
        text=">>>                                                                                                                   ",
        fg="white",
        bg="black",
        font=3,
    ).grid(row=8, column=0, columnspan=4, sticky="w")
    Label(
        win,
        text=">>>                                                                                                                   ",
        fg="white",
        bg="black",
        font=3,
    ).grid(row=9, column=0, columnspan=4, sticky="w")
    Label(
        win,
        text=">>>                                                                                                                   ",
        fg="white",
        bg="black",
        font=3,
    ).grid(row=10, column=0, columnspan=4, sticky="w")
    ################################################
    ping = call("ping -n 1 google.com", shell=True)
    if ping == 1:
        messagebox.showerror("", "There is no Internet connection")  # NO network.
    else:  # THERE IS NETWORK
        is_valid = validate_email(e_target.get())
        if is_valid == True:

            def loop_ghosts():
                try:
                    c.execute("SELECT *,oid FROM fail")
                    fnc = c.fetchall()
                    fn = fnc[0][0]
                except:
                    pass
                else:
                    if fn == drop_gh.get():
                        stop_f()
                    else:
                        print("fails are ", fn)
                        print("drop_gh is", drop_gh.get())
                        win.after(10000, loop_ghosts)

            def loop_gmails():
                try:
                    c.execute("SELECT *,oid FROM fail")
                    fnc = c.fetchall()
                    fn = fnc[0][0]
                except:
                    pass
                else:
                    if fn == drop_gm.get():
                        stop_f()
                    else:
                        print("fails are ", fn)
                        print("drop_gh is", drop_gh.get())
                        win.after(10000, loop_gmails)

            ################" PUT THE TIME AND SPAMMING WHO"
            if int(var_c1.get()) == 1:
                try:
                    abs(int(e_s.get()))
                except:
                    c_n = False
                else:
                    c_n = True
                if c_n == True:
                    var_a = True
                    timenow = datetime.now()
                    l2 = ">>>   Started at " + str(timenow)
                    l3 = ">>>   Spamming " + str(e_target.get()) + " ..."
                    Label(win, text=l2, fg="white", bg="black", font=3).grid(
                        row=7, column=0, columnspan=4, sticky="w"
                    )
                    Label(win, text=l3, fg="white", bg="black", font=3).grid(
                        row=8, column=0, columnspan=4, sticky="w"
                    )

                    stop_b.configure(
                        state=NORMAL
                    )  # ----------DISABLING FOR NO ERRORS-------
                    show_b.configure(state=NORMAL)
                    start_b.configure(state=DISABLED)
                    add_b.configure(state=DISABLED)
                    e_target.configure(state=DISABLED)
                    e_msg.configure(state=DISABLED)
                    e_s.configure(state=DISABLED)
                    c1.configure(state=DISABLED)
                    r_ghosts.configure(state=DISABLED)
                    r_gmails.configure(state=DISABLED)
                    o_ghosts.configure(state=DISABLED)
                    o_gmails.configure(state=DISABLED)
                    # --------------------------ALL THE WORK ON START--------------
                    target_v = e_target.get()
                    msg_v = e_msg.get()
                    on_of_v = var_c1.get()
                    seconds_v = e_s.get()
                    c.execute(
                        "INSERT INTO t_m_t VALUES (:target,:msg)",
                        {"target": target_v, "msg": msg_v},
                    )  # puting target and msg
                    c.execute(
                        "INSERT INTO t_t VALUES (:on_of,:seconds)",
                        {"on_of": on_of_v, "seconds": seconds_v},
                    )  # puting if time is on and puting seconds if its rly on
                    c.execute(
                        "INSERT INTO fail VALUES (:fail_number)", {"fail_number": 0}
                    )
                    c.execute("INSERT INTO spam_number VALUES (:spam_n)", {"spam_n": 0})
                    con.commit()
                    # ------------------------RUNNING PROGRAMMS-----------------------
                    if r.get() == 1:  # ghosts run
                        pass
                        n = drop_gh.get()
                        if n == 1:  # ex if 3 open g1 g2 g3
                            Popen("ghosts/g_0.exe")
                        if n == 2:
                            Popen("ghosts/g_0.exe")
                            Popen("ghosts/g_1.exe")
                        if n == 3:
                            Popen("ghosts/g_0.exe")
                            Popen("ghosts/g_1.exe")
                            Popen("ghosts/g_2.exe")
                        if n == 4:
                            Popen("ghosts/g_0.exe")
                            Popen("ghosts/g_1.exe")
                            Popen("ghosts/g_2.exe")
                            Popen("ghosts/g_3.exe")
                        if n == 5:
                            Popen("ghosts/g_0.exe")
                            Popen("ghosts/g_1.exe")
                            Popen("ghosts/g_2.exe")
                            Popen("ghosts/g_3.exe")
                            Popen("ghosts/g_4.exe")
                        if n == 6:
                            Popen("ghosts/g_0.exe")
                            Popen("ghosts/g_1.exe")
                            Popen("ghosts/g_2.exe")
                            Popen("ghosts/g_3.exe")
                            Popen("ghosts/g_4.exe")
                            Popen("ghosts/g_5.exe")
                        if n == 7:
                            Popen("ghosts/g_0.exe")
                            Popen("ghosts/g_1.exe")
                            Popen("ghosts/g_2.exe")
                            Popen("ghosts/g_3.exe")
                            Popen("ghosts/g_4.exe")
                            Popen("ghosts/g_5.exe")
                            Popen("ghosts/g_6.exe")
                        if n == 8:
                            Popen("ghosts/g_0.exe")
                            Popen("ghosts/g_1.exe")
                            Popen("ghosts/g_2.exe")
                            Popen("ghosts/g_3.exe")
                            Popen("ghosts/g_4.exe")
                            Popen("ghosts/g_5.exe")
                            Popen("ghosts/g_6.exe")
                            Popen("ghosts/g_7.exe")
                        if n == 9:
                            Popen("ghosts/g_0.exe")
                            Popen("ghosts/g_1.exe")
                            Popen("ghosts/g_2.exe")
                            Popen("ghosts/g_3.exe")
                            Popen("ghosts/g_4.exe")
                            Popen("ghosts/g_5.exe")
                            Popen("ghosts/g_6.exe")
                            Popen("ghosts/g_7.exe")
                            Popen("ghosts/g_8.exe")
                        if n == 10:
                            Popen("ghosts/g_0.exe")
                            Popen("ghosts/g_1.exe")
                            Popen("ghosts/g_2.exe")
                            Popen("ghosts/g_3.exe")
                            Popen("ghosts/g_4.exe")
                            Popen("ghosts/g_5.exe")
                            Popen("ghosts/g_6.exe")
                            Popen("ghosts/g_7.exe")
                            Popen("ghosts/g_8.exe")
                            Popen("ghosts/g_9.exe")
                        win.after(10000, loop_ghosts)

                    if r.get() == 2:  # gmails run
                        pass
                        n1 = drop_gm.get()
                        if n1 == 1:
                            Popen("ghosts/g1.exe")
                        if n1 == 2:
                            Popen("ghosts/g1.exe")
                            Popen("ghosts/g2.exe")
                        if n1 == 3:
                            Popen("ghosts/g1.exe")
                            Popen("ghosts/g2.exe")
                            Popen("ghosts/g3.exe")
                        if n1 == 4:
                            Popen("ghosts/g1.exe")
                            Popen("ghosts/g2.exe")
                            Popen("ghosts/g3.exe")
                            Popen("ghosts/g4.exe")
                        if n1 == 5:
                            Popen("ghosts/g1.exe")
                            Popen("ghosts/g2.exe")
                            Popen("ghosts/g3.exe")
                            Popen("ghosts/g4.exe")
                            Popen("ghosts/g5.exe")
                        if n1 == 6:
                            Popen("ghosts/g1.exe")
                            Popen("ghosts/g2.exe")
                            Popen("ghosts/g3.exe")
                            Popen("ghosts/g4.exe")
                            Popen("ghosts/g5.exe")
                            Popen("ghosts/g6.exe")
                        if n1 == 7:
                            Popen("ghosts/g1.exe")
                            Popen("ghosts/g2.exe")
                            Popen("ghosts/g3.exe")
                            Popen("ghosts/g4.exe")
                            Popen("ghosts/g5.exe")
                            Popen("ghosts/g6.exe")
                            Popen("ghosts/g7.exe")
                        if n1 == 8:
                            Popen("ghosts/g1.exe")
                            Popen("ghosts/g2.exe")
                            Popen("ghosts/g3.exe")
                            Popen("ghosts/g4.exe")
                            Popen("ghosts/g5.exe")
                            Popen("ghosts/g7.exe")
                            Popen("ghosts/g8.exe")
                        if n1 == 9:
                            Popen("ghosts/g1.exe")
                            Popen("ghosts/g2.exe")
                            Popen("ghosts/g3.exe")
                            Popen("ghosts/g4.exe")
                            Popen("ghosts/g5.exe")
                            Popen("ghosts/g6.exe")
                            Popen("ghosts/g7.exe")
                            Popen("ghosts/g8.exe")
                            Popen("ghosts/g9.exe")
                        if n1 == 10:
                            Popen("ghosts/g1.exe")
                            Popen("ghosts/g2.exe")
                            Popen("ghosts/g3.exe")
                            Popen("ghosts/g4.exe")
                            Popen("ghosts/g5.exe")
                            Popen("ghosts/g6.exe")
                            Popen("ghosts/g7.exe")
                            Popen("ghosts/g8.exe")
                            Popen("ghosts/g9.exe")
                            Popen("ghosts/g10.exe")
                        if n1 == 11:
                            Popen("ghosts/g1.exe")
                            Popen("ghosts/g2.exe")
                            Popen("ghosts/g3.exe")
                            Popen("ghosts/g4.exe")
                            Popen("ghosts/g5.exe")
                            Popen("ghosts/g6.exe")
                            Popen("ghosts/g7.exe")
                            Popen("ghosts/g8.exe")
                            Popen("ghosts/g9.exe")
                            Popen("ghosts/g10.exe")
                            Popen("ghosts/g11.exe")

                        if n1 == 12:
                            Popen("ghosts/g1.exe")
                            Popen("ghosts/g2.exe")
                            Popen("ghosts/g3.exe")
                            Popen("ghosts/g4.exe")
                            Popen("ghosts/g5.exe")
                            Popen("ghosts/g6.exe")
                            Popen("ghosts/g7.exe")
                            Popen("ghosts/g8.exe")
                            Popen("ghosts/g9.exe")
                            Popen("ghosts/g10.exe")
                            Popen("ghosts/g11.exe")
                            Popen("ghosts/g12.exe")

                        if n1 == 13:
                            Popen("ghosts/g1.exe")
                            Popen("ghosts/g2.exe")
                            Popen("ghosts/g3.exe")
                            Popen("ghosts/g4.exe")
                            Popen("ghosts/g5.exe")
                            Popen("ghosts/g6.exe")
                            Popen("ghosts/g7.exe")
                            Popen("ghosts/g8.exe")
                            Popen("ghosts/g9.exe")
                            Popen("ghosts/g10.exe")
                            Popen("ghosts/g11.exe")
                            Popen("ghosts/g12.exe")
                            Popen("ghosts/g13.exe")
                        if n1 == 14:
                            Popen("ghosts/g1.exe")
                            Popen("ghosts/g2.exe")
                            Popen("ghosts/g3.exe")
                            Popen("ghosts/g4.exe")
                            Popen("ghosts/g5.exe")
                            Popen("ghosts/g6.exe")
                            Popen("ghosts/g7.exe")
                            Popen("ghosts/g8.exe")
                            Popen("ghosts/g9.exe")
                            Popen("ghosts/g10.exe")
                            Popen("ghosts/g11.exe")
                            Popen("ghosts/g12.exe")
                            Popen("ghosts/g13.exe")
                            Popen("ghosts/g14.exe")
                        if n1 == 15:
                            Popen("ghosts/g1.exe")
                            Popen("ghosts/g2.exe")
                            Popen("ghosts/g3.exe")
                            Popen("ghosts/g4.exe")
                            Popen("ghosts/g5.exe")
                            Popen("ghosts/g6.exe")
                            Popen("ghosts/g7.exe")
                            Popen("ghosts/g8.exe")
                            Popen("ghosts/g9.exe")
                            Popen("ghosts/g10.exe")
                            Popen("ghosts/g11.exe")
                            Popen("ghosts/g12.exe")
                            Popen("ghosts/g13.exe")
                            Popen("ghosts/g14.exe")
                            Popen("ghosts/g15.exe")
                        if n1 == 16:
                            Popen("ghosts/g1.exe")
                            Popen("ghosts/g2.exe")
                            Popen("ghosts/g3.exe")
                            Popen("ghosts/g4.exe")
                            Popen("ghosts/g5.exe")
                            Popen("ghosts/g6.exe")
                            Popen("ghosts/g7.exe")
                            Popen("ghosts/g8.exe")
                            Popen("ghosts/g9.exe")
                            Popen("ghosts/g10.exe")
                            Popen("ghosts/g11.exe")
                            Popen("ghosts/g12.exe")
                            Popen("ghosts/g13.exe")
                            Popen("ghosts/g14.exe")
                            Popen("ghosts/g15.exe")
                            Popen("ghosts/g16.exe")
                        if n1 == 17:
                            Popen("ghosts/g1.exe")
                            Popen("ghosts/g2.exe")
                            Popen("ghosts/g3.exe")
                            Popen("ghosts/g4.exe")
                            Popen("ghosts/g5.exe")
                            Popen("ghosts/g6.exe")
                            Popen("ghosts/g7.exe")
                            Popen("ghosts/g8.exe")
                            Popen("ghosts/g9.exe")
                            Popen("ghosts/g10.exe")
                            Popen("ghosts/g11.exe")
                            Popen("ghosts/g12.exe")
                            Popen("ghosts/g13.exe")
                            Popen("ghosts/g14.exe")
                            Popen("ghosts/g15.exe")
                            Popen("ghosts/g16.exe")
                            Popen("ghosts/g17.exe")
                        if n1 == 18:
                            Popen("ghosts/g1.exe")
                            Popen("ghosts/g2.exe")
                            Popen("ghosts/g3.exe")
                            Popen("ghosts/g4.exe")
                            Popen("ghosts/g5.exe")
                            Popen("ghosts/g6.exe")
                            Popen("ghosts/g7.exe")
                            Popen("ghosts/g8.exe")
                            Popen("ghosts/g9.exe")
                            Popen("ghosts/g10.exe")
                            Popen("ghosts/g11.exe")
                            Popen("ghosts/g12.exe")
                            Popen("ghosts/g13.exe")
                            Popen("ghosts/g14.exe")
                            Popen("ghosts/g15.exe")
                            Popen("ghosts/g16.exe")
                            Popen("ghosts/g17.exe")
                            Popen("ghosts/g18.exe")
                        if n1 == 19:
                            Popen("ghosts/g1.exe")
                            Popen("ghosts/g2.exe")
                            Popen("ghosts/g3.exe")
                            Popen("ghosts/g4.exe")
                            Popen("ghosts/g5.exe")
                            Popen("ghosts/g6.exe")
                            Popen("ghosts/g7.exe")
                            Popen("ghosts/g8.exe")
                            Popen("ghosts/g9.exe")
                            Popen("ghosts/g10.exe")
                            Popen("ghosts/g11.exe")
                            Popen("ghosts/g12.exe")
                            Popen("ghosts/g13.exe")
                            Popen("ghosts/g14.exe")
                            Popen("ghosts/g15.exe")
                            Popen("ghosts/g16.exe")
                            Popen("ghosts/g17.exe")
                            Popen("ghosts/g18.exe")
                            Popen("ghosts/g19.exe")
                        if n1 == 20:
                            Popen("ghosts/g1.exe")
                            Popen("ghosts/g2.exe")
                            Popen("ghosts/g3.exe")
                            Popen("ghosts/g4.exe")
                            Popen("ghosts/g5.exe")
                            Popen("ghosts/g6.exe")
                            Popen("ghosts/g7.exe")
                            Popen("ghosts/g8.exe")
                            Popen("ghosts/g9.exe")
                            Popen("ghosts/g10.exe")
                            Popen("ghosts/g11.exe")
                            Popen("ghosts/g12.exe")
                            Popen("ghosts/g13.exe")
                            Popen("ghosts/g14.exe")
                            Popen("ghosts/g15.exe")
                            Popen("ghosts/g16.exe")
                            Popen("ghosts/g17.exe")
                            Popen("ghosts/g18.exe")
                            Popen("ghosts/g19.exe")
                            Popen("ghosts/g20.exe")
                        win.after(10000, loop_gmails)
                else:
                    messagebox.showerror("", "Time Delay must be a number")

            else:
                var_a = True
                timenow = datetime.now()
                l2 = ">>>   Started at " + str(timenow)
                l3 = ">>>   Spamming " + str(e_target.get()) + " ..."
                Label(win, text=l2, fg="white", bg="black", font=3).grid(
                    row=7, column=0, columnspan=4, sticky="w"
                )
                Label(win, text=l3, fg="white", bg="black", font=3).grid(
                    row=8, column=0, columnspan=4, sticky="w"
                )
                stop_b.configure(
                    state=NORMAL
                )  # ----------DISABLING FOR NO ERRORS-------
                show_b.configure(state=NORMAL)
                start_b.configure(state=DISABLED)
                add_b.configure(state=DISABLED)
                e_target.configure(state=DISABLED)
                e_msg.configure(state=DISABLED)
                e_s.configure(state=DISABLED)
                c1.configure(state=DISABLED)
                r_ghosts.configure(state=DISABLED)
                r_gmails.configure(state=DISABLED)
                o_ghosts.configure(state=DISABLED)
                o_gmails.configure(state=DISABLED)
                # --------------------------ALL THE WORK ON START--------------
                target_v = e_target.get()
                msg_v = e_msg.get()
                on_of_v = var_c1.get()
                seconds_v = e_s.get()
                c.execute(
                    "INSERT INTO t_m_t VALUES (:target,:msg)",
                    {"target": target_v, "msg": msg_v},
                )  # puting target and msg
                c.execute(
                    "INSERT INTO t_t VALUES (:on_of,:seconds)",
                    {"on_of": on_of_v, "seconds": seconds_v},
                )  # puting if time is on and puting seconds if its rly on
                c.execute("INSERT INTO fail VALUES (:fail_number)", {"fail_number": 0})
                c.execute("INSERT INTO spam_number VALUES (:spam_n)", {"spam_n": 0})
                con.commit()
                # ------------------------RUNNING PROGRAMMS-----------------------
                if r.get() == 1:  # ghosts run
                    pass
                    n = drop_gh.get()
                    if n == 1:  # ex if 3 open g1 g2 g3
                        Popen("ghosts/g_0.exe")
                    if n == 2:
                        Popen("ghosts/g_0.exe")
                        Popen("ghosts/g_1.exe")
                    if n == 3:
                        Popen("ghosts/g_0.exe")
                        Popen("ghosts/g_1.exe")
                        Popen("ghosts/g_2.exe")
                    if n == 4:
                        Popen("ghosts/g_0.exe")
                        Popen("ghosts/g_1.exe")
                        Popen("ghosts/g_2.exe")
                        Popen("ghosts/g_3.exe")
                    if n == 5:
                        Popen("ghosts/g_0.exe")
                        Popen("ghosts/g_1.exe")
                        Popen("ghosts/g_2.exe")
                        Popen("ghosts/g_3.exe")
                        Popen("ghosts/g_4.exe")
                    if n == 6:
                        Popen("ghosts/g_0.exe")
                        Popen("ghosts/g_1.exe")
                        Popen("ghosts/g_2.exe")
                        Popen("ghosts/g_3.exe")
                        Popen("ghosts/g_4.exe")
                        Popen("ghosts/g_5.exe")
                    if n == 7:
                        Popen("ghosts/g_0.exe")
                        Popen("ghosts/g_1.exe")
                        Popen("ghosts/g_2.exe")
                        Popen("ghosts/g_3.exe")
                        Popen("ghosts/g_4.exe")
                        Popen("ghosts/g_5.exe")
                        Popen("ghosts/g_6.exe")
                    if n == 8:
                        Popen("ghosts/g_0.exe")
                        Popen("ghosts/g_1.exe")
                        Popen("ghosts/g_2.exe")
                        Popen("ghosts/g_3.exe")
                        Popen("ghosts/g_4.exe")
                        Popen("ghosts/g_5.exe")
                        Popen("ghosts/g_6.exe")
                        Popen("ghosts/g_7.exe")
                    if n == 9:
                        Popen("ghosts/g_0.exe")
                        Popen("ghosts/g_1.exe")
                        Popen("ghosts/g_2.exe")
                        Popen("ghosts/g_3.exe")
                        Popen("ghosts/g_4.exe")
                        Popen("ghosts/g_5.exe")
                        Popen("ghosts/g_6.exe")
                        Popen("ghosts/g_7.exe")
                        Popen("ghosts/g_8.exe")
                    if n == 10:
                        Popen("ghosts/g_0.exe")
                        Popen("ghosts/g_1.exe")
                        Popen("ghosts/g_2.exe")
                        Popen("ghosts/g_3.exe")
                        Popen("ghosts/g_4.exe")
                        Popen("ghosts/g_5.exe")
                        Popen("ghosts/g_6.exe")
                        Popen("ghosts/g_7.exe")
                        Popen("ghosts/g_8.exe")
                        Popen("ghosts/g_9.exe")
                    win.after(10000, loop_ghosts)

                if r.get() == 2:  # gmails run
                    pass
                    n1 = drop_gm.get()
                    if n1 == 1:
                        Popen("ghosts/g1.exe")
                    if n1 == 2:
                        Popen("ghosts/g1.exe")
                        Popen("ghosts/g2.exe")
                    if n1 == 3:
                        Popen("ghosts/g1.exe")
                        Popen("ghosts/g2.exe")
                        Popen("ghosts/g3.exe")
                    if n1 == 4:
                        Popen("ghosts/g1.exe")
                        Popen("ghosts/g2.exe")
                        Popen("ghosts/g3.exe")
                        Popen("ghosts/g4.exe")
                    if n1 == 5:
                        Popen("ghosts/g1.exe")
                        Popen("ghosts/g2.exe")
                        Popen("ghosts/g3.exe")
                        Popen("ghosts/g4.exe")
                        Popen("ghosts/g5.exe")
                    if n1 == 6:
                        Popen("ghosts/g1.exe")
                        Popen("ghosts/g2.exe")
                        Popen("ghosts/g3.exe")
                        Popen("ghosts/g4.exe")
                        Popen("ghosts/g5.exe")
                        Popen("ghosts/g6.exe")
                    if n1 == 7:
                        Popen("ghosts/g1.exe")
                        Popen("ghosts/g2.exe")
                        Popen("ghosts/g3.exe")
                        Popen("ghosts/g4.exe")
                        Popen("ghosts/g5.exe")
                        Popen("ghosts/g6.exe")
                        Popen("ghosts/g7.exe")
                    if n1 == 8:
                        Popen("ghosts/g1.exe")
                        Popen("ghosts/g2.exe")
                        Popen("ghosts/g3.exe")
                        Popen("ghosts/g4.exe")
                        Popen("ghosts/g5.exe")
                        Popen("ghosts/g7.exe")
                        Popen("ghosts/g8.exe")
                    if n1 == 9:
                        Popen("ghosts/g1.exe")
                        Popen("ghosts/g2.exe")
                        Popen("ghosts/g3.exe")
                        Popen("ghosts/g4.exe")
                        Popen("ghosts/g5.exe")
                        Popen("ghosts/g6.exe")
                        Popen("ghosts/g7.exe")
                        Popen("ghosts/g8.exe")
                        Popen("ghosts/g9.exe")
                    if n1 == 10:
                        Popen("ghosts/g1.exe")
                        Popen("ghosts/g2.exe")
                        Popen("ghosts/g3.exe")
                        Popen("ghosts/g4.exe")
                        Popen("ghosts/g5.exe")
                        Popen("ghosts/g6.exe")
                        Popen("ghosts/g7.exe")
                        Popen("ghosts/g8.exe")
                        Popen("ghosts/g9.exe")
                        Popen("ghosts/g10.exe")
                    if n1 == 11:
                        Popen("ghosts/g1.exe")
                        Popen("ghosts/g2.exe")
                        Popen("ghosts/g3.exe")
                        Popen("ghosts/g4.exe")
                        Popen("ghosts/g5.exe")
                        Popen("ghosts/g6.exe")
                        Popen("ghosts/g7.exe")
                        Popen("ghosts/g8.exe")
                        Popen("ghosts/g9.exe")
                        Popen("ghosts/g10.exe")
                        Popen("ghosts/g11.exe")

                    if n1 == 12:
                        Popen("ghosts/g1.exe")
                        Popen("ghosts/g2.exe")
                        Popen("ghosts/g3.exe")
                        Popen("ghosts/g4.exe")
                        Popen("ghosts/g5.exe")
                        Popen("ghosts/g6.exe")
                        Popen("ghosts/g7.exe")
                        Popen("ghosts/g8.exe")
                        Popen("ghosts/g9.exe")
                        Popen("ghosts/g10.exe")
                        Popen("ghosts/g11.exe")
                        Popen("ghosts/g12.exe")

                    if n1 == 13:
                        Popen("ghosts/g1.exe")
                        Popen("ghosts/g2.exe")
                        Popen("ghosts/g3.exe")
                        Popen("ghosts/g4.exe")
                        Popen("ghosts/g5.exe")
                        Popen("ghosts/g6.exe")
                        Popen("ghosts/g7.exe")
                        Popen("ghosts/g8.exe")
                        Popen("ghosts/g9.exe")
                        Popen("ghosts/g10.exe")
                        Popen("ghosts/g11.exe")
                        Popen("ghosts/g12.exe")
                        Popen("ghosts/g13.exe")
                    if n1 == 14:
                        Popen("ghosts/g1.exe")
                        Popen("ghosts/g2.exe")
                        Popen("ghosts/g3.exe")
                        Popen("ghosts/g4.exe")
                        Popen("ghosts/g5.exe")
                        Popen("ghosts/g6.exe")
                        Popen("ghosts/g7.exe")
                        Popen("ghosts/g8.exe")
                        Popen("ghosts/g9.exe")
                        Popen("ghosts/g10.exe")
                        Popen("ghosts/g11.exe")
                        Popen("ghosts/g12.exe")
                        Popen("ghosts/g13.exe")
                        Popen("ghosts/g14.exe")
                    if n1 == 15:
                        Popen("ghosts/g1.exe")
                        Popen("ghosts/g2.exe")
                        Popen("ghosts/g3.exe")
                        Popen("ghosts/g4.exe")
                        Popen("ghosts/g5.exe")
                        Popen("ghosts/g6.exe")
                        Popen("ghosts/g7.exe")
                        Popen("ghosts/g8.exe")
                        Popen("ghosts/g9.exe")
                        Popen("ghosts/g10.exe")
                        Popen("ghosts/g11.exe")
                        Popen("ghosts/g12.exe")
                        Popen("ghosts/g13.exe")
                        Popen("ghosts/g14.exe")
                        Popen("ghosts/g15.exe")
                    if n1 == 16:
                        Popen("ghosts/g1.exe")
                        Popen("ghosts/g2.exe")
                        Popen("ghosts/g3.exe")
                        Popen("ghosts/g4.exe")
                        Popen("ghosts/g5.exe")
                        Popen("ghosts/g6.exe")
                        Popen("ghosts/g7.exe")
                        Popen("ghosts/g8.exe")
                        Popen("ghosts/g9.exe")
                        Popen("ghosts/g10.exe")
                        Popen("ghosts/g11.exe")
                        Popen("ghosts/g12.exe")
                        Popen("ghosts/g13.exe")
                        Popen("ghosts/g14.exe")
                        Popen("ghosts/g15.exe")
                        Popen("ghosts/g16.exe")
                    if n1 == 17:
                        Popen("ghosts/g1.exe")
                        Popen("ghosts/g2.exe")
                        Popen("ghosts/g3.exe")
                        Popen("ghosts/g4.exe")
                        Popen("ghosts/g5.exe")
                        Popen("ghosts/g6.exe")
                        Popen("ghosts/g7.exe")
                        Popen("ghosts/g8.exe")
                        Popen("ghosts/g9.exe")
                        Popen("ghosts/g10.exe")
                        Popen("ghosts/g11.exe")
                        Popen("ghosts/g12.exe")
                        Popen("ghosts/g13.exe")
                        Popen("ghosts/g14.exe")
                        Popen("ghosts/g15.exe")
                        Popen("ghosts/g16.exe")
                        Popen("ghosts/g17.exe")
                    if n1 == 18:
                        Popen("ghosts/g1.exe")
                        Popen("ghosts/g2.exe")
                        Popen("ghosts/g3.exe")
                        Popen("ghosts/g4.exe")
                        Popen("ghosts/g5.exe")
                        Popen("ghosts/g6.exe")
                        Popen("ghosts/g7.exe")
                        Popen("ghosts/g8.exe")
                        Popen("ghosts/g9.exe")
                        Popen("ghosts/g10.exe")
                        Popen("ghosts/g11.exe")
                        Popen("ghosts/g12.exe")
                        Popen("ghosts/g13.exe")
                        Popen("ghosts/g14.exe")
                        Popen("ghosts/g15.exe")
                        Popen("ghosts/g16.exe")
                        Popen("ghosts/g17.exe")
                        Popen("ghosts/g18.exe")
                    if n1 == 19:
                        Popen("ghosts/g1.exe")
                        Popen("ghosts/g2.exe")
                        Popen("ghosts/g3.exe")
                        Popen("ghosts/g4.exe")
                        Popen("ghosts/g5.exe")
                        Popen("ghosts/g6.exe")
                        Popen("ghosts/g7.exe")
                        Popen("ghosts/g8.exe")
                        Popen("ghosts/g9.exe")
                        Popen("ghosts/g10.exe")
                        Popen("ghosts/g11.exe")
                        Popen("ghosts/g12.exe")
                        Popen("ghosts/g13.exe")
                        Popen("ghosts/g14.exe")
                        Popen("ghosts/g15.exe")
                        Popen("ghosts/g16.exe")
                        Popen("ghosts/g17.exe")
                        Popen("ghosts/g18.exe")
                        Popen("ghosts/g19.exe")
                    if n1 == 20:
                        Popen("ghosts/g1.exe")
                        Popen("ghosts/g2.exe")
                        Popen("ghosts/g3.exe")
                        Popen("ghosts/g4.exe")
                        Popen("ghosts/g5.exe")
                        Popen("ghosts/g6.exe")
                        Popen("ghosts/g7.exe")
                        Popen("ghosts/g8.exe")
                        Popen("ghosts/g9.exe")
                        Popen("ghosts/g10.exe")
                        Popen("ghosts/g11.exe")
                        Popen("ghosts/g12.exe")
                        Popen("ghosts/g13.exe")
                        Popen("ghosts/g14.exe")
                        Popen("ghosts/g15.exe")
                        Popen("ghosts/g16.exe")
                        Popen("ghosts/g17.exe")
                        Popen("ghosts/g18.exe")
                        Popen("ghosts/g19.exe")
                        Popen("ghosts/g20.exe")
                    win.after(10000, loop_gmails)
                else:
                    pass

        else:
            messagebox.showerror("", "The target Gmail account doesn't exist")


def show_spam_f():  # toplevel that show spam from database
    global show_win
    show_win = Toplevel()
    show_win.title("Spam Number")
    show_win.geometry("150x100")
    show_win.resizable(False, False)
    show_win.iconbitmap("pictures/icon.ico")
    show_win.configure(bg="gray")
    show_b.configure(state=DISABLED)
    show_win.protocol("WM_DELETE_WINDOW", show_win_f)

    def show_b_f():
        c.execute("SELECT *,oid FROM spam_number")
        w = c.fetchall()
        sp_nu = w[0][0]
        Label(show_win, text=sp_nu, borderwidth=4, bg="gray").grid(
            row=0, column=0, padx=50, pady=10
        )

    ##################### DESIGN ######################
    c.execute("SELECT *,oid FROM spam_number")
    w = c.fetchall()
    sp_nu = w[0][0]
    l_s_s = Label(show_win, text=sp_nu, borderwidth=4, bg="gray").grid(
        row=0, column=0, padx=50, pady=10
    )
    b_r_s = Button(
        show_win, text="Refresh", bg="gray", borderwidth=4, command=show_b_f
    ).grid(row=1, column=0, padx=50, pady=5)


a = 1


def add_f():  # Toplevel that you need to press before all to put ur emails
    global add_win, a
    c.execute("DELETE FROM g_p_t")
    ############################ FUNCTIONS (3) ###########################
    texta = "Add Gmail Number " + str(a)

    def b_a_a_f():
        global a

        gmail = e_email.get()
        password = e_pass.get()
        # deleting the boxs
        e_email.delete(0, END)
        e_pass.delete(0, END)
        ping1 = call("ping -n 1 google.com", shell=True)
        if ping1 == 1:
            messagebox.showerror("", "There is no Internet connection")  # NO network.
        else:
            server = SMTP_SSL("smtp.gmail.com", 465)
            try:
                server.login(gmail, password)
            except:
                messagebox.showerror(
                    "",
                    "Couldn't connect to this Gmail account please make sure you enable less secured apps to access Gmail from settings in your account",
                )
                e_email.insert(0, gmail)
                e_pass.insert(0, password)

            else:
                server.quit()
                # inserting them to database gmail and password
                c.execute(
                    "INSERT INTO g_p_t VALUES(:gmail ,:password)",
                    {"gmail": gmail, "password": password},
                )
                a += 1
                if a == int(drop_gm.get()) + 1:
                    add_win_f()
                else:
                    texta = "Add Gmail Number " + str(a)
                    l_a_a = Label(add_win, text=texta, bg="gray").grid(row=1, column=1)

    def b_a_b_f():
        global a
        if a > 1:
            # deleting first
            e_email.delete(0, END)
            e_pass.delete(0, END)
            # selecting and taking what was there from database
            c.execute("SELECT *,oid FROM g_p_t ")
            y = c.fetchall()
            r_gmail = y[a - 2][0]
            r_pass = y[a - 2][1]
            a -= 1
            word = "DELETE FROM g_p_t WHERE oid =" + str(a)
            c.execute(word)
            print(r_gmail)
            print(r_pass)
            e_email.insert(0, r_gmail)
            e_pass.insert(0, r_pass)
            texta = "Add Gmail Number " + str(a)
            l_a_a = Label(add_win, text=texta).grid(row=1, column=1)

    ################################ ADD GMAIL WINDOW #####################################
    # ------------------------------ DESIGN ---------------------------------------
    # window
    add_win = Toplevel()
    add_win.protocol("WM_DELETE_WINDOW", add_win_f)
    add_win.title("Add Gmails")
    add_win.geometry("300x160")
    add_win.resizable(False, False)
    add_win.iconbitmap("pictures/icon.ico")
    add_win.configure(bg="gray")
    add_b.configure(state=DISABLED)
    ##### CREATING ITEMS
    # 2 buttons
    b_a_a = Button(add_win, text="Add", bg="gray", borderwidth=4, command=b_a_a_f)
    b_a_b = Button(add_win, text="Back", bg="gray", borderwidth=4, command=b_a_b_f)
    # 2 entries
    e_email = Entry(add_win, width=30, bg="silver")
    e_pass = Entry(add_win, width=30, bg="silver")
    # 3 label
    l_a_a = Label(add_win, text=texta, bg="gray")
    # --
    l_e = Label(add_win, text="Gmail Adress", bg="gray")
    l_p = Label(add_win, text="Password", bg="gray")

    # 4 white spaces
    fws = Label(add_win, text="", fg="gray", bg="gray")
    bsws = Label(add_win, text="", fg="gray", bg="gray")
    sws = Label(add_win, text="", fg="gray", bg="gray")
    tws = Label(add_win, text="", fg="gray", bg="gray")
    ##### POISITIONS
    fws.grid(row=0, column=0)
    bsws.grid(row=1, column=0)
    l_a_a.grid(row=1, column=1)
    l_e.grid(row=2, column=0)
    e_email.grid(row=2, column=1, pady=5)
    l_p.grid(row=3, column=0)
    e_pass.grid(row=3, column=1, pady=5)
    sws.grid(row=4, column=0)
    b_a_a.grid(row=5, column=2)
    tws.grid(row=5, column=1)
    b_a_b.grid(row=5, column=0)


# ---------------------------------------DISABLES-------------------------------------------
def add_win_f():
    add_b.configure(state=NORMAL)
    start_b.configure(state=NORMAL)
    add_win.destroy()


def show_win_f():
    show_b.configure(state=NORMAL)
    show_win.destroy()


def check_f():
    if var_c1.get() == 1:  # disabling and enabling time
        e_s.configure(state=NORMAL)
    if var_c1.get() == 0:
        e_s.delete(0, END)
        e_s.configure(state=DISABLED)


def a_o_g():
    if r.get() == 1:  # disabling and enabling ghosts and gmails
        o_gmails.configure(state=DISABLED)
        o_ghosts.configure(state=NORMAL)
        add_b.configure(state=DISABLED)
        o_gmails.configure(state=DISABLED)
        o_ghosts.configure(state=NORMAL)
        start_b.configure(state=NORMAL)
        try:
            add_win.destroy()
        except:
            pass

    if r.get() == 2:
        o_gmails.configure(state=NORMAL)
        o_ghosts.configure(state=DISABLED)
        add_b.configure(state=NORMAL)
        o_ghosts.configure(state=DISABLED)
        o_gmails.configure(state=NORMAL)
        start_b.configure(state=DISABLED)


# Making the window setup GUI
win = Tk()
win.geometry("761x450")
win.title("XGhost Spammer")
win.iconbitmap("pictures/icon.ico")
win.configure(bg="black")
win.resizable(False, False)
######################################---->>> DESIGN <----########################################
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
# ------------------------------------------------BANNER-------------------------------------------------
# Makingg the banner buton,images,and texts
b_info = Button(
    win, text="Info", command=info_b, padx=30, pady=10, fg="black", bg="silver"
)
b_exit = Button(
    win, text="Exit", command=exit_b, padx=31, pady=10, fg="black", bg="silver"
)

my_img = ImageTk.PhotoImage(Image.open("pictures/ban.png"))
banner_l = Label(image=my_img)
my_imge = ImageTk.PhotoImage(Image.open("pictures/imgg.png"))
ghost_l = Label(image=my_imge)


# Position of banner
banner_l.grid(row=0, column=1, rowspan=2)
ghost_l.grid(row=0, column=2, rowspan=2)
b_exit.grid(row=1, column=0)
b_info.grid(row=0, column=0)

# ------------------------------------------------INFORMATION----------------------------------------------(LABEL)
# making a frame label for the 2 inputs setup frame
f_i = LabelFrame(win, text="Information", padx=100, pady=5, background="gray")
f_i.grid(row=2, column=0, columnspan=3, pady=0)
# Making the 2 inputs
e_target = Entry(f_i, width=30, bg="gainsboro")
e_msg = Entry(f_i, width=30, bg="gainsboro")
# making the 2 labels text
l_target = Label(f_i, text="Target Gmail  ", background="gray")
l_msg = Label(f_i, text="Message to spam", padx=10, background="gray")
# Positioning all
l_target.grid(row=0, column=0)
l_msg.grid(row=0, column=2)
e_target.grid(row=0, column=1)
e_msg.grid(row=0, column=3)
# ------------------------------------------------TIME-----------------------------------------------------
# first making the frame label of time
f_t = LabelFrame(win, text="Time Delay", padx=265, pady=2, background="gray")
f_t.grid(row=3, column=0, columnspan=3, pady=0)
# making the time checkbox the label of it and the input field and ho wmany seconds asking
var_c1 = IntVar()
l_c_b = Label(f_t, text="Use Time Delay", bg="gray")  # label of checkbutton
c1 = Checkbutton(
    f_t, variable=var_c1, command=check_f, background="gray"
)  # checkbutton
l_s = Label(f_t, text="Seconds", background="gray")
e_s = Entry(f_t, width=10, bg="gainsboro", state=DISABLED)  # the entry of seconds
# position of all
l_c_b.grid(row=0, column=0)
c1.grid(row=0, column=1)
l_s.grid(row=0, column=2)
e_s.grid(row=0, column=3)
# --------------------------------------------------ATTACKER OPTIONS--------------------------------------------------------
# make a label for attacker options
f_a = LabelFrame(win, text="Attacker Options", padx=109, bg="gray")
f_a.grid(row=4, column=0, columnspan=4, pady=0)
# make 2 check buttons and 2 drop down munus


drop_gh = IntVar()
drop_gh.set(1)

drop_gm = IntVar()
drop_gm.set(1)

r = IntVar()
r.set(1)

r_ghosts = Radiobutton(
    f_a,
    text="Use Program Ghosts (Gmails)",
    command=a_o_g,
    variable=r,
    value=1,
    bg="gray",
)  # Radio button
r_gmails = Radiobutton(
    f_a, text="Use My Own Gmails", command=a_o_g, variable=r, value=2, bg="gray"
)  # Radio Button
o_ghosts = OptionMenu(f_a, drop_gh, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
o_gmails = OptionMenu(
    f_a, drop_gm, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
)


o_ghosts.configure(bg="gray")  # changing the background color
o_gmails.configure(bg="gray")
l_n_g = Label(f_a, text="Number Of Gmails                       ", bg="gray")
l_n_gh = Label(f_a, text="Number Of Gmails", bg="gray")
# Positioning
r_ghosts.grid(row=0, column=0)
r_gmails.grid(row=0, column=1)
o_ghosts.grid(row=1, column=1, pady=10)
o_gmails.grid(row=1, column=3, pady=10)
l_n_g.grid(row=1, column=2)
l_n_gh.grid(row=1, column=0)
# -----------------------------------------CONTROLING PANNEL------------------
# making a frame label ffor the output
f_p = LabelFrame(win, padx=0, bg="gray")
f_p.grid(row=5, column=0, columnspan=4, pady=3)

# Making a start button ,Stop Button,show emails and spam Button and add emails Button

start_b = Button(f_p, text="Start", command=start_f, padx=15, pady=5, bg="silver")
stop_b = Button(
    f_p, text="Stop", command=stop_f, padx=15, pady=5, bg="silver", state=DISABLED
)
show_b = Button(
    f_p,
    text="Show Spam Amount",
    command=show_spam_f,
    padx=15,
    pady=5,
    bg="silver",
    state=DISABLED,
)
add_b = Button(
    f_p, text="Add Gmails", command=add_f, padx=15, pady=5, bg="silver", state=DISABLED
)
l_space = Label(f_p, text="", padx=50, bg="gray")
try:
    a_o_g()  # bcz it doesnt get defined and we do so much work wich mean more time
except:
    pass
# Positioning
start_b.grid(row=0, column=0)
stop_b.grid(row=0, column=1)
show_b.grid(row=0, column=2)
l_space.grid(row=0, column=3)
add_b.grid(row=0, column=4)
# -----------------------------------------OUTPUT PANNEL-------------------------
# no frame label bcz its just our out put
# Making output for time of starting
l_v_o = Label(
    win,
    text=">>>   XGhost Spammer 2020 Version 1.1.8  by XGhost",
    fg="white",
    bg="black",
    font=3,
)
l_v_o.grid(row=6, column=0, columnspan=4, sticky="w")

l_s_o = Label(win, text=">>>", fg="white", bg="black", font=(3))
l_s_o.grid(row=7, column=0, columnspan=4, sticky="w")
# output of ... so he know its spamming

l_w_o = Label(win, text=">>>", fg="white", bg="black", font=(3))
l_w_o.grid(row=8, column=0, columnspan=4, sticky="w")

# out put of time of ending

l_e_o = Label(win, text=">>>", fg="white", bg="black", font=(3))
l_e_o.grid(row=9, column=0, columnspan=4, sticky="w")

# out put of spam time

l_sp_o = Label(win, text=">>>", fg="white", bg="black", font=(3))
l_sp_o.grid(row=10, column=0, columnspan=4, sticky="w")

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
######################################---->>> BACKEND PROGRAM <----##################################

win.protocol("WM_DELETE_WINDOW", closing)  # command so we make some stuff when closing


# ------------------------------------------CONNECTING----------------------------------------------
if NO_DATABASE_ENABLE == False:
    print("entered")
    con = connect("database.db")
    c = con.cursor()
    # ---------------------------------- GIVING ALERT TO THE USER ONLY ONCE --------------

    c.execute(
        "SELECT *,oid FROM alert"
    )  # checking if the user use this first time or have used before wich mean saw the message
    alert_c = c.fetchall()
    alert = alert_c[0][0]
    if alert == 0:  # first time the user downolad it
        messagebox.showinfo(
            "",
            "Spamming is ILLEGAL.\nPlease use this on your own gmail accounts.\nThe programm Devloper is not responsible for any damage caused by the users . Click Info for more ",
        )
        c.execute("DELETE FROM alert")
        con.commit()
        c.execute("INSERT INTO alert VALUES (:var)", {"var": 1})
        con.commit()


# ----------------------------------------CREATING DATABASE--------------------------------------------

# c.execute("""CREATE TABLE t_m_t (
# 	target text,
# 	msg text
# )""")#table of the target and message (informations)
# c.execute("""CREATE TABLE t_t (
# 	on_of integer,
# 	seconds integer
# )""")#table of time delay
# c.execute("""CREATE TABLE g_p_t (
# 	gmail text,
# 	pass text
# "")""")#table of user gmails
# c.execute("""CREATE TABLE fail (
# 	fail_number integer
# )""")#table of fails
# c.execute("CREATE TABLE spam_number (spam_n integer)") #table of how many did we spam
# c.execute("CREATE TABLE alert (var integer) ") #table of one time alert
# con.commit()
# c.execute("INSERT INTO alert VALUES (:var)",{"var" : 0})   #give it to user reset it
# con.commit() #same

# -------------------------------------INSERTING INFORMATIONS TO DATABASE---------------------------------


#closing at the end to leave and make sure nothing is harmed
try:  # added for UI testing with no database
    con.commit()
except:
    pass

# main loop at the end

mainloop()
con.close()
