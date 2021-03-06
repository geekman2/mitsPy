from mitsPy.mitsubishicontroller import MitsubishiController


class Manager:
    def __init__(self, controller_url, path="/servlet/MIMEReceiveServlet"):
        self.controller = MitsubishiController(url=controller_url, path=path)
        self.controller.initialize()
        self.groups = self.controller.groups
