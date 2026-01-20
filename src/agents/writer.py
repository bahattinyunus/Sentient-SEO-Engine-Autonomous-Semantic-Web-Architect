import logging
import os
from jinja2 import Environment, FileSystemLoader

logger = logging.getLogger("Sentient-SEO.Agents")

class ContentAgent:
    """
    SEO uyumlu içerik üretme konusunda uzmanlaşmış Yapay Zeka Yazı Ajanı.
    """
    def __init__(self, niche: str):
        self.niche = niche
        self.env = Environment(loader=FileSystemLoader('data/templates'))
        self.template = self.env.get_template('article_template.jinja2')
        logger.info(f"Yazı Ajanı uzmanlık alanı için kalibre edildi: {niche}")

    def generate_content(self, data: dict) -> str:
        """
        LLM (yapay zeka) ve Jinja2 şablonlarını kullanarak içerik üretir.
        """
        logger.debug(f"İçerik üretiliyor: {data.get('keyword')}")
        
        # Gerçek uygulamada, OpenAI API çağrısı burada yapılır.
        rendered_prompt = self.template.render(
            topic_expert=self.niche,
            target_audience="Profesyonel Uygulayıcılar",
            tone="Stratejik ve Analitik",
            keyword=data.get('keyword'),
            data_points=data.get('data_points', 'N/A')
        )
        
        return rendered_prompt # Şimdilik simülasyon çıktısı döndürülüyor
