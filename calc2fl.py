# electro calculator, with Flet modul
# version 0.1  2024.02.17.- 2024.02.22.   KL
import flet as ft
from math import pi
from math import sqrt
from math import atan			 

def main(page: ft.Page):

        page.title = "calc2"
		
        def xl_f_click(e):			# xl-tab 'f' változását lekezelő függvény	
                ok = True
                try:
                        xl = float(tf_xl_XL.value)   # 'XL' beolvasása szövegmezőből
                        if xl <= 0:
                                ok = False
                                tf_xl_XL.value = tf_xl_XL.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_xl_XL.value = tf_xl_XL.value + ' ?'   # nem jó érték !
                try:
                        L = float(tf_xl_L.value)   # 'L' beolvasása szövegmezőből
                        if L <= 0:
                                ok = False
                                tf_xl_L.value = tf_xl_L.value + ' ?'   # nem jó érték !               
                except:
                        ok = False
                        tf_xl_L.value = tf_xl_L.value + ' ?'   # nem jó érték !
                if ok:
                        f = 1000*xl/(2*pi*L)        #  f   Hz-ben !!
                        tf_xl_f.value = str(f)   # 'f' kiírása szövegmezőbe
                else:
                        tf_xl_f.value = "hiba!!"   

                page.update()			#  grafikus felület frissítése

        ###########################################################################################

        def xl_L_click(e):			# xl-tab 'L' változását lekezelő függvény	
                ok = True
                try:
                        xl = float(tf_xl_XL.value)   # 'XL' beolvasása szövegmezőből
                        if xl <= 0:
                                ok = False
                                tf_xl_XL.value = tf_xl_XL.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_xl_XL.value = tf_xl_XL.value + ' ?'   # nem jó érték !
                try:
                        f = float(tf_xl_f.value)   # 'f' beolvasása szövegmezőből
                        if f <= 0:
                                ok = False
                                tf_xl_f.value = tf_xl_f.value + ' ?'   # nem jó érték !               
                except:
                        ok = False
                        tf_xl_f.value = tf_xl_f.value + ' ?'   # nem jó érték !
                if ok:
                        L = 1000*xl/(2*pi*f)        #  L   mH-ben !!
                        tf_xl_L.value = str(L)   # 'L' kiírása szövegmezőbe
                else:
                        tf_xl_L.value = "hiba!!"   

                page.update()			#  grafikus felület frissítése

       ###########################################################################################

        def xl_XL_click(e):			# xl-tab XL változását lekezelő függvény	
                ok = True
                try:
                        L = float(tf_xl_L.value)   # 'L' beolvasása szövegmezőből
                        if L <= 0:
                                ok = False
                                tf_xl_L.value = tf_xl_L.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_xl_L.value = tf_xl_L.value + ' ?'   # nem jó érték !
                try:
                        f = float(tf_xl_f.value)   # 'f' beolvasása szövegmezőből
                        if f <= 0:
                                ok = False
                                tf_xl_f.value = tf_xl_f.value + ' ?'   # nem jó érték !               
                except:
                        ok = False
                        tf_xl_f.value = tf_xl_f.value + ' ?'   # nem jó érték !
                if ok:
                        xl = 2*pi*f*L/1000         #  XL   Ohm-ban !!
                        tf_xl_XL.value = str(xl)   # 'XL' kiírása szövegmezőbe
                else:
                        tf_xl_XL.value = "hiba!!"   

                page.update()			#  grafikus felület frissítése

       ###########################################################################################

        def xc_f_click(e):			#  xc-tab 'f' változását lekezelő függvény	
                ok = True
                try:
                        xc = float(tf_xc_XC.value)   # 'XC' beolvasása szövegmezőből
                        if xc <= 0:
                                ok = False
                                tf_xc_XC.value = tf_xc_XC.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_xc_XC.value = tf_xc_XC.value + ' ?'   # nem jó érték !
                try:
                        C = float(tf_xc_C.value)   # 'C' beolvasása szövegmezőből
                        if C <= 0:
                                ok = False
                                tf_xc_C.value = tf_xc_C.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_xc_C.value = tf_xc_C.value + ' ?'   # nem jó érték !
                if ok:
                        f = 1000000000/(2*pi*C*xc)        #  f   Hz-ben !!
                        tf_xc_f.value = str(f)   # 'f' kiírása szövegmezőbe
                else:
                        tf_xc_f.value = "hiba!!"        

                page.update()			#  grafikus felület frissítése

       ###########################################################################################

        def xc_C_click(e):			#  xc-tab 'C' változását lekezelő függvény	
                ok = True
                try:
                        xc = float(tf_xc_XC.value)   # 'XC' beolvasása szövegmezőből
                        if xc <= 0:
                                ok = False
                                tf_xc_XC.value = tf_xc_XC.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_xc_XC.value = tf_xc_XC.value + ' ?'   # nem jó érték !
                try:
                        f = float(tf_xc_f.value)   # 'f' beolvasása szövegmezőből
                        if f <= 0:
                                ok = False
                                tf_xc_f.value = tf_xc_f.value + ' ?'   # nem jó érték !               
                except:
                        ok = False
                        tf_xc_f.value = tf_xc_f.value + ' ?'   # nem jó érték !
                if ok:
                        C = 1000000000/(2*pi*f*xc)        #  C   nF-ban !!
                        tf_xc_C.value = str(C)   # 'C' kiírása szövegmezőbe
                else:
                        tf_xc_C.value = "hiba!!"   

                page.update()			#  grafikus felület frissítése

       ###########################################################################################

        def xc_XC_click(e):			#  xc-tab 'XC' változást lekezelő függvény	
                ok = True
                try:
                        C = float(tf_xc_C.value)   # 'C' beolvasása szövegmezőből
                        if C <= 0:
                                ok = False
                                tf_xc_C.value = tf_xc_C.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_xc_C.value = tf_xc_C.value + ' ?'   # nem jó érték !
                try:
                        f = float(tf_xc_f.value)   # 'f' beolvasása szövegmezőből
                        if f <= 0:
                                ok = False
                                tf_xc_f.value = tf_xc_f.value + ' ?'   # nem jó érték !               
                except:
                        ok = False
                        tf_xc_f.value = tf_xc_f.value + ' ?'   # nem jó érték !
                if ok:
                        xc = 1000000000/(2*pi*f*C)        #  XC   Ohm-ban !!
                        tf_xc_XC.value = str(xc)   # 'XL' kiírása szövegmezőbe
                else:
                        tf_xc_XC.value = "hiba!!"   

                page.update()			#  grafikus felület frissítése

       ###########################################################################################

        def fo_f_click(e):			#  fo-tab 'f' változását lekezelő függvény
                ok = True
                try:
                        L = float(tf_fo_L.value)   # 'L' beolvasása szövegmezőből
                        if L <= 0:
                                ok = False
                                tf_fo_L.value = tf_fo_L.value + ' ?'   # nem jó érték !               
                except:
                        ok = False
                        tf_fo_L.value = tf_fo_L.value + ' ?'   # nem jó érték !
                try:
                        C = float(tf_fo_C.value)   # 'C' beolvasása szövegmezőből
                        if C <= 0:
                                ok = False
                                tf_fo_C.value = tf_fo_C.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_fo_C.value = tf_fo_C.value + ' ?'   # nem jó érték !
                if ok:
                        f = 1000000/(2*pi*sqrt(C*L))        #  f   Hz-ben !!
                        tf_fo_f.value = str(f)   # 'f' kiírása szövegmezőbe
                else:
                        tf_fo_f.value = "hiba!!"        

                page.update()			#  grafikus felület frissítése

       ###########################################################################################

        def fo_L_click(e):			#  fo-tab 'L' változását lekezelő függvény
                ok = True
                try:
                        f = float(tf_fo_f.value)   # 'f' beolvasása szövegmezőből
                        if f <= 0:
                                ok = False
                                tf_fo_f.value = tf_fo_f.value + ' ?'   # nem jó érték !               
                except:
                        ok = False
                        tf_fo_f.value = tf_fo_f.value + ' ?'   # nem jó érték !
                try:
                        C = float(tf_fo_C.value)   # 'C' beolvasása szövegmezőből
                        if C <= 0:
                                ok = False
                                tf_fo_C.value = tf_fo_C.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_fo_C.value = tf_fo_C.value + ' ?'   # nem jó érték !
                if ok:
                        L = 1000000000000/(4*pi*pi*f*f*C)       #  L  mH-ben !!
                        tf_fo_L.value = str(L)   # 'f' kiírása szövegmezőbe
                else:
                        tf_fo_L.value = "hiba!!"        

                page.update()			#  grafikus felület frissítése

       ###########################################################################################

        def fo_C_click(e):			#  fo-tab 'C' változását lekezelő függvény
                ok = True
                try:
                        f = float(tf_fo_f.value)   # 'f' beolvasása szövegmezőből
                        if f <= 0:
                                ok = False
                                tf_fo_f.value = tf_fo_f.value + ' ?'   # nem jó érték !               
                except:
                        ok = False
                        tf_fo_f.value = tf_fo_f.value + ' ?'   # nem jó érték !
                try:
                        L = float(tf_fo_L.value)   # 'L' beolvasása szövegmezőből
                        if L <= 0:
                                ok = False
                                tf_fo_L.value = tf_fo_L.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_fo_L.value = tf_fo_L.value + ' ?'   # nem jó érték !
                if ok:
                        C = 1000000000000/(4*pi*pi*f*f*L)       #  C  nF-ban !!
                        tf_fo_C.value = str(C)   # 'f' kiírása szövegmezőbe
                else:
                        tf_fo_C.value = "hiba!!"        

                page.update()			#  grafikus felület frissítése


       ###########################################################################################

        def rlc_Ze_click(e):			#  rlc-tab 'Ze' változását lekezelő függvény
                ok = True  
                try:
                        f = float(tf_rlc_f.value)   # 'f' beolvasása szövegmezőből
                        if f <= 0:
                                ok = False
                                tf_rlc_f.value = tf_rlc_f.value + ' ?'   # nem jó érték !               
                except:
                        ok = False
                        tf_rlc_f.value = tf_rlc_f.value + ' ?'   # nem jó érték !
                try:
                        L = float(tf_rlc_L.value)   # 'L' beolvasása szövegmezőből
                        if L < 0:
                                ok = False
                                tf_rlc_L.value = tf_rlc_L.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_rlc_L.value = tf_rlc_L.value + ' ?'   # nem jó érték 
                try:
                        C = float(tf_rlc_C.value)   # 'C' beolvasása szövegmezőből
                        if C < 0:
                                ok = False
                                tf_rlc_C.value = tf_rlc_C.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_rlc_C.value = tf_rlc_C.value + ' ?'   # nem jó érték !
                try:
                        R = float(tf_rlc_R.value)   # 'R' beolvasása szövegmezőből
                        if R < 0:
                                ok = False
                                tf_rlc_R.value = tf_rlc_R.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_rlc_R.value = tf_rlc_R.value + ' ?'   # nem jó érték !                       
                if ok:
                        if L == 0:
                                xl = 0
                        else:
                                xl = 2*pi*f*L/1000         #  XL   Ohm-ban !!
                        if C == 0:
                                xc = 0
                        else:
                                xc = 1000000000/(2*pi*f*C)        #  XC   Ohm-ban !!
                        Ze = sqrt(R**2+(xl-xc)**2)
                        if R == 0:
                                if xl>xc:
                                        fi = 90
                                elif xc>xl:
                                        fi = -90
                                else:
                                        fi = ""
                        else:
                                fi = 180*atan((xl-xc)/R)/pi

                        tf_rlc_Ze.value = str(Ze)   # 'Ze' kiírása szövegmezőbe
                        tf_rlc_fi.value = str(fi)   # 'fi' kiírása szövegmezőbe
                else:
                        tf_rlc_Ze.value = "hiba!!"     
                        tf_rlc_fi.value = "hiba!!"     

                page.update()			#  grafikus felület frissítése

        
       ###########################################################################################

        def r_R_click(e):			#  r-tab 'R' változását lekezelő függvény
                ok = True
                try:
                        l = float(tf_r_l.value)   # 'l-hossz' beolvasása szövegmezőből
                        if l <= 0:
                                ok = False
                                tf_r_l.value = tf_r_l.value + ' ?'   # nem jó érték !               
                except:
                        ok = False
                        tf_r_l.value = tf_r_l.value + ' ?'   # nem jó érték !
                try:
                        d = float(tf_r_d.value)   # 'd-átmérő' beolvasása szövegmezőből
                        if d <= 0:
                                ok = False
                                tf_r_d.value = tf_r_d.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_r_d.value = tf_r_d.value + ' ?'   # nem jó érték !
                try:
                        ro = float(tf_r_ro.value)   # fajlagos ellenállás beolvasása szövegmezőből
                        if ro <= 0:
                                ok = False
                                tf_r_ro.value = tf_r_ro.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_r_ro.value = tf_r_ro.value + ' ?'   # nem jó érték !                       
                if ok:
                        A = d*d*pi/4            # keresztmetszet   mm2
                        R = ro*l/A       #  ohm-ban !!
                        tf_r_R.value = str(R)   # 'R' kiírása szövegmezőbe
                else:
                        tf_r_R.value = "hiba!!"        

                page.update()		


      ###########################################################################################

        def r_ro_sel_change(e):			#  r-tab 'ró' változását lekezelő függvény
                if tf_r_ro_sel.value == "Réz":
                    tf_r_ro.value = str(0.0175)
                elif tf_r_ro_sel.value == "Alumínium":
                    tf_r_ro.value = str(0.028)
                elif tf_r_ro_sel.value == "Arany":
                    tf_r_ro.value = str(0.023)
                elif tf_r_ro_sel.value == "Ezüst":
                    tf_r_ro.value = str(0.016)
                page.update()


      ###########################################################################################

        def rc_Tr_click(e):			#  rc-tab 'Tr' változását lekezelő függvény
                ok = True  
                try:
                        f = float(tf_rc_f.value)   # 'f' beolvasása szövegmezőből
                        if f < 0:
                                ok = False
                                tf_rc_f.value = tf_rc_f.value + ' ?'   # nem jó érték !               
                except:
                        ok = False
                        tf_rc_f.value = tf_rc_f.value + ' ?'   # nem jó érték !
                try:
                        C = float(tf_rc_C.value)   # 'C' beolvasása szövegmezőből
                        if C <= 0:
                                ok = False
                                tf_rc_C.value = tf_rc_C.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_rc_C.value = tf_rc_C.value + ' ?'   # nem jó érték !
                try:
                        R = float(tf_rc_R.value)   # 'R' beolvasása szövegmezőből
                        if R <= 0:
                                ok = False
                                tf_rc_R.value = tf_rc_R.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_rc_R.value = tf_rc_R.value + ' ?'   # nem jó érték !                       
                if ok:
                        if f==0:
                                Tr = 1
                                fi = 0
                        else:
                                xc = 1000000000/(2*pi*f*C)        #  XC   Ohm-ban !!
                                Ze = sqrt(R**2+xc**2)
                                Tr = xc/Ze
                                fi = -180*atan(R/xc)/pi

                        fh=1000000000/(2*pi*R*C)
                        tf_rc_Tr.value = str(Tr)   # 'Uki/Ube' kiírása szövegmezőbe
                        tf_rc_fi.value = str(fi)   # 'fi' kiírása szövegmezőbe
                        tf_rc_fh.value = str(fh)   # 'fh' kiírása szövegmezőbe
                else:
                        tf_rc_Tr.value = "hiba!!"     
                        tf_rc_fi.value = "hiba!!"     
                        tf_rc_fh.value = "hiba!!" 


                page.update()			#  grafikus felület frissítése

 ###########################################################################################

        def cr_Tr_click(e):			#  cr-tab 'Tr' változását lekezelő függvény
                ok = True  
                try:
                        f = float(tf_cr_f.value)   # 'f' beolvasása szövegmezőből
                        if f < 0:
                                ok = False
                                tf_cr_f.value = tf_cr_f.value + ' ?'   # nem jó érték !               
                except:
                        ok = False
                        tf_cr_f.value = tf_cr_f.value + ' ?'   # nem jó érték !
                try:
                        C = float(tf_cr_C.value)   # 'C' beolvasása szövegmezőből
                        if C <= 0:
                                ok = False
                                tf_cr_C.value = tf_cr_C.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_cr_C.value = tf_cr_C.value + ' ?'   # nem jó érték !
                try:
                        R = float(tf_cr_R.value)   # 'R' beolvasása szövegmezőből
                        if R <= 0:
                                ok = False
                                tf_cr_R.value = tf_cr_R.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_cr_R.value = tf_cr_R.value + ' ?'   # nem jó érték !                       
                if ok:
                        if f==0:
                                Tr = 1
                                fi = 0
                        else:
                                xc = 1000000000/(2*pi*f*C)        #  XC   Ohm-ban !!
                                Ze = sqrt(R**2+xc**2)
                                Tr = R/Ze
                                fi = 180*atan(xc/R)/pi

                        fh=1000000000/(2*pi*R*C)
                        tf_cr_Tr.value = str(Tr)   # 'Uki/Ube' kiírása szövegmezőbe
                        tf_cr_fi.value = str(fi)   # 'fi' kiírása szövegmezőbe
                        tf_cr_fh.value = str(fh)   # 'fh' kiírása szövegmezőbe
                else:
                        tf_cr_Tr.value = "hiba!!"     
                        tf_cr_fi.value = "hiba!!"     
                        tf_cr_fh.value = "hiba!!" 


                page.update()			#  grafikus felület frissítése


      ###########################################################################################

        txt_cim = ft.Text(
                value=" Elektrotechnika", 
                color=ft.colors.WHITE, 
                bgcolor=ft.colors.ORANGE_800, 
                size=20,
                theme_style=ft.TextThemeStyle.TITLE_LARGE, 
                width = 500
        )	  #  egy cimke

        txt_space = ft.Text(
                value=" ", 
                color=ft.colors.WHITE, 
                bgcolor=ft.colors.WHITE, 
                size=60,
                theme_style=ft.TextThemeStyle.TITLE_LARGE, 
                width = 800
        )

        buttstyle1 = ft.ButtonStyle(bgcolor=ft.colors.YELLOW)   # button style
        textstyle1 = ft.TextStyle(size=25,color="pink600",weight=ft.FontWeight.W_900)

       ###########################################################################################
                # tab1-XL  buttons, textfields
        tb_xl_f = ft.TextButton(
                content= ft.Text(value="Frekvencia, f (Hz)",size=20, width=180),
                style= buttstyle1,
                on_click=xl_f_click
        )
        tb_xl_L = ft.TextButton(
                content= ft.Text(value="Induktivitás, L (mH)",size=20, width=180),
                style= buttstyle1, 
                on_click=xl_L_click
        )
        tb_xl_XL = ft.TextButton(
                content= ft.Text(value="   XL    (ohm)",size=20, width=180),
                style= buttstyle1,
                on_click=xl_XL_click
        )
        tf_xl_f = ft.TextField(value=" ", width = 160)
        tf_xl_L = ft.TextField(value=" ", width = 160)
        tf_xl_XL = ft.TextField(value=" ", width = 160)

        data_xlf = ft.Row(controls=[tb_xl_f,tf_xl_f])
        data_xlL = ft.Row(controls=[tb_xl_L,tf_xl_L])
        data_xlXL = ft.Row(controls=[tb_xl_XL,tf_xl_XL])

       ###########################################################################################
              # tab2-XC  buttons, textfields
        tb_xc_f = ft.TextButton(
                content= ft.Text(value="Frekvencia, f (Hz)",size=20, width=180), 
                style= buttstyle1,
                on_click=xc_f_click
        )
        tb_xc_C = ft.TextButton(
                content= ft.Text(value="Kapacitás, C (nF)",size=20, width=180), 
                style= buttstyle1, 
                on_click=xc_C_click
        )
        tb_xc_XC = ft.TextButton(
                content= ft.Text(value="   XC   (ohm)",size=20, width=180), 
                style= buttstyle1, 
                on_click=xc_XC_click
        )
        tf_xc_f = ft.TextField(value=" ", width = 160)
        tf_xc_C = ft.TextField(value=" ", width = 160)
        tf_xc_XC = ft.TextField(value=" ", width = 160)

        data_xcf = ft.Row(controls=[tb_xc_f,tf_xc_f])
        data_xcC = ft.Row(controls=[tb_xc_C,tf_xc_C])
        data_xcXC = ft.Row(controls=[tb_xc_XC,tf_xc_XC])

       ###########################################################################################
                # tab3-fo  buttons, textfields
        tb_fo_f = ft.TextButton(
                content= ft.Text(value="Rezonancia frekvencia, fo (Hz)",size=20, width=180), 
                style= buttstyle1,  
                on_click=fo_f_click
        )
        tb_fo_L = ft.TextButton(
                content= ft.Text(value="Induktivitás, L (mH)",size=20, width=180),
                style= buttstyle1,  
                on_click=fo_L_click
        )
        tb_fo_C = ft.TextButton(
                content= ft.Text(value="Kapacitás, C (nF)",size=20, width=180), 
                style= buttstyle1, 
                on_click=fo_C_click
        )
        tf_fo_f = ft.TextField(value=" ", width = 160)
        tf_fo_L = ft.TextField(value=" ", width = 160)
        tf_fo_C = ft.TextField(value=" ", width = 160)

        data_fof = ft.Row(controls=[tb_fo_f,tf_fo_f])
        data_foL = ft.Row(controls=[tb_fo_L,tf_fo_L])
        data_foC = ft.Row(controls=[tb_fo_C,tf_fo_C])

       ###########################################################################################
                # tab4-RLC  buttons, textfields
        tb_rlc_f = ft.TextButton(
                content= ft.Text(value="Frekvencia, f (Hz)",size=20, width=180), 
                style= buttstyle1,  
               # on_click=rlc_f_click
        )
        tb_rlc_L = ft.TextButton(
                content= ft.Text(value="Induktivitás, L (mH)",size=20, width=180),
                style= buttstyle1,  
              #  on_click=rlc_L_click
        )
        tb_rlc_C = ft.TextButton(
                content= ft.Text(value="Kapacitás, C (nF)",size=20, width=180), 
                style= buttstyle1, 
             #  on_click=rlc_C_click
        )
        tb_rlc_R = ft.TextButton(
                content= ft.Text(value="Ellenállás, R (ohm)",size=20, width=180), 
                style= buttstyle1, 
             #  on_click=rlc_R_click
        )
        tb_rlc_Ze = ft.TextButton(
                content= ft.Text(value="Impedancia, Ze (ohm)",size=20, width=180), 
                style= buttstyle1, 
                on_click=rlc_Ze_click
        )
        tb_rlc_fi = ft.TextButton(
                content= ft.Text(value="Fázisszög, fi (fok)",size=20, width=180), 
                style= buttstyle1, 
                on_click=rlc_Ze_click
        )

        tf_rlc_f = ft.TextField(value=" ", width = 160)
        tf_rlc_L = ft.TextField(value=" ", width = 160)
        tf_rlc_C = ft.TextField(value=" ", width = 160)
        tf_rlc_R = ft.TextField(value=" ", width = 160)
        tf_rlc_Ze = ft.TextField(value=" ", width = 160)
        tf_rlc_fi = ft.TextField(value=" ", width = 160)

        data_rlcf = ft.Row(controls=[tb_rlc_f,tf_rlc_f])
        data_rlcL = ft.Row(controls=[tb_rlc_L,tf_rlc_L])
        data_rlcC = ft.Row(controls=[tb_rlc_C,tf_rlc_C])
        data_rlcR = ft.Row(controls=[tb_rlc_R,tf_rlc_R])
        data_rlcZe = ft.Row(controls=[tb_rlc_Ze,tf_rlc_Ze])
        data_rlcfi = ft.Row(controls=[tb_rlc_fi,tf_rlc_fi])

      ###########################################################################################
              # tab5-R  buttons, textfields
        tb_r_l = ft.TextButton(
                content= ft.Text(value="Hossz, l (m)",size=20, width=180), 
                style= buttstyle1,
        )
        tb_r_d = ft.TextButton(
                content= ft.Text(value="Átmérő, d (mm)",size=20, width=180), 
                style= buttstyle1, 
        )
        tb_r_R = ft.TextButton(
                content= ft.Text(value="Ellenállás  R (ohm)",size=20, width=180), 
                style= buttstyle1, 
                on_click=r_R_click
        )
        tb_r_ro = ft.TextButton(
                content= ft.Text(value="Anyag,  ró        (ohm*mm2/m)",size=20, width=180), 
                style= buttstyle1, 
        )
        tf_r_l = ft.TextField(value=" ", width = 160)
        tf_r_d = ft.TextField(value=" ", width = 160)
        tf_r_R = ft.TextField(value=" ", width = 160)
        tf_r_ro_sel = ft.Dropdown(
        	width=120,
        	options=[
            		ft.dropdown.Option("Réz"),
            		ft.dropdown.Option("Alumínium"),
            		ft.dropdown.Option("Arany"), 
                        ft.dropdown.Option("Ezüst")
                        ], 
                on_change = r_ro_sel_change
	)
        tf_r_ro = ft.TextField(value=" ", width = 120)

        data_rl = ft.Row(controls=[tb_r_l,tf_r_l])
        data_rd = ft.Row(controls=[tb_r_d,tf_r_d])
        data_rR = ft.Row(controls=[tb_r_R,tf_r_R])
        data_rro = ft.Row(controls=[tb_r_ro,tf_r_ro_sel, tf_r_ro])

  ###########################################################################################
              # tab6-RC  buttons, textfields
        tb_rc_f = ft.TextButton(
                content= ft.Text(value="Frekvencia, f (Hz)",size=20, width=180), 
                style= buttstyle1,  
               # on_click=rlc_f_click
        )
        tb_rc_C = ft.TextButton(
                content= ft.Text(value="Kapacitás, C (nF)",size=20, width=180), 
                style= buttstyle1, 
             #  on_click=rlc_C_click
        )
        tb_rc_R = ft.TextButton(
                content= ft.Text(value="Ellenállás, R (ohm)",size=20, width=180), 
                style= buttstyle1, 
             #  on_click=rlc_R_click
        )
        tb_rc_Tr = ft.TextButton(
                content= ft.Text(value="Feszültség átvitel, Uki / Ube",size=20, width=180),
                style= buttstyle1,  
                on_click=rc_Tr_click
        )
    
        tb_rc_fi = ft.TextButton(
                content= ft.Text(value="Fázistolás, ki-be (fok)",size=20, width=180), 
                style= buttstyle1, 
                on_click=rc_Tr_click
        )
        tb_rc_fh = ft.TextButton(
                content= ft.Text(value="Határfrekvencia, fh (Hz)",size=20, width=180), 
                style= buttstyle1, 
                on_click=rc_Tr_click
        )

        tf_rc_f = ft.TextField(value=" ", width = 160)  
        tf_rc_C = ft.TextField(value=" ", width = 160)
        tf_rc_R = ft.TextField(value=" ", width = 160)
        tf_rc_Tr = ft.TextField(value=" ", width = 160)
        tf_rc_fi = ft.TextField(value=" ", width = 160)
        tf_rc_fh = ft.TextField(value=" ", width = 160)

        data_rcf = ft.Row(controls=[tb_rc_f,tf_rc_f])     
        data_rcC = ft.Row(controls=[tb_rc_C,tf_rc_C])
        data_rcR = ft.Row(controls=[tb_rc_R,tf_rc_R])
        data_rcTr = ft.Row(controls=[tb_rc_Tr,tf_rc_Tr])
        data_rcfi = ft.Row(controls=[tb_rc_fi,tf_rc_fi])
        data_rcfh = ft.Row(controls=[tb_rc_fh,tf_rc_fh])

 ###########################################################################################
              # tab7-CR  buttons, textfields
        tb_cr_f = ft.TextButton(
                content= ft.Text(value="Frekvencia, f (Hz)",size=20, width=180), 
                style= buttstyle1,  
               # on_click=rlc_f_click
        )
        tb_cr_C = ft.TextButton(
                content= ft.Text(value="Kapacitás, C (nF)",size=20, width=180), 
                style= buttstyle1, 
             #  on_click=rlc_C_click
        )
        tb_cr_R = ft.TextButton(
                content= ft.Text(value="Ellenállás, R (ohm)",size=20, width=180), 
                style= buttstyle1, 
             #  on_click=rlc_R_click
        )
        tb_cr_Tr = ft.TextButton(
                content= ft.Text(value="Feszültség átvitel, Uki / Ube",size=20, width=180),
                style= buttstyle1,  
                on_click=cr_Tr_click
        )
    
        tb_cr_fi = ft.TextButton(
                content= ft.Text(value="Fázistolás, ki-be (fok)",size=20, width=180), 
                style= buttstyle1, 
                on_click=cr_Tr_click
        )
        tb_cr_fh = ft.TextButton(
                content= ft.Text(value="Határfrekvencia, fh (Hz)",size=20, width=180), 
                style= buttstyle1, 
                on_click=cr_Tr_click
        )

        tf_cr_f = ft.TextField(value=" ", width = 160)  
        tf_cr_C = ft.TextField(value=" ", width = 160)
        tf_cr_R = ft.TextField(value=" ", width = 160)
        tf_cr_Tr = ft.TextField(value=" ", width = 160)
        tf_cr_fi = ft.TextField(value=" ", width = 160)
        tf_cr_fh = ft.TextField(value=" ", width = 160)

        data_crf = ft.Row(controls=[tb_cr_f,tf_cr_f])     
        data_crC = ft.Row(controls=[tb_cr_C,tf_cr_C])
        data_crR = ft.Row(controls=[tb_cr_R,tf_cr_R])
        data_crTr = ft.Row(controls=[tb_cr_Tr,tf_cr_Tr])
        data_crfi = ft.Row(controls=[tb_cr_fi,tf_cr_fi])
        data_crfh = ft.Row(controls=[tb_cr_fh,tf_cr_fh])

       ###########################################################################################
                # tabs
        lapok = ft.Tabs(
                selected_index=0,  
                animation_duration=300,	# váltás a nézetek között ms
                tabs=[
                        ft.Tab(
                                text="XL",
                                content=ft.Column(
                                        controls=[
                                                ft.Text("Induktív reaktancia",style=textstyle1), 
                                                data_xlf, 
                                                data_xlL, 
                                                data_xlXL
                                        ]
                                ),
                        ),
                        ft.Tab(
                                text="XC",
                                content=ft.Column(
                                        controls=[
                                                ft.Text("Kapacitív reaktancia",style=textstyle1), 
                                                data_xcf, 
                                                data_xcC, 
                                                data_xcXC
                                        ]
                                ),
                        ),
                        ft.Tab(
                                text="fo",
                                content=ft.Column(
                                        controls=[
                                                ft.Text("Rezonancia fekvencia",style=textstyle1),
                                                data_foC, 
                                                data_foL, 
                                                data_fof
                                        ]
                                )
                        ),
                        ft.Tab(
                                text="RLC",
                                content=ft.Column(
                                        controls=[
                                                ft.Text("soros RLC",style=textstyle1),
                                                data_rlcf,      
                                                data_rlcL,
                                                data_rlcC,
                                                data_rlcR,
                                                data_rlcZe,
                                                data_rlcfi,
                                        ]
                                )
                        ),
                        ft.Tab(
                                text="R",
                                content=ft.Column(
                                        controls=[
                                                ft.Text("Vezeték ellenállása",style=textstyle1),
                                                data_rl, 
                                                data_rd,
                                                data_rro, 
                                                data_rR
                                        ]
                                )
                        ),
                        ft.Tab(
                                text="RC",
                                content=ft.Column(
                                        controls=[
                                                ft.Text("RC szűrő, alulát.",style=textstyle1),
                                                data_rcf,      
                                                data_rcC,
                                                data_rcR,
                                                data_rcTr,
                                                data_rcfi,
                                                data_rcfh,
                                        ]
                                )
                        ),
                        ft.Tab(
                                text="CR",
                                content=ft.Column(
                                        controls=[
                                                ft.Text("CR szűrő, felülát.",style=textstyle1),
                                                data_crf,      
                                                data_crC,
                                                data_crR,
                                                data_crTr,
                                                data_crfi,
                                                data_crfh,
                                        ]
                                )
                        ),
                ],
                expand=1,
        )

       ###########################################################################################

        page.window_width = 540
        page.window_height = 1000
        page.add(
                txt_cim,
                lapok,
                txt_space
        )


        

ft.app(target=main)		#  fő ablak/alkalmazás példány létrehozása
