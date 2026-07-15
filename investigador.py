import yt_dlp

def buscar_videos_virales():
    print("🕵️‍♂️ Agente 1: Iniciando búsqueda de videos de psicología oscura...")
    
    opciones = {
        'quiet': True,
        'no_warnings': True,
        'skip_download': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            # Buscamos los 5 videos más relevantes sobre psicología oscura en español
            resultados = ydl.extract_info("ytsearch5:psicología oscura", download=False)
            
            print("\n📊 === TOP 5 VIDEOS VIRALES ENCONTRADOS ===\n")
            
            for i, video in enumerate(resultados.get('entries', []), 1):
                print(f"{i}. Título: {video.get('title', 'Desconocido')}")
                print(f"   Views: {video.get('view_count', 0):,}")
                print(f"   URL: https://youtube.com/watch?v={video.get('id')}")
                print("-" * 50)
                
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Esta es la orden principal para que el agente despierte y trabaje
if __name__ == "__main__":
    buscar_videos_virales()
