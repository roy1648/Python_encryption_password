	import base64
	import getpass
	# 加密 
	def enctry(s):
	    k = 'Z&sg6nu7A79tP#g#a6Q@&1UejtVo^&ys*SH^sOtTW*!WiUGmS19L#j%2daBBFs!IlvS*!9u3Ht@qKVum'
	    encry_str = ""
	    for i,j in zip(s,k): # i為字符，j為秘鑰字符
	        temp = str(ord(i)+ord(j))+'_' # 加密字符 = 字符的Unicode碼 + 秘鑰的Unicode碼
	        encry_str = encry_str + temp
	    s1 = base64.b64encode(encry_str.encode("utf-8"))
	    return s1
	# 解密
	
	def dectry(s2):
	    p = base64.b64decode(s2).decode("utf-8")
	    k = 'Z&sg6nu7A79tP#g#a6Q@&1UejtVo^&ys*SH^sOtTW*!WiUGmS19L#j%2daBBFs!IlvS*!9u3Ht@qKVum'
	    dec_str = ""
	    for i,j in zip(p.split("_")[:-1],k): # i 為加密字符，j為秘鑰字符
	        temp = chr(int(i) - ord(j)) # 解密字符 = (加密Unicode碼字符 - 秘鑰字符的Unicode碼)的單字節字符
	        dec_str = dec_str+temp
	    return dec_str
	
	def ask():
	    ans = input("請選擇 1.加密 2.解密(輸入數字)：")
	    if ans == "1":
	        data = input("請輸入要加密密碼：")
	        enc_str = enctry(data)
	        dec_str = dectry(enc_str)
	        print("原始數據為：",data)
	        print("加密數據為：",enc_str)
	        print("檢查解密數據：",dec_str)
	    elif ans == "2":
	        data = input("請輸入要解密密碼：")
	        dec_str = dectry(data)
	        print("加密數據為：",data)
	        print("解密數據為：",dec_str)
	        
	if getpass.getpass("請輸入中文姓名(全小寫)") == "test":
	    if getpass.getpass("請輸入身份證字號") == "test":
	        if getpass.getpass("請輸入以前狗狗的名字(全小寫)") == "test":
	            while 1:
	                ask()
	                if input("是否再次輸入？(Y/N)") == "N":
	                    break
	        else:
	            print("輸入錯誤")
	    else:
	        print("輸入錯誤")
	else:
	    print("輸入錯誤")
	input("輸入任意鍵已結束")