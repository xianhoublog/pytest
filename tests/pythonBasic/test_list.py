# test list
my_list=["China", "Dalian","LiaoNing province"]

def test_my_list():
    assert my_list ==["China", "Dalian","LiaoNing province"]
    assert my_list[2] == "LiaoNing province"


    my_list[2] ="ji Lin province"
    assert my_list[2] == "ji Lin province"

    for val in my_list:
        print (val)

    my_list.append("boston")
    assert my_list ==["China", "Dalian","ji Lin province","boston"]


    my_list.pop()
    assert my_list == ["China", "Dalian", "ji Lin province"]

    my_list.reverse()
    assert my_list == ["ji Lin province", "Dalian","China" ]

    my_list.clear()
    assert my_list == []