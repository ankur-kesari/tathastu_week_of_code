player1=int(input("Enter score of first player on 60 ball:"))
player2=int(input("Enter score of second player on 60 ball:"))
player3=int(input("Enter score of third player on 60 ball:"))
strike_rate1=(player1*100)/60
strike_rate2=(player2*100)/60
strike_rate3=(player3*100)/60
print("strike_rate1 of player1:",strike_rate1)
print("strike_rate2 of player2:",strike_rate2)
print("strike_rate3 of player3:",strike_rate3)
print("player1 score after more 60 ball:",player1*2)
print("player2 score after more 60 ball:",player2*2)
print("player3 score after more 60 ball:",player3*2)
print("maximum number of six player1 hit:",player1//6)
print("maximum number of six player2 hit:",player2//6)
print("maximum number of six player3 hit:",player3//6)