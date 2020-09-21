import config
import telegram

# 텔레그램 핸들러


def telegramHandler(place, blankSeatCount):
    telegramToken = config.TELEGRAM_TOKEN

    bot = telegram.Bot(token=telegramToken)

    """
    telegram 채팅방 chat_id 얻는 방법
    알리미 봇 채팅방에서 아무 메시지 전송 후 아래 코드 실행 시 채팅방의 chat_id 출력

    updates = bot.getUpdates()

    print(updates)

    for i in updates:
        print(i)

    """

    bot.sendMessage(
        chat_id=config.chat_id, text=f"시험장소 {place}에 {blankSeatCount}자리 있습니다."
    )

    return
