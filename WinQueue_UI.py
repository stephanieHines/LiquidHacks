__author__ = 'Derek Morales'

import tkinter
import MatchHistoryGrabber


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
        self.api = None

    def run(self) -> None:
        self._root_window.mainloop()

    def _cancel_button(self):
        self._root_window.destroy()

    def get_ig(self) -> int:
        return self.ig
    def get_api(self) -> int:
        return self.api
    def _ok_button(self):
        self.ig = self._ig_entry.get()
        self.api = self._api_entry.get()
        self._root_window.destroy()

class QuizUI:
    def __init__(self, ig,riot_api_key):
        self._quiz_window = tkinter.Tk()
        self.top = tkinter.PhotoImage(master = self._quiz_window, file = "DariusSquare.gif")
        self.top_emote = tkinter.PhotoImage(master = self._quiz_window, file = "Youre-Next-Emote.gif")
        self.jungle = tkinter.PhotoImage(master = self._quiz_window, file = "Lee-SinSquare.gif")
        self.jungle_emote = tkinter.PhotoImage(master = self._quiz_window, file = "Yikes-Emote.gif")
        self.mid = tkinter.PhotoImage(master = self._quiz_window, file = "ZedSquare.gif")
        self.mid_emote = tkinter.PhotoImage(master = self._quiz_window, file = "Tough-Times-Emote.gif")
        self.adc = tkinter.PhotoImage(master = self._quiz_window, file = "AsheSquare.gif")
        self.adc_emote = tkinter.PhotoImage(master = self._quiz_window, file = "Adoeable-Emote.gif")
        self.supp = tkinter.PhotoImage(master = self._quiz_window, file = "DJSonaSquare.gif")
        self.supp_emote = tkinter.PhotoImage(master = self._quiz_window, file = "Are-You-Serious-Emote.gif")
        self.ig = ig
        self.riot_api_key = riot_api_key
        self.winrate =0
        self._canvas = tkinter.Canvas(
            master = self._quiz_window, width = 400, height = 500)

        self.title_label = tkinter.Label(
            master = self._quiz_window, text = "Hello {}! What role do you play?".format(ig),
            font = DEFAULT_FONT)

        self.title_label.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N)

        self.choice_frame = tkinter.Frame(master = self._quiz_window)

        self.choice_frame.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.S)
        
        self.top_button = tkinter.Button(
            master = self.choice_frame, text = 'Top Lane', font = DEFAULT_FONT,
            command = self.toplane_command)
        
        self.top_button.grid(row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)

        top_label = tkinter.Label(
            master = self.choice_frame, image = self.top)

        top_label.grid(
            row = 0, column = 1, padx = 10, pady = 10,
            sticky = tkinter.E)

        self.jungle_button = tkinter.Button(
            master = self.choice_frame, text = 'Jungle', font = DEFAULT_FONT,
            command = self.jungle_command)
        
        self.jungle_button.grid(row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)

        jungle_label = tkinter.Label(
            master = self.choice_frame, image = self.jungle)

        jungle_label.grid(
            row = 1, column = 1, padx = 10, pady = 10,
            sticky = tkinter.E)

        self.mid_button = tkinter.Button(
            master = self.choice_frame, text = 'Mid Lane', font = DEFAULT_FONT,
            command = self.midlane_command)
        
        self.mid_button.grid(row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)

        mid_label = tkinter.Label(
            master = self.choice_frame, image = self.mid)

        mid_label.grid(
            row = 2, column = 1, padx = 10, pady = 10,
            sticky = tkinter.E)

        self.adc_button = tkinter.Button(
            master = self.choice_frame, text = 'Bot Lane', font = DEFAULT_FONT,
            command = self.botlane_command)
        
        self.adc_button.grid(row = 0, column = 2, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)

        adc_label = tkinter.Label(
            master = self.choice_frame, image = self.adc)

        adc_label.grid(
            row = 0, column = 3, padx = 10, pady = 10,
            sticky = tkinter.E)

        self.support_button = tkinter.Button(
            master = self.choice_frame, text = 'Support', font = DEFAULT_FONT,
            command = self.support_command)
        
        self.support_button.grid(row = 1, column = 2, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)

        support_label = tkinter.Label(
            master = self.choice_frame, image = self.supp)

        support_label.grid(
            row = 1, column = 3, padx = 10, pady = 10,
            sticky = tkinter.E)
        
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        
    def run(self) -> None:
        self._quiz_window.mainloop()

    def toplane_command(self):
        self.choice_frame.destroy()
        self.title_label.config(text = "You're a lone wolf.")
        topemote_label = tkinter.Label(
            master = self._quiz_window, image = self.top_emote)
        topemote_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S)
        self.ok_button = tkinter.Button(
            master = self._quiz_window, text = 'OK', font = DEFAULT_FONT,
            command = self._ok_button)

        self.ok_button.grid(row = 2, column = 0, padx = 10, pady = 10,
            sticky =  tkinter.S)

    def jungle_command(self):
        self.choice_frame.destroy()
        self.title_label.config(text = "You're a masochist.")
        topemote_label = tkinter.Label(
            master = self._quiz_window, image = self.jungle_emote)
        topemote_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S)
        self.ok_button = tkinter.Button(
            master = self._quiz_window, text = 'OK', font = DEFAULT_FONT,
            command = self._ok_button)

        self.ok_button.grid(row = 2, column = 0, padx = 10, pady = 10,
            sticky =  tkinter.S)

    def midlane_command(self):
        self.choice_frame.destroy()
        self.title_label.config(text = "You're a control freak.")
        topemote_label = tkinter.Label(
            master = self._quiz_window, image = self.mid_emote)
        topemote_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S)
        self.ok_button = tkinter.Button(
            master = self._quiz_window, text = 'OK', font = DEFAULT_FONT,
            command = self._ok_button)

        self.ok_button.grid(row = 2, column = 0, padx = 10, pady = 10,
            sticky =  tkinter.S)

    def botlane_command(self):
        self.choice_frame.destroy()
        self.title_label.config(text = "You're a star.")
        topemote_label = tkinter.Label(
            master = self._quiz_window, image = self.adc_emote)
        topemote_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S)
        self.ok_button = tkinter.Button(
            master = self._quiz_window, text = 'OK', font = DEFAULT_FONT,
            command = self._ok_button)

        self.ok_button.grid(row = 2, column = 0, padx = 10, pady = 10,
            sticky =  tkinter.S)

    def support_command(self):
        self.choice_frame.destroy()
        self.title_label.config(text = "You're a babysitter.")
        topemote_label = tkinter.Label(
            master = self._quiz_window, image = self.supp_emote)
        topemote_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S)
        self.ok_button = tkinter.Button(
            master = self._quiz_window, text = 'OK', font = DEFAULT_FONT,
            command = self._ok_button)

        self.ok_button.grid(row = 2, column = 0, padx = 10, pady = 10,
            sticky =  tkinter.S)
    def _ok_button(self):
        #progbar = tkinter.ttk.Progressbar(parent = self._quiz_window, orient='horizontal', length=200, mode='indeterminate')
        #progbar.start()
        self.winrate = self.getWinrate()
        #progbar.stop()
        self._quiz_window.destroy()
    def getWinrate(self):
        return MatchHistoryGrabber.getMatchHistory(self.riot_api_key,self.ig)
    def getWinrateCalculated(self):
        return self.winrate

