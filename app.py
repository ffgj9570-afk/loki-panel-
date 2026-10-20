
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>LOKI PANEL</title>
<style>
* { box-sizing: border-box; }
body {
    margin: 0;
    background: #050507;
    color: white;
    font-family: Arial, sans-serif;
}
header {
    padding: 20px;
    background: #101016;
    border-bottom: 1px solid #252535;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.logo { color: #00eaff; font-size: 23px; font-weight: bold; }
.menu { color: #aaa; font-size: 13px; }
main { max-width: 850px; margin: auto; padding: 20px; }
.balance, .card {
    background: #101016;
    border: 1px solid #29293c;
    border-radius: 20px;
    padding: 24px;
    margin-bottom: 22px;
    box-shadow: 0 0 14px #00d9ff30;
}
.balance { border-color: #ff087d; text-align: center; }
.small { color: #aaa; letter-spacing: 2px; }
.amount { color: #ff087d; font-size: 42px; font-weight: bold; margin-top: 12px; }
h2 { font-size: 18px; color: #00eaff; }
.grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; }
.tile {
    padding: 25px 10px;
    text-align: center;
    background: #101016;
    border: 1px solid #303044;
    border-radius: 17px;
    box-shadow: 0 0 12px #a34dff35;
}
.tile span { display: block; font-size: 27px; margin-bottom: 12px; }
button {
    background: linear-gradient(100deg, #10d99a, #00ddeb);
    border: 0; padding: 13px 18px;
    border-radius: 10px; font-size: 15px;
    font-weight: bold; cursor: pointer;
}
footer { text-align: center; color: #888; padding: 20px; }
@media (max-width: 380px) {
    main { padding: 12px; }
    .grid { gap: 10px; }
    .tile { padding: 20px 5px; }
}
</style>
</head>
<body>
<header>
    <div class="logo">⚡ LOKI PANEL</div>
    <div class="menu">RESELLER DASHBOARD</div>
</header>
<main>
    <section class="balance">
        <div class="small">YOUR CURRENT BALANCE</div>
        <div class="amount">₹0.00</div>
        <p>Welcome to your panel</p>
    </section>
    <section class="card">
        <h2>👑 BECOME A PRO RESELLER</h2>
        <p style="color:#aaa">Manage your products and reseller business from one dashboard.</p>
        <button onclick="alert('Reseller registration will be added in a later step.')">GET STARTED ↗</button>
    </section>
    <section class="grid">
        <div class="tile"><span>💳</span>DEPOSIT</div>
        <div class="tile"><span>🛒</span>BUY KEYS</div>
        <div class="tile"><span>👥</span>MY RESELLERS</div>
        <div class="tile"><span>🔑</span>MY KEYS</div>
        <div class="tile"><span>🕘</span>HISTORY</div>
        <div class="tile"><span>🎁</span>REFER & EARN</div>
    </section>
    <section class="card" style="margin-top:22px">
        <h2>📢 LOKI PANEL UPDATES</h2>
        <p style="color:#aaa">Your panel dashboard starts here.</p>
    </section>
</main>
<footer>© 2026 LOKI PANEL</footer>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
