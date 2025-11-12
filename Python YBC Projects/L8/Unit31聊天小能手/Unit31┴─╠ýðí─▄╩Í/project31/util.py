from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag

def pinyin_to_hanzi(pinyin, n):
    if n > 20:
        print("只能最多输出20个可能结果！请重新设置n哦。")
        return
    else:
        pinyinList = pinyin.split(" ")
        print("你输入的拼音是：", pinyinList)
        dagParams = DefaultDagParams()
        result = dag(dagParams, pinyinList, path_num=100)
        print("拼音转文字最可能的",n,"个结果：",sep="")

        print_list = []
        count = 1
        for item in result:
            if count > n:
                break
            else:
                socre = item.score
                res = item.path # 转换结果
                text = ""
                for i in res:
                    text = text + i
                if text not in print_list:
                    print_list.append(text)
                    print("结果:", text, " 分数:", socre)
                    count += 1


