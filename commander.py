class Commander:

    def reKeyboard(self,text:str):

        if text == "Начать":
            return "start_activity"
        if text == "В начало":
            return "start"
        return "start"


    def reMsg(self,text:str):
        if text == "Начать":
            return "Я бот компании\n Выбери действие которое хочешь совершить"
        if text == "В начало":
            return "Нажми на кнопку начать"
        return "Нажми на кнопку начать"
