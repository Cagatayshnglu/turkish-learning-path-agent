import gradio as gr

def öneri_oluştur(konu, düzey, tarz):
    kaynaklar = {
        "Video": ["YouTube", "Khan Academy", "Akademiklink"],
        "Metin": ["WikiBooks", "Medium", "Veri Bilimi Türkiye"],
        "Etkileşimli": ["Kaggle Courses", "Codecademy"]
    }
    önerilen = kaynaklar.get(tarz, ["YouTube"])
    mesaj = f'''
Öğrenme Planı:
- Hedef Konu: {konu}
- Seviye: {düzey}
- Öğrenme Tarzı: {tarz}

Önerilen Kaynaklar:
- {önerilen[0]}
- {önerilen[1]}
- {önerilen[2]}

Tavsiye: Her gün 1 saatlik çalışma ile 4 hafta sonunda {konu} alanında sağlam bir temele sahip olabilirsin.
'''
    return mesaj

with gr.Blocks() as demo:
    gr.Markdown("## Kişiselleştirilmiş Eğitim Yolu Asistanı")
    konu = gr.Textbox(label="Hedef Konu", placeholder="Örn: Python ile Veri Analizi")
    düzey = gr.Radio(["Başlangıç", "Orta", "İleri"], label="Bilgi Seviyeniz")
    tarz = gr.Radio(["Video", "Metin", "Etkileşimli"], label="Tercih Ettiğiniz Öğrenme Tarzı")
    buton = gr.Button("Öğrenme Yolunu Oluştur")
    çıktı = gr.Textbox(label="Tavsiyeler")
    buton.click(fn=öneri_oluştur, inputs=[konu, düzey, tarz], outputs=çıktı)

demo.launch()
