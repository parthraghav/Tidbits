from tinyRSA.rsa import *

class Message:
	def __init__(self, msg, sender_node):
		self.contents = msg
		self.sender = sender_node

	def view(self):
		print("*"*8)
		print(self.contents)
		print('Sent by '+self.sender.getName())
		print("*"*8)

	def view_encrypted(self, wallet):
		print("*"*8)
		print( decrypt(self.contents, wallet) )
		print('Sent by '+self.sender.getName())		
		print("*"*8)


class Node:
	def __init__(self, name):
		self._keys = generate_keys()
		self._status = 1
		self._name = name
		self._inbox = []

	def getName(self):
		return self._name

	def _viewInbox(self):
		while len(self._inbox) > 0:
			view_encrypted( self._inbox[0], self._keys )
			self._inbox.pop(0)
		print("The inbox is currently empty!")

	def requestPublicKey(self):
		return self._keys[:2]
	
	def signalIncomingMessage(self, msg):
		if self._status == 1:
			self._inbox += msg
	
	def sendEncryptedMsg(self, node, msg):
		public_key = node.requestPublicKey()
		encrypted_msg = encrypt(msg, public_key)
		ready_msg = Message(encrypted_msg, self)
		node.signalIncomingMessage(ready_msg)


#node1 = {'keys': (13689267934752668487464617909158213783586525198460871801978474209956688970651974301864000684957404982343297930075946458751642895426411715724442053396534809364370271098759284754112594094963344896583522081952942486890918895856745597618666043884645541909419400521704089868186160398953364546129918905771003456479162496808624700899783518348809734284376017235911223132356958131574555302616718174091080834825370160552451225728518367003907456388566008001463086577137316761272870642291005870518271256838234199259701743980913266350003039902935855609096164944290230566249202260485971859676526097380423550220685261310691058564581, 6844633967376334243732308954579106891793262599230435900989237104978344485325987150932000342478702491171648965037973229375821447713205857862221026698267404682185135549379642377056297047481672448291761040976471243445459447928372798809333021942322770954709700260852044934093080199476682273064959452885501728239464245900802698528523553308125169202654407474490857620416914791763553863520759200173893063010458919049134734119830089947058666531741101164954588584885076042011187619135237427068232083891814751100021368353727495107642166020318404216762337985980828933935771533306704084294754675343826073037414016360663854710807, 6844633967376334243732308954579106891793262599230435900989237104978344485325987150932000342478702491171648965037973229375821447713205857862221026698267404682185135549379642377056297047481672448291761040976471243445459447928372798809333021942322770954709700260852044934093080199476682273064959452885501728239464245900802698528523553308125169202654407474490857620416914791763553863520759200173893063010458919049134734119830089947058666531741101164954588584885076042011187619135237427068232083891814751100021368353727495107642166020318404216762337985980828933935771533306704084294754675343826073037414016360663854710807), 'msg': 'hello'}
#node2 = {'keys': (16675545739875707894718851988874318710820313060008520243676248015708014885551008208982186590209781596421531267510206685830772910694027683968674985516714984560447649479046870187087548310964863984179009994135741632375603895956947770686525568798660397150415041052993153823307518445682721180471606318338064809528463258901780659186525770465328153121647616646759714427280332186663043918888089322322560570852345049211277067862784434988996311833514297266022502163383790929644180377417462338365075917801171624131334408149589729955799661805764762122240060183395093495208772270465603790008416961567588391019699063533661177185337, 8337772869937853947359425994437159355410156530004260121838124007854007442775504104491093295104890798210765633755103342915386455347013841984337492758357492280223824739523435093543774155482431992089504997067870816187801947978473885343262784399330198575207520526496576911653759222841360590235803159169032404764096573121866364984441672226052305527662222175274127179065992801861455573065218049800983082044362508627807821188885812534391150193400431106038239446572200439248783474396629307635433330076664111209040208496235549053723732477982114943133833473793703754521521349755388486865594228859632107781251168076862818985019, 8337772869937853947359425994437159355410156530004260121838124007854007442775504104491093295104890798210765633755103342915386455347013841984337492758357492280223824739523435093543774155482431992089504997067870816187801947978473885343262784399330198575207520526496576911653759222841360590235803159169032404764096573121866364984441672226052305527662222175274127179065992801861455573065218049800983082044362508627807821188885812534391150193400431106038239446572200439248783474396629307635433330076664111209040208496235549053723732477982114943133833473793703754521521349755388486865594228859632107781251168076862818985019), 'msg': 'bye'}