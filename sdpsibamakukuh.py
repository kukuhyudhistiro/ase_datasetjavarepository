#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:27:11 2025

@author: kukuh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Pustaka Pre-processing dan Metrik
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import (
    classification_report, 
    confusion_matrix, 
    accuracy_score, 
    precision_score, 
    recall_score, 
    f1_score,
    roc_auc_score
)
# Pustaka untuk menangani imbalance data
from imblearn.over_sampling import SMOTE

# 2. Pustaka Model
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# Mengatur tampilan pandas
pd.set_option('display.max_columns', None)

# --- 1. PEMUATAN DATA ---
print("--- 1. Memuat Data ---")
try:
    # Dataset menggunakan semicolon (;) sebagai pemisah
    df = pd.read_csv('dataset_sibamacode1.csv', sep=';')
    print("Dataset berhasil dimuat.")
    print(f"Bentuk data: {df.shape}")
    print("\nContoh data (5 baris pertama):")
    print(df.head())
    print("\nInformasi Tipe Data:")
    df.info()
except FileNotFoundError:
    print("Error: File 'dataset_sibamacode1.csv' tidak ditemukan.")
    exit()

# --- 2. PRA-PEMROSESAN DATA ---
print("\n--- 2. Pra-pemrosesan Data ---")

# Menangani missing values (jika ada) dengan mengisi median
# Ini lebih aman daripada menghapus baris, terutama jika data sedikit
# Kita asumsikan semua kolom kecuali 'defects' adalah numerik
for col in df.columns:
    if df[col].dtype != 'object' and col != 'defects':
        median_val = df[col].median()
        df[col] = df[col].fillna(median_val)
print("Missing values telah ditangani (diisi dengan median).")

# Encoding kolom target 'defects' (True -> 1, False -> 0)
# astype(int) adalah cara cepat untuk konversi boolean ke int
if df['defects'].dtype == 'bool':
    df['defects'] = df['defects'].astype(int)
    print("Kolom target 'defects' telah di-encode (True->1, False->0).")
else:
    # Jika sudah 0/1 atau lainnya, pastikan itu numerik
    le = LabelEncoder()
    df['defects'] = le.fit_transform(df['defects'])
    print(f"Kolom target 'defects' telah di-encode menggunakan LabelEncoder. Kelas: {le.classes_}")


# Memeriksa distribusi kelas (seberapa tidak seimbang)
print("\nDistribusi Kelas Target (defects):")
class_distribution = df['defects'].value_counts(normalize=True) * 100
print(class_distribution)
if class_distribution.min() < 20:
    print("PERINGATAN: Dataset sangat tidak seimbang. SMOTE sangat direkomendasikan.")

# Pisahkan fitur (X) dan target (y)
X = df.drop('defects', axis=1)
y = df['defects']
# Simpan nama fitur untuk analisis nanti
feature_names = X.columns.tolist()

# --- 3. PEMBAGIAN DATA (TRAIN-TEST SPLIT) ---
print("\n--- 3. Membagi Data (70% Latih, 30% Uji) ---")
# Stratify=y sangat penting untuk memastikan proporsi kelas seimbang di train dan test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.3, 
    random_state=42, 
    stratify=y
)
print(f"Ukuran X_train: {X_train.shape}")
print(f"Ukuran X_test: {X_test.shape}")

# --- 4. PENANGANAN IMBALANCE (SMOTE) ---
print("\n--- 4. Menerapkan SMOTE pada Data Latih ---")
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

print(f"Ukuran y_train sebelum SMOTE: {y_train.value_counts().to_dict()}")
print(f"Ukuran y_train setelah SMOTE: {y_train_res.value_counts().to_dict()}")

# --- 5. PENSKALAAN FITUR (FEATURE SCALING) ---
print("\n--- 5. Menerapkan StandardScaler ---")
scaler = StandardScaler()
# Fit HANYA pada data latih (yang sudah di-SMOTE)
X_train_scaled = scaler.fit_transform(X_train_res)
# Transformasi data latih dan data uji
X_test_scaled = scaler.transform(X_test)

