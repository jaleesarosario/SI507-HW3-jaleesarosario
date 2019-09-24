def askquestion():
    information= input("What is your question?")
    return information


def magic_answers():
m_ball= {1:"It is certain", 2: "It is decidedly so.", 3: "Without a doubt", 4:"Yes - definitely", 5: "You may rely on it", 6: "As I see it, yes.", 7: "Most likely", 8:"Outlook good", 9: "Signs point to yes", 10: "Reply hazy, try again", 11: "Ask again later", 12: "Better not tell you now", 13: "Cannot predict now", 14: "Concentrate and ask again", 15:"Don’t count on it", 16:"My reply is no", 17: "My sources say no", 18: "Outlook not good", 19: "Very doutbful", 20: "Yes"}
answer= random.randint(1, 20)
Print(m_ball[answer])

