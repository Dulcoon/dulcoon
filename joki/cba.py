class TreeNode:
    def _init_(self, sku, nama_barang, harga_satuan, jumlah_stok):
        self.sku = sku
        self.nama_barang = nama_barang
        self.harga_satuan = harga_satuan
        self.jumlah_stok = jumlah_stok
        self.left = None
        self.right = None


class Barang:
    def _init_(self):
        self.root = None

    def insert(self, sku, nama_barang, harga_satuan, jumlah_stok):
        if not self.root:
            self.root = TreeNode(self, sku, nama_barang, harga_satuan, jumlah_stok)
        else:
            self._insert_recursive(self.root, self, sku, nama_barang, harga_satuan, jumlah_stok)

    def _insert_recursive(self, temp, sku, nama_barang, harga_satuan, jumlah_stok):
        if sku == temp.sku:
            print("No. SKU already exists in the BST.")
            return
        elif sku < temp.sku:
            if temp.left:
                self._insert_recursive(temp.left, sku, nama_barang, harga_satuan, jumlah_stok)
            else:
                temp.left = TreeNode(sku, nama_barang, harga_satuan, jumlah_stok)
        else:
            if temp.right:
                self._insert_recursive(temp.right, sku, nama_barang, harga_satuan, jumlah_stok)
            else:
                temp.right = TreeNode(sku, nama_barang, harga_satuan, jumlah_stok)

    def restock(self, sku, jumlah_stok):
        if not self.root:
            print("SKU Tidak Terdaftar ! Harap Daftar SKU dahulu")
            return
        else:
            self._restock_recursive(self.root, sku, jumlah_stok)

    def _restock_recursive(self, temp, sku, jumlah_stok):
        if sku == temp.sku:
            temp.jumlah_stok += jumlah_stok
            print("Stok Barang Berhasil Diperbarui")
            return
        elif sku < temp.sku:
            if temp.left:
                self._restock_recursive(temp.left, sku, jumlah_stok)
            else:
                print("SKU Tidak Terdaftar ! Harap Daftar SKU dahulu")
                ask = input("Ingin Melakukan Transaksi Lagi (y/n) : ")
                if ask.lower() == "y":
                    self.restock()
        else:
            if temp.right:
                self._restock_recursive(temp.right, sku, jumlah_stok)
            else:
                print("SKU Tidak Terdaftar ! Harap Daftar SKU dahulu")
                ask = input("Ingin Melakukan Transaksi Lagi (y/n) : ")
                if ask.lower() == "y":
                    self.restock()

    def display(self):
        self._display_recursive(self.root)

    def _display_recursive(self, temp):
        if temp:
            self._display_recursive(temp.left)
            print("No. SKU:", temp.sku)
            print("Nama Barang:", temp.nama_barang)
            print("Harga Satuan:", temp.harga_satuan)
            print("Jumlah Stok:", temp.jumlah_stok)
            print()
            self._display_recursive(temp.right)


# Create an instance of BST
bst = Barang()

# Menu 1.1: Input Data Stok Barang
def input_stock():
    sku = input("Enter SKU: ")
    nama_barang = input("Enter Nama Barang: ")
    harga_satuan = float(input("Enter Harga Satuan: "))
    jumlah_stok = int(input("Enter Jumlah Stok: "))

    bst.insert(sku, nama_barang, harga_satuan, jumlah_stok)

# Menu 1.2: Restok Barang
def restock_item():
    sku = input("Enter SKU: ")
    jumlah_stok = int(input("Enter Jumlah Stok Baru: "))

    bst.restock(sku, jumlah_stok)

# Sample usage
while True:
    print("1.1 Input Data Stok Barang")
    print("1.2 Restok Barang")
    print("2.1 Input Data Transaksi Baru")
    print("2.2 Lihat Data Seluruh Transaksi Konsumen")
    print("2.3 Lihat Data Transaksi Berdasarkan Subtotal")
    choice = input("Enter your choice: ")

    if choice == "1.1":
        input_stock()
    elif choice == "1.2":
        restock_item()
    elif choice == "2.1":
        # Implement the logic for Menu 2.1 here
        pass
    elif choice == "2.2":
        # Implement the logic for Menu 2.2 here
        pass
    elif choice == "2.3":
        # Implement the logic for Menu 2.3 here
        pass
    else:
        print("Invalid choice. Please try again.")