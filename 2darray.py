team = [["佐藤","鈴木","田中"],["岸田","有森","峯川"],["武田","武藤","神田"]]
print(team)
print("チーム数は" + str(len(team)) + "チームです。")
print()

print("*** 追加 ***")
team.append(["芥川","太宰","直木"])
team[0].append("田沢")
print(team)
print("チーム数は" + str(len(team)) + "チームです。")
print()

print("*** 変更 ***")
team[0][2] = "佐川"
print(team)
print("チーム数は" + str(len(team)) + "チームです。")
print()

print("*** 削除 ***")
team.pop(3)
team[2].pop(1)
print(team)
print("チーム数は" + str(len(team)) + "チームです。")
