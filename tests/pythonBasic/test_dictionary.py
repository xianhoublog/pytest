my_dict={
    "class":"animal",
    "name":"giraffe",
    "age": 10
}

def test_dict():
    assert my_dict=={
    "class":"animal",
    "name":"giraffe",
    "age": 10}
    assert my_dict["name"]=="giraffe"
    assert my_dict.get("name")=="giraffe"
    print(my_dict.values())

    # assert my_dict.values() ==(['animal', 'giraffe', 10])
    for x in my_dict:
        # print(x)
        print(my_dict[x])

    for x,y in my_dict.items():
        print(x,y)

    my_dict["name"]="elephant"
    print(my_dict)

    my_dict["color"]= "gray"
    print(my_dict)

    my_dict.pop("color")
    print(my_dict)

    my_dict.popitem()
    print(my_dict)

    del my_dict["class"]
    print(my_dict)