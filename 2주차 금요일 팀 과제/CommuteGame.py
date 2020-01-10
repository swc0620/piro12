commute = [['DMC', '합정', '신촌', '혜화', '청량리'],
           ['김포공항', '당산', '용산', '동역사', '왕십리'],
           ['까치산', '영등포구청', '노량진', '약수', '뚝섬'],
           ['계양', '신도림', '숭실대입구', '고속터미널', '건대입구'],
           ['부평구청', '대림', '서울대입구', '교대', '잠실'],
           ['None', 'None', '서울대', 'None', 'None']]

table = {'DMC':((0,0), (-10,-5)), '합정':((0,0), (-25, -15)), '신촌':((0,0), (-30,-20)),
         '혜화':((0,0), (-10, -5)), '청량리':((0,0), (-40, -30)), '김포공항':((0,0), (-20, -10), (-30,-20)),
         '당산':((0,0), (-20, -10)), '용산':((0,0), (-10, -5)), '동역사':((0,0), (-25, -15)), '왕십리':((0,0), (-45, -30), (-30, -20), (-10, -5), (-15, -10)),
         '까치산':((0,0), (-10, -5), (-10, -5)), '영등포구청':((0,0), (-20, -10)), '노량진':((0,0), (-10, -5), (-10, -5)),
         '약수':((0,0), (-15, -10)), '뚝섬':((0,0), (-40, -30), (-15, -20)), '계양':((0,0), (-15, -10), (-10, -5)),
         '신도림':((0,0), (-15, -10)), '숭실대입구':((0,0), (-10, -5), (-5, -5)), '고속터미널':((0,0), (-5, -5)),
         '건대입구':((0,0), (-35, -25)), '부평구청':((0,0), (-30, -20)), '대림':((0,0), (-15, -5)), '교대':((0,0), (-10, -5)),
         '잠실':((0,0), (-30, -20))}

destination = {'DMC':(None, (0,1)), '합정':((0,0), (4,2)), '신촌':((0,0), (4,2)),
         '혜화':((0,0), (1,3)), '청량리':((0,0), (3, 1)), '김포공항':((0,0), (2,1), (1,1)),
         '당산':((0,0), (4,2)), '용산':((0,0), (3, 1)), '동역사':((0,0), None, (4, 2)), '왕십리':((0,0), (4, 2), (2, 1), (1, 3), None),
         '까치산':((0,0), (3, 1), (2, 1)), '영등포구청':((0,0), (4, 2)), '노량진':((0,0), (3, 1), (4, 2)),
         '약수':((0,0), (4, 3)), '뚝섬':((0,0), (4, 2), None), '계양':((0,0), (4, 0), (1, 0)),
         '신도림':((0,0), (4, 2)), '숭실대입구':((0,0), None, (4, 2)), '고속터미널':((0,0), (4, 3)),
         '건대입구':((0,0), (4, 2)), '부평구청':((0,0), (4, 1)), '대림':((0,0), (4, 2)), '교대':((0,0), (4, 2)),
         '잠실':((0,0), (4, 2))}




class Gamer:
    def __init__(self, name, a, b):
        self.name = name
        self.time = 60
        self.energy = 100
        self.position = [a, b]

    def pos(self):
        a = self.position[0]
        b = self.position[1]
        return a, b

    def result(self, pos, answer):
        temp = table[pos][answer]
        self.time += temp[0]
        self.energy += temp[1]

    