print("Penskalaan fitur selesai.")

# --- 6. PELATIHAN DAN EVALUASI MODEL ---
print("\n--- 6. Pelatihan dan Evaluasi Model ---")

# Fungsi helper untuk mencetak hasil
def print_evaluation_metrics(y_true, y_pred, model_name):
    print(f"--- Hasil untuk {model_name} ---")
    
    # 1. Confusion Matrix
    cm = confusion_matrix(y_true, y_pred)
    print("\nConfusion Matrix:")
    print(cm)
    try:
        # Visualisasi Confusion Matrix
        plt.figure(figsize=(6,4))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                    xticklabels=['Not Defect (0)', 'Defect (1)'], 
                    yticklabels=['Not Defect (0)', 'Defect (1)'])
        plt.title(f'Confusion Matrix - {model_name}')
        plt.ylabel('Aktual')
        plt.xlabel('Prediksi')
        plt.show()
    except Exception as e:
        print(f"Tidak dapat membuat plot heatmap: {e}")

    
    # 2. Classification Report
    print("\nClassification Report:")
    print(classification_report(y_true, y_pred, target_names=['Not Defect (0)', 'Defect (1)']))
    
    # 3. Metrik Utama
    print("Metrik Utama:")
    print(f"  Accuracy : {accuracy_score(y_true, y_pred):.4f}")
    print(f"  Recall (Defect): {recall_score(y_true, y_pred, pos_label=1):.4f}  <-- (Penting)")
    print(f"  Precision (Defect): {precision_score(y_true, y_pred, pos_label=1):.4f}")
    print(f"  F1-Score (Defect): {f1_score(y_true, y_pred, pos_label=1):.4f}   <-- (Penting)")
    print(f"  AUC-ROC  : {roc_auc_score(y_true, y_pred):.4f}")
    print("-" * (20 + len(model_name)))

# === Model 1: Regresi Logistik ===
print("\nMelatih Model Regresi Logistik...")
lr_model = LogisticRegression(random_state=42, max_iter=1000)
lr_model.fit(X_train_scaled, y_train_res)

# Prediksi pada data uji
y_pred_lr = lr_model.predict(X_test_scaled)
print_evaluation_metrics(y_test, y_pred_lr, "Regresi Logistik")

# === Model 2: Random Forest ===
print("\nMelatih Model Random Forest...")
# n_estimators=100 adalah default yang baik
rf_model = RandomForestClassifier(random_state=42, n_estimators=100)
# Catatan: RF tidak memerlukan penskalaan, tetapi tidak masalah jika digunakan
# Untuk konsistensi, kita gunakan data yang sudah di-scaled
rf_model.fit(X_train_scaled, y_train_res) 

# Prediksi pada data uji
y_pred_rf = rf_model.predict(X_test_scaled)
print_evaluation_metrics(y_test, y_pred_rf, "Random Forest")


# --- 7. ANALISIS FITUR PENTING (DARI RANDOM FOREST) ---
print("\n--- 7. Analisis Fitur Penting (Random Forest) ---")
importances = rf_model.feature_importances_
# Buat DataFrame untuk visualisasi
feature_importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importances
}).sort_values(by='Importance', ascending=False)

print("Fitur Paling Penting (Top 15):")
print(feature_importance_df.head(15))

# Visualisasi Fitur Penting
try:
    plt.figure(figsize=(10, 8))
    sns.barplot(
        x='Importance', 
        y='Feature', 
        data=feature_importance_df.head(15),
        palette='viridis'
    )
    plt.title('Top 15 Fitur Paling Penting (Random Forest)')
    plt.xlabel('Tingkat Kepentingan')
    plt.ylabel('Metrik Perangkat Lunak')
    plt.tight_layout()
    plt.show()
except Exception as e:
    print(f"Tidak dapat membuat plot feature importance: {e}")

print("\n--- Eksperimen Selesai ---")