import eel

eel.init('pthonappomg')

@eel.expose
def App():
    print("Lets bloody goooo")

App()

eel.start('app.html',size=(500,600))