def question(pos):
    if pos == 'DMC':
        print("0. 집으로 간다. (시간: 0, 체력: 0)")
        print("1. 6호선을 이용해 합정으로 간다. (시간: -10, 체력: -5)\n")
    elif pos == '합정':
        print("0. 집으로 간다. (시간: 0, 체력: 0)")
        print("1. 2호선을 이용해 서울대입구로 간다. (시간: -25, 체력: -15)\n")
    elif pos == '신촌':
        print("0. 집으로 간다. (시간: 0, 체력: 0)")
        print("1. 2호선을 이용해 서울대입구로 간다. (시간: -30, 체력: -20)\n")
    elif pos == '혜화':
        print("0. 집으로 간다. (시간: 0, 체력: 0)")
        print("1. 4호선을 이용해 동역사로 간다. (시간: -10, 체력: -5)\n")
    elif pos == '청량리':
        print("0. 집으로 간다. (시간: 0, 체력: 0)")
        print("1. 1호선을 이용해 신도림으로 간다. (시간: -40, 체력: -30)\n")
    elif pos == '김포공항':
        print("0. 집으로 간다. (시간: 0, 체력: 0)")
        print("1. 5호선을 이용해 영등포구청으로 간다. (시간: -20, 체력: -10)")
        print("2. 9호선을 이용해 당산으로 간다. (시간: -30, 체력: -20)\n")
    elif pos == '당산':
        print("0. 집으로 간다. (시간: 0, 체력: 0)")
        print("1. 2호선을 이용해 서울대입구로 간다. (시간: -20, 체력: -10)\n")
    elif pos == '용산':
        print("0. 집으로 간다. (시간: 0, 체력: 0)")
        print("1. 1호선을 이용해 신도림으로 간다. (시간: -10, 체력: -5)\n")
    elif pos == '동역사':
        print("*** 4호선이 고장났다.. !! ***")
        print("0. 집으로 간다. (시간: 0, 체력: 0)")
        print("1. 4호선을 이용해 사당으로 간다. (시간: -25, 체력: -15)")
        print("2. 2호선을 이용해 서울대입구로 간다. (시간: -40, 체력: -30)\n")
    elif pos == '왕십리':
        print("0. 집으로 간다. (시간: 0, 체력: 0)")
        print("1. 2호선을 이용해 서울대입구로 간다. (시간: -45, 체력: -30)")
        print("2. 5호선을 이용해 영등포구청으로 간다. (시간: -30, 체력: -20)")
        print("3. 5호선을 이용해 동역사로 간다. (시간: -10, 체력: -5)")
        print("4. 분당선을 이용해 선릉으로 향해본다. (시간: -15, 체력: -10)\n")
    elif pos == '까치산':
        print("0. 집으로 간다. (시간: 0, 체력: 0)")
        print("1. 2호선을 이용해 신도림으로 간다. (시간: -10, 체력: -5)")
        print("2. 5호선을 이용해 영등포구청으로 간다. (시간: -10, 체력: -5)\n")
    elif pos == '영등포구청':
        print("0. 집으로 간다. (시간: 0, 체력: 0)")
        print("1. 2호선을 이용해 서울대입구로 간다. (시간: -20, 체력: -10)\n")
    elif pos == '노량진':
        print("0. 집으로 간다. (시간: 0, 체력: 0)")
        print("1. 1호선을 이용해 신도림으로 간다. (시간: -10, 체력: -5)")
        print("2. 6515번 버스를 타고 서울대입구로 간다. (시간: -10, 체력: -5)\n")
    elif pos == '약수':
        print("0. 집으로 간다. (시간: 0, 체력: 0)")
        print("1. 3호선을 이용해 교대로 간다. (시간: -15, 체력: -10)\n")
    elif pos == '뚝섬':
        print("0. 집으로 간다. (시간: 0, 체력: 0)")
        print("1. 2호선을 이용해 서울대입구로 간다. (시간: -40, 체력: -30)")
        print("2. 날씨도 좋은 김에 뚝섬유원지로 가 청춘을 즐긴다. (시간: -15, 체력: -20)\n")
    elif pos == '계양':
        print("0. 집으로 간다. (시간: 0, 체력: 0)")
        print("1. 인천 1호선을 이용해 부평구청으로 간다. (시간: -15, 체력: -10)")
        print("2. 공항철도를 이용해 김포공항으로 간다. (시간: -10, 체력: -5)\n")
    elif pos == '신도림':
        print("0. 집으로 간다. (시간: 0, 체력: 0)")
        print("1. 2호선을 이용해 서울대입구로 간다. (시간: -15, 체력: -10)\n")
    elif pos == '숭실대입구':
        print("0. 집으로 간다. (시간: 0, 체력: 0)")
        print("1. 7호선을 이용해 이수역으로 간다. (시간: -10, 체력: -5)")
        print("2. 5511번 버스를 타고 서울대입구로 간다. (시간: -5, 체력: -5)\n")
    elif pos == '고속터미널':
        print("0. 집으로 간다. (시간: 0, 체력: 0)")
        print("1. 3호선을 이용해 교대로 간다. (시간: -5, 체력: -5)\n")
    elif pos == '건대입구':
        print("0. 집으로 간다. (시간: 0, 체력: 0)")
        print("1. 2호선을 이용해 서울대입구로 간다. (시간: -35, 체력: -25)\n")
    elif pos == '부평구청':
        print("0. 집으로 간다. (시간: 0, 체력: 0)")
        print("1. 7호선을 이용해 대림역으로 간다. (시간: -30, 체력: -20)\n")
    elif pos == '대림':
        print("0. 집으로 간다. (시간: 0, 체력: 0)")
        print("1. 2호선을 이용해 서울대입구로 간다. (시간: -15, 체력: -5)\n")
    elif pos == '교대':
        print("0. 집으로 간다. (시간: 0, 체력: 0)")
        print("1. 2호선을 이용해 서울대입구로 간다. (시간: -10, 체력: -5)\n")
    elif pos == '잠실':
        print("0. 집으로 간다. (시간: 0, 체력: 0)")
        print("1. 2호선을 이용해 서울대입구로 간다. (시간: -30, 체력: -20)\n")

    ans = answer(pos)
    print("")

    if exception_check(pos, ans[1]) == True:
        temp = exception(pos)
        me.time += temp[0]
        me.energy += temp[1]
    else:
        me.result(*ans)

    return ans
    

