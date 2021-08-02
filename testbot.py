import museumbot.bot
import museumbot.bot as bot
while True:
    question = input(" 질문입력: ")
    answer= bot.search_answer_from_bot(question)
    print(answer)