from notion_client import Client

# Initialize Notion API client
notion = Client(auth="your-notion-api-token")

async def send_to_notion(content: dict):
    # Example of adding data to a database in Notion
    notion.pages.create(
        parent={"database_id": "your-database-id"},
        properties={
            "Name": {"title": [{"text": {"content": content.get("title", "No Title")}}]},
            "Content": {"rich_text": [{"text": {"content": content.get("body", "No Body")}}]}
        }
    )
    return {"status": "Success"}
