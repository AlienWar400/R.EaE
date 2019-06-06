import tkinter as tk
from tkinter import *
from cefpython3 import cefpython as cef
import ctypes
import sys
import os
import platform
import logging as _logging
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror
from PIL import Image, ImageTk
import webbrowser
import time
import datetime
import Weather

root = tk.Tk()
root.resizable(False, False)
W = 480
H = 320

IMAGE_EXT = ".png" if tk.TkVersion > 8.5 else ".gif"

canvas = tk.Canvas(root, height=H, width=W, bg='#13111E', bd=0)
canvas.pack()

filename = NONE
logger = _logging.getLogger("tkinter_.py")


img = ImageTk.PhotoImage(Image.open("BGI.png"))
img1 = ImageTk.PhotoImage(Image.open("BGI.png"))
interficeImg = ImageTk.PhotoImage(Image.open("BGI.png"))
img2 = ImageTk.PhotoImage(Image.open("1.jpg"))
img3 = ImageTk.PhotoImage(Image.open("1.jpg"))
img4 = ImageTk.PhotoImage(Image.open("3.png"))

# def link(event):
#     webbrowser.open(url)
#
#
# def link1(event):
#     webbrowser.open(url1)
#
#
# def msg():
#     answer = messagebox.askyesno("Information", "Wanna exit?")
#     if answer == YES:
#         root.destroy()
#
#
# def About():
#     a = Toplevel()
#     a.geometry('480x320')
#     a.overrideredirect(False)
#     AbFrame = Frame(a, bg='pink')
#     AbFrame2 = Frame(a, bg='pink')
#     AbLabel = Label(AbFrame, text='Welcome to About page of \n Test version of REYE', bg='pink')
#     AbLabel.pack()
#     AbLabel2 = Label(AbFrame2, bg='pink', text='Links for Developers \n or smth')
#     AbLabel2.pack()
#     AbLabel3 = Label(AbFrame2, bg='pink', text='Github link', fg='blue')
#     AbLabel4 = Label(AbFrame2, bg='pink', text='Vk link', fg='blue')
#     AbLabel3.bind('<Button-1>', link)
#     AbLabel4.bind('<Button-1>', link1)
#     AbLabel3.pack()
#     AbLabel4.pack()
#     AbFrame.place(x=47, y=17, relwidth=0.8, relheight=0.3)
#     AbFrame2.place(x=167, y=111, relwidth=0.3, relheight=0.5)

def reye():
    def newf():
        global filename
        filename = 'Untitled'
        text.delete('1.0', END)

    def savef():
        data = text.get('1.0', END)
        out = open(filename, 'w')
        out.write(data)
        out.close

    def saveas():
        out = asksaveasfile(mode='w', defaultextension='.txt')
        data = text.get('1.0', END)
        try:
            out.write(data.rstrip())
        except Exception:
            showerror(title='DAMN BOY', message="Where'd you found DIS?")

    def openf():
        global filename
        inp = askopenfile(mode='r')
        if inp is None:
            return
        filename = inp.name

        data = inp.read()
        text.delete('1.0', END)
        text.insert('1.0', data)


bl = Label(canvas, image=interficeImg, bg='#13111E')
bl.place( relheight=1, relwidth=1)

# Lf = Frame(canvas,bg='blue')
# Lf.place(relx=0.5,rely=0.8,relwidth=0.8,relheight=0.13,anchor=N)

# b1 = Button(Lf,bd=1,image=img,command=reye)
# b2 = Button(Lf,bd=1,image=img,command=About)
# b3 = Button(Lf,bd=1,image=img,command=msg)
# b1.place(relwidth=0.33,relheight=1,bordermode='inside')
# b2.place(relx=0.33,relwidth=0.34,relheight=1)
# b3.place(relx=0.67,relwidth=0.33,relheight=1)


