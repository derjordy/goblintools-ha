import asyncio
from flask import Flask, jsonify, request
from playwright.async_api import async_playwright
import json

app = Flask(__name__)
todos_data = []

@app.route('/todos')
def get_todos():
    return jsonify({"todos": todos_data})

@app.route('/mark-done/<int:todo_id>', methods=['POST'])
def mark_done(todo_id):
    # Hier könnte später ein konkreter DOM-Klick-Script kommen
    return jsonify({"status": "not_implemented", "id": todo_id})

@app.route('/refresh', methods=['POST'])
def refresh():
    asyncio.run(scrape_todos())
    return jsonify({"status": "refreshed"})

async def scrape_todos():
    global todos_data
    from options import username, password

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://goblin.tools/")

        await page.click("text=Log in")
        await page.fill("input[name=email]", username)
        await page.fill("input[name=password]", password)
        await page.click("button:has-text('Log in')")

        await page.wait_for_timeout(5000)

        todos_json = await page.evaluate("localStorage.getItem('todos')")
        todos_data = json.loads(todos_json).get("todos", [])

        await browser.close()

if __name__ == '__main__':
    asyncio.run(scrape_todos())
    app.run(host="0.0.0.0", port=3000)
