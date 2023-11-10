import os
import cv2

caminho_da_pasta_principal = input("Digite o caminho da pasta que deseja analisar: ")

def calcular_tempo_videos_em_pasta(caminho_da_pasta):
    tempo_total = 0
    extensoes_de_video = [".mp4", ".mov", ".avi"]

    for pasta_raiz, _, arquivos in os.walk(caminho_da_pasta):
        tempo_pasta = 0

        for nome_arquivo in arquivos:
            nome, extensao = os.path.splitext(nome_arquivo)
            if extensao in extensoes_de_video:
                caminho_completo = os.path.join(pasta_raiz, nome_arquivo)
                try:
                    cap = cv2.VideoCapture(caminho_completo)
                    fps = cap.get(cv2.CAP_PROP_FPS)
                    frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
                    tempo_pasta += frames / fps
                    tempo_total += frames / fps
                    cap.release()
                except Exception as e:
                    print(f"Erro ao processar {nome_arquivo}: {e}")

        horas = int(tempo_pasta / 3600)
        minutos = int((tempo_pasta % 3600) / 60)
        print(f"Pasta: {pasta_raiz} - Tempo total: {horas} horas e {minutos} minutos")

    horas_total = int(tempo_total / 3600)
    minutos_total = int((tempo_total % 3600) / 60)
    print(f"Tempo total de vídeos em todas as pastas: {horas_total} horas e {minutos_total} minutos")

calcular_tempo_videos_em_pasta(caminho_da_pasta_principal)


input("Pressione Enter para sair...")