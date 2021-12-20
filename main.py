# Python script to control fuel transfer and cleaning between tanks

if __name__ == '__main__':
    from guizero import App, Text

    app = App(title='Fuel Tank Control', width=1024, height=600)

    t = Text(app, text="Test")

    app.display()
