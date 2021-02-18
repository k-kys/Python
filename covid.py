answer = input("Đã ở nhà chưa? Bạn cần trả lời RỒI hoặc CHƯA").upper()
print(answer)
unexpt_answer = "CHƯA"
expt_answer = "RỒI"
while answer != expt_answer:
    print("VỀ NHÀ")
    answer = input("Về đến nhà chưa? ").upper()
    print(answer)
else:
    print ("TỐT, Ở YÊN ĐẤY")
