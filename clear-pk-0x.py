
file_path = "pk.txt"
try:
    with open(file_path, "r") as file:
        lines = file.readlines()
    processed_lines = [line.strip()[2:] if line.strip().startswith("0x") else line.strip() for line in lines]
    with open(file_path, "w") as file:
        file.write("\n".join(processed_lines) + "\n")

    print("✅ Semua prefiks '0x' berhasil dihapus dari pk.txt.")
except FileNotFoundError:
    print("❌ File pk.txt tidak ditemukan.")
except Exception as e:
    print(f"❌ Terjadi kesalahan: {e}")