def answer(pos):
    answer = int(input('your answer? '))
    return pos, answer

def exception_check(pos, ans):
    if (pos == '합정' and ans == 1) or (pos == '신촌' and ans == 1) or (pos == '신도림' and ans == 1) or (pos == '용산' and ans == 1) or (pos == '왕십리' and ans == 3) or (pos == '까치산' and ans == 1) or (pos == '숭실대입구' and ans == 1):
        return True
    else:
        return False

def exception(pos):
    if pos == '합정':
        print("거리의 연주자들이 지옥철에서 탈출하려 합니다.. 당신은 지옥철에서 밀려나 탑승하지 못했습니다..")
        print("다음 열차를 타야합니다.")
        print("(시간: -5, 체력: -10)")
        return (-30, -25)
    elif pos == '신촌':
        print("거리의 연주자들이 지옥철에서 탈출하려 합니다.. 당신은 지옥철에서 밀려나 탑승하지 못했습니다..")
        print("다음 열차를 타야합니다.")
        print("(시간: -5, 체력: -10)")
        return (-35, -30)
    elif pos == '용산':
        print("팔도의 군인들이 모두 용산으로 모여들었습니다.")
        print("군 시절이 떠올라 차마 그들을 밀치지 못했네요. 다음 열차를 기다립니다.")
        print("(시간: -5, 체력: -10)")
        return (-15, -15)
    elif pos == '신도림':
        print("계단을 내려가던 중 발을 헛디딥니다. 상당히 아프지만 쪽팔리니까 빨리 가야죠.")
        print("하지만 속도가 나지 않습니다. 아아.. 방금 또 하나 놓쳤네요. 무릎이 더 아파옵니다.")
        print("(시간: -5, 체력: -20)")
        return (-20, -30)
    elif pos == '왕십리':
        print("4호선도 말썽이라더니, 분당선도 말썽이군요.")
        print("어쩔 수 없이 2호선을 이용해 서울대입구로 갑니다.")
        return (-45, -30)
    elif pos == '까치산':
        print("외선순환은 너무 늦는군요.. 폰으로 5호선을 확인해보니 전력으로 뛰면 잡을 수 있을지도..?")
        print("학창시절 계주 때를 생각하며 뛰어보지만, 세월엔 장사가 없군요..")
        print("숨을 헐떡이며 겨우겨우 5호선 열차를 잡습니다.")
        print("(체력: -10)")
        return (-10, -15)
    elif pos == '숭실대입구':
        print("역시 7호선, 아주 핫하군요. 출근길 7호선은 피하는게 상책이라는걸 새삼 느낍니다.")
        print("또 한 번 5511과 친해질 기회군요!")
        print("(시간: -5, 체력: -5)")
        return (-10, -10)

