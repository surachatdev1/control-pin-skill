from mycroft import MycroftSkill, intent_file_handler


class ControlPin(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('pin.control.intent')
    def handle_pin_control(self, message):
        number = message.data.get('number')

        self.speak_dialog('pin.control', data={
            'number': number
        })


def create_skill():
    return ControlPin()

