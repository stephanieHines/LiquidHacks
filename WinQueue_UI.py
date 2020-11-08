__author__ = 'Derek Morales'

import tkinter

DEFAULT_FONT = ('Times New Roman', 12)

class WinQueueUI:
    # Quick UI for Liquid Hackathon
    def __init__(self):
        self._root_window = tkinter.Tk()
        self.league = tkinter.PhotoImage(master = self._root_window, file = "lol.gif")

        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 400, height = 500,
            background = '#273746')
        
        self._canvas.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        start_label = tkinter.Label(
            master = self._root_window, image = self.league)

        start_label.place(x=0, y=-60, relwidth=1, relheight=1)

        text_label = tkinter.Label(
            master = self._root_window, text = "Hi there! Welcome! Here you'll learn more\nabout yourself and your winrate through this lego legends quiz.",
            font = DEFAULT_FONT)

        text_label.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N)

        settings_frame = tkinter.Frame(master = self._root_window)

        settings_frame.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.S)

        self.ig_label = tkinter.Label(
            master = settings_frame, text = "Enter your In Game League Name.",
            font = DEFAULT_FONT)

        self.ig_label.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.S)

        self.api_label = tkinter.Label(
            master = settings_frame, text = "Enter your Riot API Key.",
            font = DEFAULT_FONT)

        self.api_label.grid(
            row = 0, column = 1, padx = 10, pady = 10,
            sticky = tkinter.S)

        self._api_entry = tkinter.Entry(
            master = settings_frame, width = 36, font = DEFAULT_FONT)

        self._api_entry.grid(
            row = 1, column = 1, padx = 10, pady = 10,
            sticky = tkinter.S)

        self._ig_entry = tkinter.Entry(
            master = settings_frame, width = 20, font = DEFAULT_FONT)

        self._ig_entry.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.S)

        self.ok_button = tkinter.Button(
            master = settings_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._ok_button)

        self.ok_button.grid(row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.W + tkinter.N + tkinter.S)

        cancel_button = tkinter.Button(
            master = settings_frame, text = 'Cancel', font = DEFAULT_FONT,
            command = self._cancel_button)

        cancel_button.grid(row = 2, column = 1, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.W + tkinter.N + tkinter.S)
      
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        self.ig = None

    def run(self) -> None:
        self._root_window.mainloop()

    def _cancel_button(self):
        self._root_window.destroy()

    def get_ig(self) -> int:
        return self.ig

    def _ok_button(self):
        self.ig = self._ig_entry.get()
        self._root_window.destroy()

class QuizUI:
    def __init__(self, ig):
        self._quiz_window = tkinter.Tk()
        self.top = tkinter.PhotoImage(master = self._quiz_window, file = "DariusSquare.gif")
        self.jungle = tkinter.PhotoImage(master = self._quiz_window, file = "Lee-SinSquare.gif")
        self.mid = tkinter.PhotoImage(master = self._quiz_window, file = "ZedSquare.gif")
        self.adc = tkinter.PhotoImage(master = self._quiz_window, file = "AsheSquare.gif")
        self.supp = tkinter.PhotoImage(master = self._quiz_window, file = "DJSonaSquare.gif")

        self._canvas = tkinter.Canvas(
            master = self._quiz_window, width = 400, height = 500)

        title_label = tkinter.Label(
            master = self._quiz_window, text = "Hello {}! What role do you play?".format(ig),
            font = DEFAULT_FONT)

        title_label.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N)

        choice_frame = tkinter.Frame(master = self._quiz_window)

        choice_frame.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.S)
        
        self.top_button = tkinter.Button(
            master = choice_frame, text = 'Top Lane', font = DEFAULT_FONT,command =self._displayAns("top"))
        
        self.top_button.grid(row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)

        top_label = tkinter.Label(
            master = choice_frame, image = self.top)

        top_label.grid(
            row = 0, column = 1, padx = 10, pady = 10,
            sticky = tkinter.E)

        self.jungle_button = tkinter.Button(
            master = choice_frame, text = 'Jungle', font = DEFAULT_FONT,command =self._displayAns("jung"))
        
        self.jungle_button.grid(row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)

        jungle_label = tkinter.Label(
            master = choice_frame, image = self.jungle)

        jungle_label.grid(
            row = 1, column = 1, padx = 10, pady = 10,
            sticky = tkinter.E)

        self.mid_button = tkinter.Button(
            master = choice_frame, text = 'Mid Lane', font = DEFAULT_FONT,command =self._displayAns("mid"))
        
        self.mid_button.grid(row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)

        mid_label = tkinter.Label(
            master = choice_frame, image = self.mid)

        mid_label.grid(
            row = 2, column = 1, padx = 10, pady = 10,
            sticky = tkinter.E)

        self.adc_button = tkinter.Button(
            master = choice_frame, text = 'Bot Lane', font = DEFAULT_FONT,command =self._displayAns("adc"))
        
        self.adc_button.grid(row = 0, column = 2, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)

        adc_label = tkinter.Label(
            master = choice_frame, image = self.adc)

        adc_label.grid(
            row = 0, column = 3, padx = 10, pady = 10,
            sticky = tkinter.E)

        self.support_button = tkinter.Button(
            master = choice_frame, text = 'Support', font = DEFAULT_FONT,command =self._displayAns("supp"))
        
        self.support_button.grid(row = 1, column = 2, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)

        support_label = tkinter.Label(
            master = choice_frame, image = self.supp)

        support_label.grid(
            row = 1, column = 3, padx = 10, pady = 10,
            sticky = tkinter.E)
        
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
    def _displayAns(self, role):
        self.role = role
        Ans(role).run()
        #self._quiz_window.destroy()

    def run(self) -> None:
        self._quiz_window.mainloop()

class Ans:
    def __init__(self,role):
        self._ans_win = tkinter.Tk()
        #self.league = tkinter.PhotoImage(master = self._root_window, file = "AsheSquare")

        self._canvas = tkinter.Canvas(
            master = self._ans_win, width = 400, height = 500,
            background = '#273746')

        ans_frame = tkinter.Frame(master = self._ans_win)
        ans_frame.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.S)
        
        if (self.isAdc):
            tkinter.Label(
            master = self._ans_win, text = "You're a star :)",
            font = DEFAULT_FONT)
        #elif (self.isJung):
           # tkinter.Label(master=self._ans_win, text = "You're a masochist ;)", font = DEFAULT_FONT)
        #elif 
        choice_frame = tkinter.Frame(master = self._ans_win)
    def run(self) -> None:
        self._ans_win.mainloop()
       

    def isAdc(self, role):
        return role == "adc"
    def isTop(self,role):
        return role == "top"
    def isMid(self, role):
        return role == "mid"
    def isSupp(self, role):
        return role == "supp"
    def isJung(self, role):
        return role == "jung"

if __name__ == '__main__':
    winqueue = WinQueueUI()
    winqueue.run()
    player_ig = winqueue.get_ig()
    QuizUI(player_ig).run()
    
    
