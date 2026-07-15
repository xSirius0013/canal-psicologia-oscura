import os
import requests
import json

def buscar_videos_virales():
    print("🕵️‍♂️ Agente 1: Iniciando búsqueda oficial en YouTube...")
    
    api_key = os.environ.get("YOUTUBE_API_KEY")
    
    if not api_key:
        print("❌ Error: No se encontró la YOUTUBE_API_KEY en los Secrets.")
        return

    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&order=viewCount&q=psicologia+oscura&maxResults=5&key={api_key}"
    
    try:
        respuesta = requests.get(url)
        datos = respuesta.json()
        
        if 'error' in datos:
            print(f"❌ Error de YouTube: {datos['error']['message']}")
            return
            
        print("\n📊 === TOP 5 VIDEOS VIRALES ENCONTRADOS ===\n")
        
        for i, item in enumerate(datos.get('items', []), 1):
            titulo = item['snippet']['title']
            video_id = item['id']['videoId']
            url_video = f"https://youtube.com/watch?v={video_id}"
            
            url_stats = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video_id}&key={api_key}"
            resp_stats = requests.get(url_stats)
            stats = resp_stats.json()['items'][0]['statistics']
            
            vistas = int(stats.get('viewCount', 0))
            
            print(f"{i}. Título: {titulo}")
            print(f"   Views: {vistas:,}")
            print(f"   URL: {url_video}")
            print("-" * 50)
            
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    buscar_videos_virales()

