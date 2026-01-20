import argparse
import sys
import logging
from src.core.engine import SEOEngine

# Log yapılandırması
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/system.log", encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("Sentient-SEO")

def main():
    parser = argparse.ArgumentParser(description="Sentient-SEO-Engine: Otonom Semantik Web Mimarı")
    
    parser.add_argument("--dataset", type=str, required=True, help="Giriş CSV/JSON dosyasının yolu")
    parser.add_argument("--niche", type=str, default="Genel Teknoloji", help="Yapay zeka personası için uzmanlık alanı")
    parser.add_argument("--count", type=int, default=10, help="Üretilecek sayfa sayısı")
    parser.add_argument("--dry-run", action="store_true", help="API çağırmadan sistemi test et")

    args = parser.parse_args()

    logger.info("Sentient-SEO-Engine başlatılıyor...")
    logger.info(f"Hedef Uzmanlık Alanı: {args.niche}")
    logger.info(f"İşlenen Veri Seti: {args.dataset}")

    try:
        engine = SEOEngine(args)
        engine.run()
    except Exception as e:
        logger.error(f"Kritik Sistem Hatası: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
