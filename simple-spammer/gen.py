import random

"""
beacon = ['Send Nude to Lâm Pls ',
          'Test wifi',
          'Brother hood wifi',
          'Gammer wifi',
          'Nonstop',
          'Vina HOuse ',
          'Hack this',
          'ưhats up',
          'nibba',
          'sendNude',
          'hi im gay',
          'Địt mẹ wifi',
          'Inbox Lâm for nudes',
          'Đổi wifi đeeee',
          'Trường ơi nâng cấp wifi pls ',
          'Wifi như lollll',
          '']
"""
beacon  =['Chủ nhật',
          'Vui vẻ',
          'Hoq quạo',
          'Nắng',
          'Mưa',          
          'HOàng thượng',
          'và Con sen ngu ngục',
          'Bánh mì chấm sữa',
          'Bắp xào bơ']
tho = """Dữ dội và dịu êm
Ồn ào và lặng lẽ
Sông không hiểu nổi mình
Sóng tìm ra tận bể

Ôi con sóng ngày xưa
Và ngày sau vẫn thế
Nỗi khát vọng tình yêu
Bồi hồi trong ngực trẻ

Trước muôn trùng sóng bể
Em nghĩ về anh, em
Em nghĩ về biển lớn
Từ nơi nào sóng lên?

Sóng bắt đầu từ gió
Gió bắt đầu từ đâu?
Em cũng không biết nữa
Khi nào ta yêu nhau

Con sóng dưới lòng sâu
Con sóng trên mặt nước
Ôi con sóng nhớ bờ
Ngày đêm không ngủ được
Lòng em nhớ đến anh
Cả trong mơ còn thức

Dẫu xuôi về phương bắc
Dẫu ngược về phương nam
Nơi nào em cũng nghĩ
Hướng về anh - một phương

Ở ngoài kia đại dương
Trăm nghìn con sóng đó
Con nào chẳng tới bờ
Dù muôn vời cách trở

Cuộc đời tuy dài thế
Năm tháng vẫn đi qua
Như biển kia dẫu rộng
Mây vẫn bay về xa

Làm sao được tan ra
Thành trăm con sóng nhỏ
Giữa biển lớn tình yêu
Để ngàn năm còn vỗ
"""

names = []
alpha = "abcklmJKLMNOPQRSnostuvwxyzAB~!@#$defghi%^&*()CDEFGHI12345TUpqrVXYZ67890`_+-=[]{};',./<>?"
alphasize = len(alpha)
def ranStr(size = 5):
    s = ''
    for i in range(size):
        s+= alpha[int((random.random()*10000)%alphasize)]
    return s
for i in range(300):
    names.append(ranStr())
for name in names:
#    for i in range(10):
        print('"{}\\n"'.format(name))

#form = list(tho.split('\n'))

#for i in range(32):
#    print('"{}\\n"'.format(i))
    
