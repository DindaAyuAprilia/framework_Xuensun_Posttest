2209106095
Dinda Ayu Aprilia

# Tampilan Website
## Detail Buku
![image](https://github.com/user-attachments/assets/c696437a-35b6-48be-b798-57fc74269ca4)
![image](https://github.com/user-attachments/assets/85133ab4-a668-4c7f-8fc8-da180c74da6b)


## Landingpage
![image](https://github.com/user-attachments/assets/26877327-5207-438e-a7a7-99169cc755f7)
![image](https://github.com/user-attachments/assets/662417d2-a595-4e22-a2ed-0a58bcf37a94)

## Daftar Buku
![image](https://github.com/user-attachments/assets/74f0e956-ca0b-44d1-81ef-7f7aa8d8efcc)







# Database

## admin
![image](https://github.com/user-attachments/assets/cfa88603-e45a-4010-8c35-94fd8684c25f)

## akun
![image](https://github.com/user-attachments/assets/2618676b-2850-4b3c-9b66-46e82bd20cfe)

## user
![image](https://github.com/user-attachments/assets/4a3b90ae-c00f-4c4b-9c43-cffc018b13b4)

## penulis
![image](https://github.com/user-attachments/assets/f4b24b2a-9475-4986-b713-c885ed553e60)

## buku
![image](https://github.com/user-attachments/assets/dea66597-36ee-47f3-9ad1-efb383553924)

## many to many antara buku dan kategori
![image](https://github.com/user-attachments/assets/f403bea8-de1a-4d12-b99f-77c4b28efece)

## kategori
![image](https://github.com/user-attachments/assets/87e586b7-dd46-46ca-93bf-19e49178c338)

## keranjang
![image](https://github.com/user-attachments/assets/974c6a91-90be-4f9e-956d-fdbcd2cba334)

# Desain
![image](https://github.com/user-attachments/assets/cee00e38-34c0-40e5-8bc8-b687834572bb)







# Admin Django

## Admin
![image](https://github.com/user-attachments/assets/c046ec97-b075-4161-b1f0-898b8c433687)
![image](https://github.com/user-attachments/assets/7510743e-8fd2-4ca1-a6d2-91d2ffd67cd7)

## User
![image](https://github.com/user-attachments/assets/6c7e1e43-9fd3-48d9-bb15-e43306f349fe)
![image](https://github.com/user-attachments/assets/87aee17e-fd2b-48d5-8daf-bf3632fc9020)

## Akun
![image](https://github.com/user-attachments/assets/4eb2e68a-cd00-4a86-aba2-e38921f87ae7)
![image](https://github.com/user-attachments/assets/fc0a2b22-83fc-4063-83e9-4b56734d2e37)

## Penulis
![image](https://github.com/user-attachments/assets/401a3f2c-4fce-4c67-9f7a-abde8e4bc9f3)
![image](https://github.com/user-attachments/assets/efe3061c-70ac-4430-865c-b6818e1307e0)

## Buku
![image](https://github.com/user-attachments/assets/24b46b7e-bfcc-432d-b4a0-6852f41263b9)
![image](https://github.com/user-attachments/assets/57d36d5d-17d1-4094-b79c-49e1e6adeac6)

## Kategori
![image](https://github.com/user-attachments/assets/ba8ff23b-0106-4f41-bdb3-1c84511107b8)
![image](https://github.com/user-attachments/assets/04651d7e-7730-4cd4-8101-4fa899f17530)









# Penjelasan

## aksi/function custom

def save_model(self, request, obj, form, change):
       
        super().save_model(request, obj, form, change)

        akun, created = Akun.objects.get_or_create(
            email=obj.email,
            defaults={
                'password': make_password('123'),
                'role': Akun.ADMIN,
            }
        )

        if not created:
            # Jika Akun sudah ada, perbarui peran dan password jika diperlukan
            akun.role = Akun.ADMIN
            akun.password = make_password('123') 

Ada pada bagian admin dan user dimana setiap membuat admin atau user akan otomatis membuat akun sesuai rolenya dan membuat password otomatis(untuk sementara).





## static assets
Foldernya di dalam aplikasi xue, lalu saya gunakan untuk latar belakang web dan untuk menambahkan foto cover buku

### cutom.css
.body-custom {
    background-image: url('../images/bg2.jpg'); /* Gambar background */
    background-size: auto; /* Gambar sesuai ukuran aslinya */
    background-repeat: repeat; /* Gambar diulang secara horizontal dan vertikal */
    background-attachment: scroll; /* Background ikut tergulir saat scroll */
    background-position: top left; /* Menempatkan gambar di pojok kiri atas */
}

### detail_buku
<div class="card mb-3">
  <div class="text-center">
    <img src="{% static 'images/harry_potter1.jpg' %}" class="card-img-top img-fluid" alt="Harry Potter and the Philosopher's Stone" style="max-width: 50%;">
  </div>

### daftar buku
<div class="card-group">
    <div class="card">
        <img src="{% static 'images/harry_potter1.jpg' %}" class="card-img-top" alt="Harry Potter and the Philosopher's Stone">
        <div class="card-body">

### landingpage
<div class="card" style="width: 18rem;">
  <img src="{% static 'images/harry_potter1.jpg' %}" class="card-img-top" alt="Harry Potter and the Philosopher's Stone">
  <div class="card-body">
    <h5 class="card-title">Harry Potter and the Philosopher's Stone</h5>
    <p class="card-text">Harry Potter and the Philosopher's Stone adalah novel fantasi karangan penulis Inggris J. K. Rowling yang merupakan novel pertama dalam seri Harry Potter dan novel debut Rowling. </p>
    <p class="card-text"><strong>Harga:</strong> Rp150.000</p>
    <a href="{% url 'detail_buku' %}" class="btn btn-custom">Selengkapnya..</a>
  </div>
</div>
