
def loadQns(file_path):
    ans = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            # Read temple information
            temple_info = lines[i].strip().split(',')
            temple_name = temple_info[0]
            latitude = float(temple_info[1])
            longitude = float(temple_info[2])
            i += 1
            
            # Read questions for the temple
            questions = []
            while i < len(lines) and lines[i].strip():
                question_data = lines[i].strip().split(',')
                question = question_data[0]
                options = question_data[1:-1]
                correct_option = int(question_data[-1])
                questions.append([question, options, correct_option])
                i += 1
            
            # Skip any blank lines separating temples
            while i < len(lines) and not lines[i].strip():
                i += 1
            
            ans.append([(latitude, longitude), questions])
    
    return ans



#id(1,2,3) + 4digit code
games = []

#id: [[players w data (see below)], time_began]

gamesData = dict()

#username: [games:[type, {see below}]]
#cultural: quests completed
#geoguessr: quests completed
#classi: identity, isFrozen, isIce, item1, item2, num_unfreezes]
playersData = dict()

#[place, task_type, instruction, {see below}]
#quiz: [[location(tuple:longitude, latitude), [questions, [options],correctoptionindex]]
#match: [image files]
#riddle: [[location, question]]
culturalQuests = [
    ['Botanic Gardens', 'match', 'Eh, go lah to that one UNESCO heritage place, Botanic Gardens or whatever. Go smell some flowers, hug tree also can, then complain about the weather like true Singaporean.',
     []],
    ['Chinatown', 'quiz', 'Wah, go see temples ah? Buddha Tooth Temple, Mariamman, and Thian Hock Keng all waiting for you to kaypoh their history. Aish, you confirm dunno anything, just go take photo only right?',
     loadQns('chinatown.txt')],
    ['Marina bay Sands', 'quiz', 'Wah, Marina Bay Sands sia! Go there for what, learn ah? More like go take selfie at Infinity Pool and burn wallet at casino. Your bank account confirm cry one.',
     loadQns('MBS.txt')],
    ['Sixth Avenue', 'riddle', 'I’m not the first, nor the second, but I’m fancy enough to flaunt.\nI’m no mall, no street, but I’m a station with a numbery taunt.'],
    ["Serangoon",'', ''],
    ['Caldecott', '', ''],
    ['Mayflower', '', ''],
    ['Bukit Batok', '', ''],
    ['Yishun', '', ''],
    ['Newton', '', '']
]