# Main Interfice#
rFrame = Frame(canvas, bg='pink')
rFrame2 = Frame(canvas, bg='#13111E')
rFrame3 = Frame(canvas, bg='pink')
rFrame4 = Frame(canvas, bg='pink')
rFrame.place(x=20, y=40, relwidth=0.33, relheight=0.1)
rFrame2.place(x=250, y=20, width=220, height=80)#relwidth=0.4, relheight=0.2)
rFrame3.place(x=10, y=120, relwidth=0.5, relheight=0.6)
# rFrame4.place(x=260, y=100, relwidth=0.4, relheight=0.6)
# text = Text(rFrame4, bg='pink', width=100, height=10)
# buttons
# b1 = Button(rFrame4,bd=1,bg='pink',text='New',command=newf)
# b2 = Button(rFrame4,bd=1,bg='pink',text='Open', command=openf)
# b3 = Button(rFrame4,bd=1,bg='pink',text='Save', command=savef)
# b4 = Button(rFrame4,bd=1,bg='pink',text='Save as', command=saveas)
# b1.place(y=20,relx=0,relwidth=0.25,relheight=0.1)
# b2.place(y=20,relx=0.25,relwidth=0.25,relheight=0.1)
# b3.place(y=20,relx=0.50,relwidth=0.25,relheight=0.1)
# b4.place(y=20,relx=0.75,relwidth=0.25,relheight=0.1)
# labels
time1 = ''
rLabel = Label(rFrame, text=time1, fg='#00ffff', bg='#13111E', font=('Roboto', 16))
rLabel2 = Label(rFrame2, text=Weather.weatherText,fg='#00ffff', bg='#13111E', font=('Roboto', 13))
iconFrame = Frame(rFrame2, bg='green')
iconic = Label(iconFrame,bg='#13111E', image=img4)

# rLabel3 = Label(rFrame3 , text='Карта?', bg='pink')
# rLabel4 = Label(rFrame4, text='Заметки', bg='pink')
rLabel.pack(fill=BOTH, expand=1)
rLabel2.pack(side=LEFT)
#iconic.pack(side=LEFT, expand=1)
iconFrame.place(relwidth=0.18, relheight=0.3, relx=0.8, y=14)

iconic.pack()

# rLabel3.pack()
# rLabel4.place(relheight=0.1, x=73)
# text.place(rely=0.2, relx=0, relheight=0.8, relwidth=1)


# clock = Label(root, font=('times', 20, 'bold'), bg='green')
# clock.pack(fill=BOTH, expand=1)

def tick():
    global time1
    time2 = time.strftime('%d %b %H:%M')
    if time2 != time1:
        time1 = time2
        rLabel.config(text=time2)
    rLabel.after(500, tick)
    print(time1)


# Map&Browser
class MainFrame(tk.Frame):
    def __init__(self, root):
        self.browser_frame = None
        self.navigation_bar = None

        # Root
        # root.geometry("260x200")
        tk.Grid.rowconfigure(rFrame3, 0, weight=1)
        tk.Grid.columnconfigure(rFrame3, 0, weight=1)

        # MainFrame
        tk.Frame.__init__(self, rFrame3)
        # self.master.title("Tkinter example")
        # self.master.protocol("WM_DELETE_WINDOW", self.on_close)
        # self.master.bind("<Configure>", self.on_root_configure)
        self.setup_icon()
        self.bind("<Configure>", self.on_configure)
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)

        # NavigationBar
        self.navigation_bar = NavigationBar(self)
        self.navigation_bar.grid(row=0, column=0,
                                 sticky=(tk.N + tk.S + tk.E + tk.W))
        tk.Grid.rowconfigure(self, 0, weight=0)
        tk.Grid.columnconfigure(self, 0, weight=0)

        # BrowserFrame
        self.browser_frame = BrowserFrame(self, self.navigation_bar)
        self.browser_frame.grid(row=1, column=0,
                                sticky=(tk.N + tk.S + tk.E + tk.W))
        tk.Grid.rowconfigure(self, 1, weight=1)
        tk.Grid.columnconfigure(self, 0, weight=1)

        # Pack MainFrame
        self.pack(fill=tk.BOTH, expand=tk.YES)

    def on_root_configure(self, _):
        logger.debug("MainFrame.on_root_configure")
        if self.browser_frame:
            self.browser_frame.on_root_configure()

    def on_configure(self, event):
        logger.debug("MainFrame.on_configure")
        if self.browser_frame:
            width = event.width
            height = event.height
            if self.navigation_bar:
                height = height - self.navigation_bar.winfo_height()
            self.browser_frame.on_mainframe_configure(width, height)

    def on_focus_in(self, _):
        logger.debug("MainFrame.on_focus_in")

    def on_focus_out(self, _):
        logger.debug("MainFrame.on_focus_out")

    def on_close(self):
        if self.browser_frame:
            self.browser_frame.on_root_close()
        self.master.destroy()

    def get_browser(self):
        if self.browser_frame:
            return self.browser_frame.browser
        return None

    def get_browser_frame(self):
        if self.browser_frame:
            return self.browser_frame
        return None

    def setup_icon(self):
        resources = os.path.join(os.path.dirname(__file__), "resources")
        icon_path = os.path.join(resources, "tkinter" + IMAGE_EXT)
        if os.path.exists(icon_path):
            self.icon = tk.PhotoImage(file=icon_path)
            # noinspection PyProtectedMember
            self.master.call("wm", "iconphoto", self.master._w, self.icon)