def commutegame(a, b):
    print("\n당신의 위치는 {0}입니다.".format(commute[a][b]))
    print("현재 남은 시간은 {0}이며, 체력은 {1} 남았습니다.\n".format(me.time, me.energy))

    while 1:
        qwer = input('명령어를 입력하세요.\n계속한다 : c, 맵을 본다 : m\n')
        print("")

        if qwer == 'c':
            dest = question(commute[a][b])
            if dest[1] == 0:
                print("오오 이불밖은 위험해~ 집에 가서 귤이나 까자 예~")
                print("Game Over")
                break
            me.position = destination[dest[0]][dest[1]]
            temp = me.pos()
            a = temp[0]
            b = temp[1]

            print("당신의 위치는 {0}입니다.".format(commute[a][b]))
            print("현재 남은 시간은 {0}이며, 체력은 {1} 남았습니다.\n".format(me.time, me.energy))

            if me.pos() == (4, 2):
                print("서울대 입구에 도착하였습니다..!!")
                print("5511번 버스에 몸을 욱여 넣고 관악의 향기를 맡아봅니다.")
                print("도착!!")
                print("오늘 당신의 출근길은..??")
                print("남은 체력: {0}, 남은 시간(분): {1}".format(me.energy, me.time))
                if me.time>=20:
                    print("시간이 남아도네요~ 부지런한 당신은 『Black Cow』!!")
                elif 10<=me.time<20:
                    print("모두에게 좋은 인상을 심어줄 수 있는 시간이네요!! 오늘 당신은 『히터틀기 당번』!!")
                elif 5<=me.time<10:
                    print("프로그래밍을 하고자 하는 자세가 되어있군요!! 당신은 『인간 알람시계』!!")
                elif 0<=me.time<5:
                    print("아슬아슬하지만 오늘도 제시간에 오셨군요!! 오늘 당신은 『버저비터 장인』!!")
                else:
                    print("회장님이 실망하는 표정입니다. 눈을 마주치지 마세요. 오늘 당신은 『프로눈치러』!!")
                break
            elif me.energy<=0:
                print("당신의 체력이 바닥났습니다. 집에나 가야죠 ㅠㅠ")
                print("Game Over")
                break
        elif qwer == 'm':
            for i in range(len(commute)):
                for j in range(len(commute[i])):
                    if i==me.position[0] and j==me.position[1]:
                        print('★★나★★\t ', end='')
                    elif commute[i][j] == 'None':
                        print('■■■\t\t ', end='')
                    elif len(commute[i][j])>=4:
                        print('{0}\t '.format(commute[i][j]), end='')
                    else:
                        print('{0}\t\t '.format(commute[i][j]), end='')
                print("")
    
for i in range(len(commute)):
    for j in range(len(commute[i])):
        if commute[i][j] == 'None':
            print('■■■\t\t ', end='')
        elif len(commute[i][j])>=4:
            print('{0}\t '.format(commute[i][j]), end='')
        else:
            print('{0}\t\t '.format(commute[i][j]), end='')
    print("")

import random

from introduction import name

a = random.randint(0, 4)
b = random.randint(0, 4)

me = Gamer(name, a, b)

home = commute[a][b]
print("\n당신의 위치는 {0}입니다.".format(commute[a][b]))
print("현재 남은 시간은 {0}이며, 체력은 {1} 남았습니다.\n".format(me.time, me.energy))

while 1:
    qwer = input('명령어를 입력하세요.\n계속한다 : c, 맵을 본다 : m\n')
    print("")

    if qwer == 'c':
        dest = question(commute[a][b])
        if dest[1] == 0:
            print("오오 이불밖은 위험해~ 집에 가서 귤이나 까자 예~")
            print("Game Over")
            print("---------------------------------------------------------------\n\n")
            break
        me.position = destination[dest[0]][dest[1]]
        temp = me.pos()
        a = temp[0]
        b = temp[1]

        print("당신의 위치는 {0}입니다.".format(commute[a][b]))
        print("현재 남은 시간은 {0}이며, 체력은 {1} 남았습니다.\n".format(me.time, me.energy))

        if me.pos() == (4, 2):
            print("서울대 입구에 도착하였습니다..!!")
            print("5511번 버스에 몸을 욱여 넣고 관악의 향기를 맡아봅니다.")
            print("도착!!")
            print("오늘 당신의 출근길은..??")
            print("")
            print("남은 체력: {0}, 남은 시간(분): {1}".format(me.energy, me.time))
            if me.time>=20:
                print("시간이 남아도네요~ 부지런한 당신은 『Black Cow』!!")
            elif 10<=me.time<20:
                print("모두에게 좋은 인상을 심어줄 수 있는 시간이네요!! 오늘 당신은 『히터틀기 당번』!!")
            elif 5<=me.time<10:
                print("프로그래밍을 하고자 하는 자세가 되어있군요!! 당신은 『인간 알람시계』!!")
            elif 0<=me.time<5:
                print("아슬아슬하지만 오늘도 제시간에 오셨군요!! 오늘 당신은 『버저비터 장인』!!")
            else:
                print("회장님이 실망하는 표정입니다. 눈을 마주치지 마세요. 오늘 당신은 『프로눈치러』!!")
            print("---------------------------------------------------------------\n\n")
            break
        elif me.energy<=0:
            print("당신의 체력이 바닥났습니다. 집에나 가야죠 ㅠㅠ")
            print("Game Over")
            print("---------------------------------------------------------------\n\n")
            break
    elif qwer == 'm':
        for i in range(len(commute)):
            for j in range(len(commute[i])):
                if i==me.position[0] and j==me.position[1]:
                    print('★★나★★\t ', end='')
                elif commute[i][j] == 'None':
                    print('■■■\t\t ', end='')
                elif len(commute[i][j])>=4:
                    print('{0}\t '.format(commute[i][j]), end='')
                else:
                    print('{0}\t\t '.format(commute[i][j]), end='')
            print("")
