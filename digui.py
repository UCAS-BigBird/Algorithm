def look_for_key(main_box):
    pile=main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box=pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print("find the key!")

def look_for_key(box):
    for item in box:
        if item.is_a_box():
           look_for_key(item)
        elif item.is_a_key():
            print("found the key")

#上方的两个程序我认为都存在一个问题   item 除非默认是一个盒子套多个盒子

