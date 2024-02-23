# -*- coding: utf-8 -*-
"""Testing_self_cashier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vsfqdQLNgraSTzDlCR3SGIL58HCZEPio
"""

from self_cashier_3 import Transaction

# Membuat Obejek Transaction
user = Transaction()

# Testing method add_item
# Menambah item kedalam Transaction
user.add_item("Ayam Goreng", 2, 20000)
user.add_item("Pasta Gigi", 3 , 15000)

# Testing method check_order
# Memeriksa daftar transaksi
user.check_order()

# Testing method total_price
# Menampilkan harga akhir yang harus dibayar
user.total_price()

"""Test 2"""

# Testing method delete_item
# Menghapus baris item dalam Transaction
user.delete_item("Pasta Giggi")

# Testing method check_order
# Memeriksa daftar transaksi
user.check_order()

# Testing method total_price
# Menampilkan harga akhir yang harus dibayar
user.total_price()

# Testing method delete_item
# Menghapus baris item dalam Transaction
user.delete_item("Pasta Gigi")

# Testing method check_order
# Memeriksa daftar transaksi
user.check_order()

# Testing method total_price
# Menampilkan harga akhir yang harus dibayar
user.total_price()

"""Test 3"""

# Testing method reset_item
# Menghapus semua item dalam Transaction
user.reset_transaction()

# Testing method check_order
# Memeriksa daftar transaksi
user.check_order()

"""Test 4"""

# Testing method add_item
# Menambah item kedalam Transaction
user.add_item("Mainan Mobil", 1, 200000)
user.add_item("Mie Instant", 5, 3000)

# Testing method check_order
# Memeriksa daftar transaksi
user.check_order()

# Testing method total_price
# Menampilkan harga akhir yang harus dibayar
user.total_price()

"""Test 5"""

# Testing method delete_item
# Menghapus baris item dalam Transaction
user.update_item_name("Mie Instant", "Sabun")

# Testing method check_order
# Memeriksa daftar transaksi
user.check_order()

# Testing method total_price
# Menampilkan harga akhir yang harus dibayar
user.total_price()

"""Test 6"""

# Testing method delete_item
# Menghapus baris item dalam Transaction
user.update_item_qty("Mainan Mobil", 3)

# Testing method check_order
# Memeriksa daftar transaksi
user.check_order()

# Testing method total_price
# Menampilkan harga akhir yang harus dibayar
user.total_price()
