class BusinessCard:
    def __init__(self,name,surname,company,position,email):
        self.name = name
        self.surname = surname
        self.company = company
        self.position = position
        self.email = email

dataList=[['Adam','Wesołowski','SkyNet','AI Developer','A.W@Sky.net'],
          ['Piotr','Matyszczak','UmbrellaCorp.','BioEngineer','Piotr@UCorp.edu'],
          ['Monika','Potocka','IBM','ScrumMaster','Monika87@IBM.com'],
          ['Wacław','Nowak','MindGeek','Moderator','WN@mind.com'],
          ['Marcin','Kowalski','EY','Accountant','MarcinK@EY.eu']]

for i in range (len(dataList)):
    data = BusinessCard(name=dataList[i][0],surname=dataList[i][1],company=dataList[i][2],position=dataList[i][3],email=dataList[i][4])
    print(str(data.name)+' | '+str(data.surname)+' | '+str(data.company)+' | '+str(data.position)+' | '+str(data.email))



        