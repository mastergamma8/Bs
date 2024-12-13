from Classes.Packets.PiranhaMessage import PiranhaMessage


class AllianceDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeBoolean(True)

        self.writeLong(0, 1) # alliance ID
        self.writeString('haccers') # alliance name
        self.writeDataReference(8, 37) # alliance icon
        self.writeVInt(1) # type
        self.writeVInt(1) # member count
        self.writeVInt(9500) # total trophies
        self.writeVInt(0) # minimum trophies to enter
        self.writeVInt(0) # 0
        self.writeString('CA') # location
        self.writeVInt(1) # people online
        self.writeBoolean(True) # isFamilyFriendly
        self.writeVInt(20) 
        self.writeVInt(1) # if not 0: 2 more vint (piggy state)
        self.writeVInt(250) # piggy total wins
        self.writeVInt(1) # wins left until max reward

        self.writeString("this is the hacciest club in the world")

        self.writeVInt(1) # member count
        self.writeLong(0, 1) # player ID
        self.writeVInt(2) # role
        self.writeVInt(9500) # trophies
        self.writeVInt(0) # status: 0=offline 2=online
        self.writeVInt(1) # last connected time seconds ?
        highestPowerLeagueRank = 2
        self.writeVInt(highestPowerLeagueRank)
        if highestPowerLeagueRank != 0:
            self.writeVInt(2) #solo
            self.writeVInt(1) #duo
        self.writeBoolean(False) # boolean always false?

        self.writeString('risporce') # player name
        self.writeVInt(100) # VInt always 100
        self.writeVInt(28000183) # thumbnail
        self.writeVInt(43000008) # name color
        self.writeVInt(-1)

        self.writeVInt(-1) # most people have it -1 but some with something
        self.writeBoolean(False) # whats this ? only 2/30 people have it true in my club
        week = 58 # week 58 of club league as of 2023/07/05, this number is 0 if you just arrived in the club
        self.writeVInt(week)
        if week != 0: # club league week number?
            self.writeVInt(3) # day
            self.writeVInt(18) # total club trophies earned
            self.writeVInt(1) # event day club trophies earned
            self.writeVInt(8) # total tickets used
            self.writeVInt(2) # event day tickets used
            self.writeVInt(6) # event day max tickets
            self.writeVInt(6) # event day tickets left
            self.writeVInt(3) # event day player ranking
            self.writeBoolean(True) # everyone have it to true
        
        self.writeVInt(1)
        self.writeVInt(1) # if not 0: 3 more vints
        self.writeVInt(5) # piggy player wins
        self.writeVInt(6) # piggy player tickets
        self.writeVInt(10) # 
        #self.writeVInt(200) # player experience lvl but why tf it doesn't show for some people

    def decode(self):
        fields = {}
        super().decode(fields)
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24301

    def getMessageVersion(self):
        return self.messageVersion