class winrateWindow:
    def __init__(self, winrate): 
        self.winrate_window = tkinter.Tk()
        self.loser_image = tkinter.PhotoImage(master=self.winrate_window, file = "r9E_Xctk-LnDTJCxh8aC6YI8Oz2QqQSEK_wdrGNggkLBtcUmokMmHbIORA6-q-rDqZVoJhJ-T-GToNJEZZ1k1PeL6L7GoR2uZmfi.gif")
        self.winner_image = tkinter.PhotoImage(master=self.winrate_window, file = "lol_league_of_legends_pool_party_taliyah_updated.gif")
        self.hardstuck_image = tkinter.PhotoImage(master= self.winrate_window, file ="t1rage.gif" )
        self._canvas = tkinter.Canvas(
            master = self.winrate_window, width = 400, height = 500)

        self.title_label = tkinter.Label(
            master = self.winrate_window, text = "Here is your win rate: {}".format(winrate), 
            font = DEFAULT_FONT)
        self.title_label.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N)

        self.result_frame = tkinter.Frame(master = self.winrate_window)
        self.result_frame.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N)
        if (winrate>.5):
            winemote_label = tkinter.Label(master = self.result_frame, image = self.winner_image)
            win_message_label = tkinter.Label(master = self.result_frame, text = "Congrats! You're in winners queue!",
                                              font = DEFAULT_FONT)
        elif (winrate<.5):
            winemote_label = tkinter.Label(master = self.result_frame, image = self.loser_image)
            win_message_label = tkinter.Label(master = self.result_frame, text = "Aww, you're in losers queue. I'm sorry for your teammates.",
                                              font = DEFAULT_FONT)
        else:
            winemote_label = tkinter.Label(master = self.result_frame, image = self.hardstuck_image)
            win_message_label = tkinter.Label(master = self.result_frame, text = "You're hardstuck in elo hell.",
                                              font = DEFAULT_FONT)
        
        winemote_label.grid(row = 0, column = 0, padx = 10, pady = 10,sticky = tkinter.N + tkinter.S)
        win_message_label.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.N + tkinter.S)

        cancel_button = tkinter.Button(
            master = self.result_frame, text = 'Finish', font = DEFAULT_FONT,
            command = self._cancel_button)

        cancel_button.grid(row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.W + tkinter.N + tkinter.S)
    def _cancel_button(self):
        self.winrate_window.destroy()
    def run(self) -> None:
        self.winrate_window.mainloop()


#make a button on each class frame that's says like "Calculate Your Winrate" or something
#pass pass it the winrate from MatchHistoryGrabber
# display winrate and a different statement based on >,<, or = .5  

if __name__ == '__main__':
    winqueue = WinQueueUI()
    winqueue.run()
    
    player_ig = winqueue.get_ig()
    riot_api_key = winqueue.get_api()
    
    quiz = QuizUI(player_ig,riot_api_key)
    quiz.run()
    winrate = quiz.getWinrateCalculated()
    winrateWindow(winrate).run()
    


    #'RGAPI-740dbc19-ef19-4c6f-bcc4-6e8f0a3fb8d2'
    


#have winrate calc in parallel?? <--????
#make winrate window pretty
#fix picture size in winrate display
#put close button on winrate window to finish out quiz :)
