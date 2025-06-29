import qrcode
#taking upi_id input
upi_id=input("enter  your upi number")

# upi://pay?pa=upi=ID&pn=NAME&am=AMOUNT&cu=CURRENCY&tn=message
#Defination the payment url base on the UPI ID and the payment app
#You can modify  these urls based on the payment apps you want to support

phonepe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#creat  qr code for each payment app
phonepe_qr=qrcode.make(phonepe_url)
paytm_qr=qrcode.make(paytm_url)
google_pay_qr=qrcode.make(google_pay_url)
#save the qrcode image file
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")
#dispaly the qr code
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()




