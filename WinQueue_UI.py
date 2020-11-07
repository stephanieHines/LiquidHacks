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
            master = settings_frame, text = 'OK', font = DEFAULT_FONT)

        self.ok_button.grid(row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.W + tkinter.N + tkinter.S)

        cancel_button = tkinter.Button(
            master = settings_frame, text = 'Cancel', font = DEFAULT_FONT,
            command = self._cancel_button)

        cancel_button.grid(row = 2, column = 1, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.W + tkinter.N + tkinter.S)
      
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

    def run(self) -> None:
        self._root_window.mainloop()

    def _cancel_button(self):
        self._root_window.destroy()

if __name__ == '__main__':
    WinQueueUI().run()
