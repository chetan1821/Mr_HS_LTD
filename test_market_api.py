import yfinance as yf
import json
from datetime import datetime
import time

def get_market_data():
    """Fetch latest NSE and BSE market data using yfinance"""
    try:
        market_data = {}
        
        # Fetch NSE Index data
        nse_symbols = {
            'NIFTY 50': '^NSEI',
            'NIFTY BANK': '^NSEBANK',
        }
        
        # Fetch BSE Index data
        bse_symbols = {
            'SENSEX': '^BSESN',
        }
        
        print("=" * 80)
        print("🔄 FETCHING NSE & BSE MARKET DATA (Using yfinance)...")
        print("=" * 80)
        
        # Get NSE data
        print("\n📊 NSE (National Stock Exchange) Indices:")
        print("-" * 80)
        for name, symbol in nse_symbols.items():
            try:
                ticker = yf.Ticker(symbol)
                data = ticker.history(period="1d")
                info = ticker.info
                
                if not data.empty:
                    current_price = data['Close'].iloc[-1]
                    previous_close = info.get('previousClose', 'N/A')
                    change = current_price - previous_close if previous_close != 'N/A' else 'N/A'
                    change_percent = (change / previous_close * 100) if previous_close != 'N/A' and change != 'N/A' else 'N/A'
                    
                    market_data[name] = {
                        'symbol': symbol,
                        'current': round(float(current_price), 2),
                        'change': round(float(change), 2) if change != 'N/A' else 'N/A',
                        'changePercent': round(float(change_percent), 2) if change_percent != 'N/A' else 'N/A',
                        'previous_close': round(float(previous_close), 2) if previous_close != 'N/A' else 'N/A',
                        'exchange': 'NSE'
                    }
                    
                    # Print formatted output
                    print(f"\n✓ {name} ({symbol})")
                    print(f"  Current Price:    ₹ {market_data[name]['current']}")
                    print(f"  Change:           {market_data[name]['change']}")
                    print(f"  Change %:         {market_data[name]['changePercent']}%")
                    print(f"  Previous Close:   ₹ {market_data[name]['previous_close']}")
                else:
                    print(f"✗ {name}: No data available")
                    
                time.sleep(1)  # Add delay to avoid rate limiting
            except Exception as e:
                print(f"✗ {name}: Error - {str(e)[:50]}")
        
        # Get BSE data
        print("\n" + "-" * 80)
        print("\n📊 BSE (Bombay Stock Exchange) Indices:")
        print("-" * 80)
        for name, symbol in bse_symbols.items():
            try:
                ticker = yf.Ticker(symbol)
                data = ticker.history(period="1d")
                info = ticker.info
                
                if not data.empty:
                    current_price = data['Close'].iloc[-1]
                    previous_close = info.get('previousClose', 'N/A')
                    change = current_price - previous_close if previous_close != 'N/A' else 'N/A'
                    change_percent = (change / previous_close * 100) if previous_close != 'N/A' and change != 'N/A' else 'N/A'
                    
                    market_data[name] = {
                        'symbol': symbol,
                        'current': round(float(current_price), 2),
                        'change': round(float(change), 2) if change != 'N/A' else 'N/A',
                        'changePercent': round(float(change_percent), 2) if change_percent != 'N/A' else 'N/A',
                        'previous_close': round(float(previous_close), 2) if previous_close != 'N/A' else 'N/A',
                        'exchange': 'BSE'
                    }
                    
                    # Print formatted output
                    print(f"\n✓ {name} ({symbol})")
                    print(f"  Current Price:    ₹ {market_data[name]['current']}")
                    print(f"  Change:           {market_data[name]['change']}")
                    print(f"  Change %:         {market_data[name]['changePercent']}%")
                    print(f"  Previous Close:   ₹ {market_data[name]['previous_close']}")
                else:
                    print(f"✗ {name}: No data available")
                    
                time.sleep(1)  # Add delay to avoid rate limiting
            except Exception as e:
                print(f"✗ {name}: Error - {str(e)[:50]}")
        
        print("\n" + "=" * 80)
        print(f"✅ Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)
        print("\n📋 JSON Data Output:")
        print(json.dumps(market_data, indent=2, default=str))
        
        return market_data
    except Exception as e:
        print(f"Error in get_market_data: {e}")
        return {}

if __name__ == "__main__":
    market_data = get_market_data()
    print(f"\n✨ Total indices fetched: {len(market_data)}")