class BrowserFrame(tk.Frame):

    def __init__(self, master, navigation_bar=None):
        self.navigation_bar = navigation_bar
        self.closing = False
        self.browser = None
        tk.Frame.__init__(self, master)
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)
        self.bind("<Configure>", self.on_configure)
        self.focus_set()

    def embed_browser(self):
        window_info = cef.WindowInfo()
        rect = [0, 0, self.winfo_width(), self.winfo_height()]
        window_info.SetAsChild(self.get_window_handle(), rect)
        self.browser = cef.CreateBrowserSync(window_info,
                                             url="file:///C:/Projects/PfC/venv/Test/MainTest/map1.html")  # todo
        assert self.browser
        self.browser.SetClientHandler(LoadHandler(self))
        self.browser.SetClientHandler(FocusHandler(self))
        self.message_loop_work()

    def get_window_handle(self):
        if self.winfo_id() > 0:
            return self.winfo_id()
        elif MAC:
            # On Mac window id is an invalid negative value (Issue #308).
            # This is kind of a dirty hack to get window handle using
            # PyObjC package. If you change structure of windows then you
            # need to do modifications here as well.
            # noinspection PyUnresolvedReferences
            from AppKit import NSApp
            # noinspection PyUnresolvedReferences
            import objc
            # Sometimes there is more than one window, when application
            # didn't close cleanly last time Python displays an NSAlert
            # window asking whether to Reopen that window.
            # noinspection PyUnresolvedReferences
            return objc.pyobjc_id(NSApp.windows()[-1].contentView())
        else:
            raise Exception("Couldn't obtain window handle")

    def message_loop_work(self):
        cef.MessageLoopWork()
        self.after(10, self.message_loop_work)

    def on_configure(self, _):
        if not self.browser:
            self.embed_browser()

    def on_root_configure(self):
        # Root <Configure> event will be called when top window is moved
        if self.browser:
            self.browser.NotifyMoveOrResizeStarted()

    def on_mainframe_configure(self, width, height):
        if self.browser:
            if WINDOWS:
                ctypes.windll.user32.SetWindowPos(
                    self.browser.GetWindowHandle(), 0,
                    0, 0, width, height, 0x0002)
            elif LINUX:
                self.browser.SetBounds(0, 0, width, height)
            self.browser.NotifyMoveOrResizeStarted()

    def on_focus_in(self, _):
        logger.debug("BrowserFrame.on_focus_in")
        if self.browser:
            self.browser.SetFocus(True)

    def on_focus_out(self, _):
        logger.debug("BrowserFrame.on_focus_out")
        if self.browser:
            self.browser.SetFocus(False)

    def on_root_close(self):
        if self.browser:
            self.browser.CloseBrowser(True)
            self.clear_browser_references()
        self.destroy()

    def clear_browser_references(self):
        # Clear browser references that you keep anywhere in your
        # code. All references must be cleared for CEF to shutdown cleanly.
        self.browser = None


class LoadHandler(object):

    def __init__(self, browser_frame):
        self.browser_frame = browser_frame

    def OnLoadStart(self, browser, **_):
        if self.browser_frame.master.navigation_bar:
            self.browser_frame.master.navigation_bar.set_url(browser.GetUrl())


class FocusHandler(object):

    def __init__(self, browser_frame):
        self.browser_frame = browser_frame

    def OnTakeFocus(self, next_component, **_):
        logger.debug("FocusHandler.OnTakeFocus, next={next}"
                     .format(next=next_component))

    def OnSetFocus(self, source, **_):
        logger.debug("FocusHandler.OnSetFocus, source={source}"
                     .format(source=source))
        return False

    # def OnGotFocus(self, **_):
    #     """Fix CEF focus issues (#255). Call browser frame's focus_set
    #        to get rid of type cursor in url entry widget."""
    #     logger.debug("FocusHandler.OnGotFocus")
    #     self.browser_frame.focus_set()


