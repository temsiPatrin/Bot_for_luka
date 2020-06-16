class Commander:
    last_msg = ""

    def reKeyboard(self,text:str):

        if text == "Начать":
            return "start_activity"
        if text == "В начало":
            return "start"
        if text == "О компании":
            return "start_activity"
        if text == "Хочу сетку":
            self.last_msg = "корпус"
            return "color_canvas"
        if self.last_msg == "корпус":
            self.last_msg = ""
            return "color_korpus"

        return "start"


    def reMsg(self,text:str):
        if text == "Начать":
            return "Я бот компании\n Выбери действие которое хочешь совершить"
        if text == "В начало":
            return "Нажми на кнопку начать"
        if text == "О компании":
            return "Иформация о компании..............."
        if text == "Хочу сетку":
            return "Выбери цвет полотна"
        if self.last_msg == "корпус":
            return "Выбери цвет корпуса"

        return "Нажми на кнопку начать"
