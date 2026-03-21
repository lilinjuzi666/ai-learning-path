def format_name(first_name:str,last_name:str)->str:
    """
    param first_name:第一个人的名字
    param last_name:第二个人的名字
    return:返回一个字符串，包含第一个人和第二个人的名字
    """
    return f"{first_name} {last_name}"

if __name__=="__main__":
    print(format_name("John","Smith"))


players=[{"name1":"join","name2":"smith"},
        {"name1":"jane","name2":"doe"},
        {"name1":"jim","name2":"smith"}]
if __name__=="__main__":
    for player in players:
        print(format_name(player["name1"],player["name2"]))    



