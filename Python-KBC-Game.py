Questions =[
    [
        "Who is the first Priminister of India ?" , "Amit Sah" , "Nitish Kumar", "Lalu prasad yadav" , "Narendra Damodar Das Modi",4
    ]
    ,
    [
        "Who was the first prasident of india ? " , " Shreemati Indra Gandhi ", "Pratibha singh patil" ,"Pd. Jwahar lal Nehru" ,"Dr. Rajendra Parasad ",4
    ]
    ,
    [
        "Who is the chife Minister of Bihar ?" , "Lalu Parasad yadav " , "Nitish Kumar", "Shusil Modi ", "Samrat Choudry",4
    ]
    ,
    [
        "Who is the chife Minister of Utter Pradesh ? ", "Mulayam Singh yadav" , "Akhilesh yadav" , " Shreemati Mayawati ji ", "Aaditay nath yogi ",4
    ]
    ,
    [
        "who was the first Priminister of India ?", " Atal Bihari bajpeyye " , "Dr. Manmohan Sing", "Narendra Das Modi " , "Pd. Jawahar lala nehru",4
    ]
    ,
    [
        "What is the capital of India?","Mumbai", "Kolkata", "Chennai", "New Delhi",4
    ]
    ,
    [
        "Which is the national animal of India?" , "Lion" , "Elephant" , "Leopard", "Tiger",4
    ]
    ,
    [
        "Which planet is known as the Red Planet?" , "Earth" , "Jupiter" , "Venus" , "Mars",4
    ]
    ,
    [
        "Who is known as the Father of the Nation in India?", "Jawaharlal Nehru", "Sardar Patel" , "Bhagat Singh" , "Mahatma Gandhi",4
    ]
    ,
    [
        "Which is the largest ocean in the world?" , "Atlantic Ocean" , "Indian Ocean" , "Arctic Ocean" , "Pacific Ocean",4
    ]
    ,
    [
        "How many colors are there in the Indian National Flag?" , "2" , "4" , "5" , "3",4
    ]
    ,
    [
        "Who wrote the Indian National Anthem?" , "Bankim Chandra Chattopadhyay" , "Sarojini Naidu" , "Premchand" , "Rabindranath Tagore",4
    ]
    ,
    [
        "Which is the largest continent in the world?" ,  " Africa" , "Europe" , "Australia" ,"Asia",4
    ]
    ,
    [
        "How many states are there in India?" , "22" , "27" , "29" ,"28",4
    ]
    ,
    [
        "What does ISRO stand for?" , "International Space Research Organisation" , "Indian Satellite Research Office" , "International Satellite Research Office" , "Indian Space Research Organisation",4
    ]
]

Level = [2000,3000,5000,10000, 20000 , 40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,30000000,70000000]
Money = 0
safemoney=0
for i in range (0 , len(Questions)):
    Question = Questions[i]
    print(Question[0])

    print(f"  \n          a. {Question[1]}                                                                      b.{Question [2]} ")
    print(f"          c.{Question [3]}                                                              d.{Question[4]}")
    Reply = int(input(f"enter the corect optionn (1-4) : "))

    if( Reply==Question[-1]):
        print(f"Corect ansewr won the Rs. {Level[i]}")
        Money= Level[i]
        print(Money)
        if(i==4):
            safemoney=10000
        elif(i==9):
            safemoney = 320000
        elif(i==13):
            safemoney = 10000000
        elif(i==14):
            safemoney=70000000
    else:
        Money=safemoney
        print(Money)
        break
print(f"Your tak home Money {Money}")