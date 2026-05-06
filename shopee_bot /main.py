import asyncio
import os
import random
from playwright.async_api import async_playwright
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

TARGET_URL = os.getenv("TARGET_URL")
SALE_TIME = os.getenv("SALE_TIME")

async def run_hybrid_sniper():
    async with async_playwright() as p:
        print("🚀 Menghubungkan ke Chrome di port 9222...")
        try:
            browser = await p.chromium.connect_over_cdp("http://localhost:9222")
            page = None
            for context in browser.contexts:
                for p_tab in context.pages:
                    title = await p_tab.title()
                    if "shopee" in title.lower() or "apple" in title.lower():
                        page = p_tab
                        break
            
            if not page:
                print("❌ ERROR: Tab Shopee/iPhone gak ketemu!")
                return

            await page.bring_to_front()
            # Bypass deteksi bot
            await page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

            print(f"🌐 Standby... Target: {SALE_TIME}")
            print("💡 Bot sekarang nyari tombol 'Beli Dengan Voucher' atau 'Beli Sekarang'")

            while True:
                now = datetime.now().strftime("%H:%M:%S")
                
                if now >= SALE_TIME:
                    print(f"🔥 JAM {now} - SIKAT!")
                    try:
                        # --- PERBAIKAN SELECTOR DI SINI ---
                        # Bot bakal nyari tombol yang mengandung kata 'Beli' (Bisa Beli Sekarang atau Beli Dengan Voucher)
                        beli_selector = "button:has-text('Beli')"
                        
                        # Tunggu sebentar banget & klik
                        btn = page.locator(beli_selector).first
                        await btn.click(timeout=3000)
                        print("✅ Klik Beli Berhasil!")
                        
                        # Jeda manusiawi dikit biar gak mental ke halaman error
                        await asyncio.sleep(random.uniform(0.3, 0.6))

                        # 2. Klik Checkout
                        checkout_selector = "button:has-text('Check Out'), button:has-text('Checkout')"
                        await page.wait_for_selector(checkout_selector, timeout=5000)
                        await page.click(checkout_selector)
                        print("✅ Masuk Checkout! SELESAIKAN DI HP SEKARANG!")
                        
                        # Bot berhenti di sini, sisanya jari lu di HP yang main!
                        break
                    except Exception as e:
                        print(f"⚠️ Gagal: {e}. Tombol mungkin belum muncul, coba refresh manual!")
                        break
                
                await asyncio.sleep(0.01) # Cek waktu super rapat
                
        except Exception as e:
            print(f"❌ Koneksi Gagal: {e}")

if __name__ == "__main__":
    asyncio.run(run_hybrid_sniper())
