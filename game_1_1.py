try :
    class Game :
        def problem(level,password,pro) :
            print(f'레벨 {level}')
            p = '비번'
            while p != password :
                print(pro)
                p = input('비번: ')
                if p == password :
                    print('비번이 맞습니다.')
                else :
                    print('비번이 틀립니다.')
            input('성공')
    
    g = Game.problem
    l = int(input('레벨을 정해주세요.'))
    while True :
        match l :
            case 1 :
                g(1,'123456','123456')
            case 2 :
                g(2,'3212','*** ** * **')
            case 3 :
                g(3,'1510','I V X')
            case 4 :
                g(4,'579','123 + 456 =')
            case 5 :
                g(5,'22528','2048 * 11 =')
            case 6 :
                g(6,'6','현재 레벨')
            case 7 :
                g(7,'1310','一 三 十')
            case 8 :
                g(8,'205','가위 바위 보')
            case 9 :
                g(9,'10','OX 퀴즈\n2번째 문자')
            case 10 :
                g(10,'5','三 合 六 分 三 同')
            case 11 :
                g(11,'12112212','1 ←---→ 2\n←→←←→→←→')
            case 12 :
                g(12,'2048','2 ^ 11')
            case 13 :
                g(13,'5','부엉이와 오각별')
            case 14 :
                g(14,'7','눈의 개수\n부엉이 1마리, 별님과 달님, 눈 한쪽 그림')
            case 15 :
                g(15,'01','부엉이와 01010101010101...')
            case 16 :
                g(16,'13','부엉이와 방정식\nx + 7 = 2x - 6')
            case 17 :
                g(17,'','NO')
            case 18 :
                g(18,'6','4, ?, 8, 12, 20')
            case 19 :
                g(19,'1111','!!!!')
            case 20 :
                g(20,'0214','밸런타인데이의 날짜')
            case 21 :
                g(21,'202122','이전, 현재, 다음 레벨')
            case 22 :
                g(22,'1111111','비번: 1111111\n비번: 1111111\n비번: 1111111')
            case 23 :
                g(23,'6','(1 + 2 - 3 * 4 / 5) * 10 =')
            case 24 :
                g(24,'190000','세상에서 제일 쉬운 숫자')
            case 25 :
                g(25,'162534','1_2_3_ = ? = _6_5_4')
            case 26 :
                g(26,'113355','135351\n<<<')
            case 27 :
                g(27,'20220101','zozzolol')
            case 28 :
                g(28,'198','영어 첫글자\nONE')
            case 29 :
                g(29,'8','□에 들어갈 영어 첫글자\nON□')
            case 30 :
                g(30,'8','이전 레벨의 비번')
            case 31 :
                g(31,'52','초록 채소 길쭉')
            case 32 :
                g(32,'56088','123 * 456 =')
            case 33 :
                g(33,'50100500','L C D')
            case 34 :
                g(34,'0861','부엉이와 1980\n180˚')
            case 35 :
                g(35,'10','부엉이와 01010101010101...\n180˚')
            case 36 :
                g(36,'123456','처음 레벨의 비번')
            case 37 :
                g(37,'','無')
            case 38 :
                g(38,'3','w\n-90˚')
            case 39 :
                g(39,'303','wow\n-90˚')
            case 40 :
                g(40,'410','3 + 1 = 24\n6 + 3 = 39\n7 + 3 = ?')
            case 41 :
                g(41,'1576','() = 90\n!%&^ = ?')
            case 42 :
                g(42,'12','(***) * (**) * (*) * (**)')
            case 43 :
                g(43,'111119108','Aa1 = 659749\nowl = ?')
            case 44 :
                g(44,'359907','123 + 456 * 789 =')
            case 45 :
                g(45,'1232123','비빈: 1111111\n비번: 1232123\n버번: 1234321')
            case 46 :
                g(46,'4','획\n今')
            case 47 :
                g(47,'132','획\n一 三 十')
            case 48 :
                g(48,'052','승 ? ? ?\n패 가위 바위 보')
            case 49 :
                g(49,'654321','.다니입123456 은번비')
            case 50 :
                g(50,'699678','1234 * 567 =')
            case 51 :
                g(51,'','비번패드 OFF')
            case 52 :
                g(52,'86420','12345 = 87654\n13579 = ?')
            case 53 :
                g(53,'12','1O 2O 3X 4X 5X 6X')
            case 54 :
                g(54,'12310456','123 X 456 =')
            case 55 :
                g(55,'5','(현재 레벨) / 11 =')
            case 56 :
                g(56,'105','9, 13 레벨의 비번')
            case 57 :
                g(57,'6482','→←↑↓')
            case 58 :
                g(58,'314','π = □.□□...')
            case 59 :
                g(59,'456831','(123 + 456) * 789 =')
            case 60 :
                g(60,'7006652','1234 * 5678 =')
            case _ :
                input('끝')
                break
        l += 1
except :
    input('오류')