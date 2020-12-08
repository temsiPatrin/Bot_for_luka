class Commander:
    last_msg = ""
    color_canvas = ""
    color_korpus = ""
    width = ""
    height = ""

    def reKeyAndMsg(self, text:str):
        if text == "Начать":
            keyboard = "start_activity"
            message = "Я бот компании\n Выбери действие которое хочешь совершить"
            km = [keyboard, message]
            return km
        if text == "В начало":
            keyboard = "start"
            message = "Нажми на кнопку начать"
            km = [keyboard, message]
            return km
        if text == "О компании":
            keyboard = "start_activity"
            message = "Иформация о компании..............."
            km = [keyboard, message]
            return km
        if text == "Хочу сетку":
            keyboard = "color_canvas"
            message = "Выбери цвет полотна"
            self.last_msg = "корпус"
            km = [keyboard, message]
            return km
        if self.last_msg == "корпус":
            keyboard = "color_korpus"
            message = "Выбери цвет корпуса"
            self.color_canvas = text
            self.last_msg = "высота"
            km = [keyboard, message]
            return km
        if self.last_msg == "высота":
            keyboard = "none"
            message = "Напиши высоту окна в милиметрах"
            self.color_korpus = text
            self.last_msg = "ширина"
            km = [keyboard, message]
            return km
        if self.last_msg == "ширина":
            keyboard = "none"
            message = "Напиши ширину окна в милиметрах"
            self.height = text
            self.last_msg = "конец"
            km = [keyboard, message]
            return km
        if self.last_msg == "конец":
            keyboard = "end"
            self.width = text
            self.last_msg = "конец"
            message = "Хорошо\n" \
                      "Цвет полотна: " + self.color_canvas + "\n" \
                      "Цвет корпуса: " + self.color_korpus + "\n" \
                      "Высота и ширина: " + self.height + "мм, " + self.width + "мм\n" \
                      "Цена сетки: " + self.priceNet(self.width, self.height)
            km = [keyboard, message]
            return km
        km = ["start", "Нажми на кнопку начать"]
        return km


    def priceNet(self, s1:str, s2:str):
        w = int(s1)/1000
        h = int(s2)/1000

        if w > 5 or w <= 0 or h > 5 or h <= 0:
            return "Некорректные размеры окна, не могу посчитать цену"

        s = w*h
        price = 2788

        if s <= 1:
            return str(price)
        else:
            return str(price*s)
