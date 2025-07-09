import json
import os
from typing import List, Dict
from getpass import getpass

usr = ["admin", "user", "guest", "teacher", "student"]
psw = ["admin123", "user123", "guest123", "teacher123", "student123"]
TODO_FILE = 'SideJob.json'

def login():
    username = input("Masukan username: ")
    password = getpass("Masukan password: ")
    
    if username in usr and password in psw:
        index = usr.index(username)
        if psw[index] == password:
            print(f"Login berhasil! Selamat datang, {username}.")
            return True
        else:
            print("Password yang anda masukan salah.")
            return False
    else:
        print("Username yang anda masukan tidak terdaftar.")
        return False
        exit()
        
def load_todos() -> list[dict]:
    try:
        if os.path.exists(TODO_FILE):
            with open(TODO_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []  
    except json.JSONDecodeError:
        print("Warning: File Corrupt Cokk")
        return []
    except Exception as e:
        print(f"Gagal Memuat Todos: {e}")
        return []
    
def save_todos(todos: List[Dict]) -> None:
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)
        
def show_todos(todos: List[Dict]) -> None:
    print("\n=== DAFTAR TUGAS ===")
    for idx, todo in enumerate(todos, 1):
        status = "✓" if todo["completed"] else " "
        print(f"{idx}. [{status}] {todo['task']}")
    print()

def add_todo(todos: List[Dict], task: str) -> None:
    todos.append({"task": task, "completed": False})
    save_todos(todos)
    print(f"Tugas '{task}' baru berhasil ditambahkan!")

def complete_todo(todos: List[Dict], index: int) -> None:
    if 1 <= index <= len(todos):
        todos[index-1]["completed"] = True
        save_todos(todos)
        print(f"Tugas '{todos[index-1]['task']}' ditandai selesai!")
    else:
        print("Nomor tugas tidak valid!")

def delete_todo(todos: List[Dict], index: int) -> None:
    if 1 <= index <= len(todos):
        removed = todos.pop(index-1)
        save_todos(todos)
        print(f"Tugas '{removed['task']}' dihapus!")
    else:
        print("Nomor tugas tidak valid!")

def main():
    todos = load_todos()
    
    while True:
        login()
        print("\n=== APLIKASI TO-DO LIST ===")
        show_todos(todos)
        print("Menu:")
        print("1. Tambahkan Tugas")
        print("2. Tandai Tugas Selesai")
        print("3. Hapus Tugas")
        print("4. Keluar")
        
        choice = input("Pilihan Anda (1-4): ")
        
        if choice == "1":
            task = input("Masukkan tugas baru: ")
            add_todo(todos, task)
        elif choice == "2":
            index = int(input("Nomor tugas yang selesai: "))
            complete_todo(todos, index)
        elif choice == "3":
            index = int(input("Nomor tugas yang dihapus: "))
            delete_todo(todos, index)
        elif choice == "4":
            print("Jangan Lupa Selesaikan Tugas Anda, Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid!")
            exit()

if __name__ == "__main__":
    main()