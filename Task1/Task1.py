import datetime


class Client:
    history = []
    start_time = None

    def __init__(self, name, description, sessioncount):
        self.Name = name
        self.Description = description
        self.Sessioncount = sessioncount

    def decrease_sessioncount(self):
        self.Sessioncount = self.Sessioncount - 1

    def start_torture(self):
        if self.start_time is None and self.Sessioncount > 0:
            self.start_time = datetime.datetime.now()
        else:
            print("No more sessions")

    def stop_torture(self):
        if self.start_time is not None:
            stop_time = datetime.datetime.now()
            torture_time = stop_time - self.start_time
            self.history.append(
                "{0} was {1} {2} {3}".format(self.Name, self.Description, self.start_time, torture_time))
            self.start_time = None
            self.decrease_sessioncount()

    def print_Client(self):
        print("{0} is to be {1} : {2} Sessions remaining".format(self.Name, self.Description, self.Sessioncount))

    def print_history(self):
        for i in self.history:
            print(i)

    def get_name(self):
        return self.Name

    def active_torture(self):
        print("{0} is being {1}".format(self.Name, self.Description))