class NavigationBar(tk.Frame):
    def __init__(self, master):
        self.back_state = tk.NONE
        self.forward_state = tk.NONE
        self.back_image = None
        self.forward_image = None
        self.reload_image = None

        tk.Frame.__init__(self, master)
        resources = os.path.join(os.path.dirname(__file__), "resources")

        # Back button
        back_png = os.path.join(resources, "back" + IMAGE_EXT)
        if os.path.exists(back_png):
            self.back_image = tk.PhotoImage(file=back_png)
        self.back_button = tk.Button(self, image=self.back_image,
                                     command=self.go_back)
        # self.back_button.grid(row=0, column=0)
        # Forward button
        forward_png = os.path.join(resources, "forward" + IMAGE_EXT)
        if os.path.exists(forward_png):
            self.forward_image = tk.PhotoImage(file=forward_png)
        self.forward_button = tk.Button(self, image=self.forward_image,
                                        command=self.go_forward)
        # self.forward_button.grid(row=0, column=1)
        # Reload button
        reload_png = os.path.join(resources, "reload" + IMAGE_EXT)
        if os.path.exists(reload_png):
            self.reload_image = tk.PhotoImage(file=reload_png)
        self.reload_button = tk.Button(self, image=self.reload_image,
                                       command=self.reload)
        # self.reload_button.grid(row=0, column=2)

        # Url entry
        self.url_entry = tk.Entry(self)
        self.url_entry.bind("<FocusIn>", self.on_url_focus_in)
        self.url_entry.bind("<FocusOut>", self.on_url_focus_out)
        self.url_entry.bind("<Return>", self.on_load_url)
        self.url_entry.bind("<Button-1>", self.on_button1)
        # self.url_entry.grid(row=0, column=3,
        #                    sticky=(tk.N + tk.S + tk.E + tk.W))
        tk.Grid.rowconfigure(self, 0, weight=100)
        tk.Grid.columnconfigure(self, 3, weight=100)

        # Update state of buttons
        self.update_state()

    def go_back(self):
        if self.master.get_browser():
            self.master.get_browser().GoBack()

    def go_forward(self):
        if self.master.get_browser():
            self.master.get_browser().GoForward()

    def reload(self):
        if self.master.get_browser():
            self.master.get_browser().Reload()

    def set_url(self, url):
        self.url_entry.delete(0, tk.END)
        self.url_entry.insert(0, url)

    def on_url_focus_in(self, _):
        logger.debug("NavigationBar.on_url_focus_in")

    def on_url_focus_out(self, _):
        logger.debug("NavigationBar.on_url_focus_out")

    def on_load_url(self, _):
        if self.master.get_browser():
            self.master.get_browser().StopLoad()
            self.master.get_browser().LoadUrl(self.url_entry.get())

    def on_button1(self, _):
        """Fix CEF focus issues (#255). See also FocusHandler.OnGotFocus."""
        logger.debug("NavigationBar.on_button1")
        self.master.master.focus_force()

    def update_state(self):
        browser = self.master.get_browser()
        if not browser:
            if self.back_state != tk.DISABLED:
                self.back_button.config(state=tk.DISABLED)
                self.back_state = tk.DISABLED
            if self.forward_state != tk.DISABLED:
                self.forward_button.config(state=tk.DISABLED)
                self.forward_state = tk.DISABLED
            self.after(100, self.update_state)
            return
        if browser.CanGoBack():
            if self.back_state != tk.NORMAL:
                self.back_button.config(state=tk.NORMAL)
                self.back_state = tk.NORMAL
        else:
            if self.back_state != tk.DISABLED:
                self.back_button.config(state=tk.DISABLED)
                self.back_state = tk.DISABLED
        if browser.CanGoForward():
            if self.forward_state != tk.NORMAL:
                self.forward_button.config(state=tk.NORMAL)
                self.forward_state = tk.NORMAL
        else:
            if self.forward_state != tk.DISABLED:
                self.forward_button.config(state=tk.DISABLED)
                self.forward_state = tk.DISABLED
        self.after(100, self.update_state)


if __name__ == '__main__':
    logger.setLevel(_logging.INFO)
    stream_handler = _logging.StreamHandler()
    formatter = _logging.Formatter("[%(filename)s] %(message)s")
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.info("CEF Python {ver}".format(ver=cef.__version__))
    logger.info("Python {ver} {arch}".format(
        ver=platform.python_version(), arch=platform.architecture()[0]))
    logger.info("Tk {ver}".format(ver=tk.Tcl().eval('info patchlevel')))
    assert cef.__version__ >= "55.3", "CEF Python v55.3+ required to run this"
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    # root = tk.Tk()
    app = MainFrame(root)
    # Tk must be initialized before CEF otherwise fatal error (Issue #306)
    cef.Initialize()

tick()
root.mainloop()
cef.Shutdown()
