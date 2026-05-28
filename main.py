from fastapi import FastAPI, HTTPException
from neo4j import GraphDatabase

app = FastAPI(
    title="Tugas Besar Neo4j",
    description="Backend API untuk Sistem Jaringan Sosial, Rekomendasi Produk, dan Shortest Path",
    version="1.0.0"
)

# --- KONFIGURASI KONEKSI NEO4J ---
# Ganti dengan data dari Neo4j Sandbox kalian
NEO4J_URI = "bolt://98.80.200.149"  
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "cover-reactors-eggs"    

# Inisialisasi Driver
try:
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    # Validasi koneksi awal
    driver.verify_connectivity()
    print("✅ Berhasil terhubung ke Neo4j Database!")
except Exception as e:
    print(f"❌ Gagal koneksi ke Neo4j: {e}")
    driver = None

# Event ketika aplikasi dimatikan (menutup koneksi database)
@app.on_event("shutdown")
def shutdown_db_client():
    if driver:
        driver.close()
        print("🔒 Koneksi Neo4j ditutup.")

# --- ENDPOINT UTAMA (CEK STATUS) ---
@app.get("/", tags=["Status"])
def read_root():
    if driver:
        return {"status": "Online", "message": "Backend FastAPI & Neo4j siap digunakan kelompok!"}
    return {"status": "Offline", "message": "Koneksi database bermasalah."}


# =====================================================================
# KODE DI BAWAH INI ADALAH TEMPAT UNTUK ZAHRA, KIYA, DAN AZIZAH CODING
# =====================================================================

# --- [TUGAS 1 - ZAHRA] ---
@app.get("/tugas1/status", tags=["Tugas 1: Jaringan Sosial"])
def tugas1_status():
    return {"pic": "Zahra", "status": "Ready untuk dicoding"}

# --- [TUGAS 2 - KIYA] ---
@app.get("/tugas2/status", tags=["Tugas 2: Rekomendasi Produk"])
def tugas2_status():
    return {"pic": "Kiya", "status": "Ready untuk dicoding"}

# --- [TUGAS 3 - AZIZAH] ---
@app.get("/tugas3/status", tags=["Tugas 3: Shortest Path"])
def tugas3_status():
    return {"pic": "Azizah", "status": "Ready untuk dicoding"}